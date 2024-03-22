# undetected chrome driver imports
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
# General imports
import os
from time import sleep
import re
# flask server imports
from flask import Flask, request, jsonify
# Selenium imports
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


app = Flask(__name__)

drivers = {}


@app.route('/create_driver')
def create_driver():
	print("Creating driver ....")
	global drivers

	data = request.json 

	print("data:", str(data))

	if not data or 'driver_uuid' not in data:
		return jsonify({"code": "invalid request: no driver_uuid provided"}), 400

	if data['driver_uuid'] in list(drivers.keys()):
		return jsonify({"code": "invalid request: driver_uuid already exists"}), 400

	print("-> driver_uuid =", data["driver_uuid"])
	try:
		options = uc.ChromeOptions()
		options.add_argument("--incognito")
		options.add_argument("--no-sandbox")
		driver = uc.Chrome(headless=False, options=options, version_main=121)
	except:
		options = ChromeOptions()
		options.add_argument("--disable-web-security")
		options.add_argument("--allow-running-insecure-content")
		driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

	print("-> Driver created!")
	drivers[data['driver_uuid']] = driver

	return jsonify({"code": "successfully created driver"}), 200


@app.route('/quit_driver')
def quit_driver():
	print("Quitting driver...")
	global drivers

	data = request.json 

	if not data or 'driver_uuid' not in data:
		return jsonify({"code": "invalid request: no driver_uuid provided"}), 400

	if not data['driver_uuid'] in list(drivers.keys()):
		return jsonify({"code": "invalid request: the provided driver_uuid does not exist"}), 400

	print("-> driver_uuid =", data["driver_uuid"])
	drivers[data['driver_uuid']].quit()
	print("-> Driver quit!")
	drivers.pop(data['driver_uuid'], None)
	print("-> Driver removed from dict!")

	return jsonify({"code": "successfully quit driver"}), 200


@app.route('/get')
def get_page():
	print("Get request ...")
	data = request.json # Get JSON data from the request

	# Check if 'url' parameter is present and is a valid URL
	if not data or 'url' not in data:
		print("-> 400: no data or 'url'")
		return jsonify({"code": "invalid request: no url provided"}), 400

	if 'driver_uuid' not in data:
		print('-> 400: no driver_uuid provided.')
		return jsonify({"code": "invalid request: no driver_uuid provided"}), 400

	if data['driver_uuid'] not in list(drivers.keys()):
		print("-> 400: driver not created. Here are the ones that are: ", str(list(drivers.keys())))
		return jsonify({"code": "invalid request: you need to create the driver first"}), 400

	target_url = data['url']
	print("-> driver_uuid =", data['driver_uuid'])
	print("-> target_url =", target_url)
	driver = drivers[data['driver_uuid']]

	try:
		driver.get(target_url)
		sleep(4)
		page_source = driver.page_source
		print("-> Request succesful!")
		return jsonify({"code": "successful requests", "page_source": page_source}), 200
	except Exception as e:
		print("-> Exception occured while requesting the page:", str(e))
		return jsonify({"code": f"Request failure: {str(e)}"}), 400


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3333, debug=True)
