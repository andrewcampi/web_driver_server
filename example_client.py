import requests
import uuid

# Base URL of the web_driver_server
BASE_URL = "http://0.0.0.0:3333"

# Generate a unique driver UUID using the uuid library
driver_uuid = str(uuid.uuid4())

def create_driver():
    """
    Sends a POST request to the server to create a new driver instance.
    """
    # Define the endpoint for creating a driver
    endpoint = f"{BASE_URL}/create_driver"
    # JSON payload with the driver_uuid
    payload = {"driver_uuid": driver_uuid}
    # Send POST request and get the response
    response = requests.post(endpoint, json=payload)
    print(f"Create Driver Response: {response.json()}")

def get_page_source(url):
    """
    Fetches the page source for the given URL using the created driver instance.
    """
    # Define the endpoint for getting page source
    endpoint = f"{BASE_URL}/get"
    # JSON payload with the driver_uuid and URL
    payload = {"driver_uuid": driver_uuid, "url": url}
    # Send POST request and get the response
    response = requests.post(endpoint, json=payload)
    print(f"Page Source Response: {response.json()}")

def quit_driver():
    """
    Sends a POST request to the server to quit and remove the driver instance.
    """
    # Define the endpoint for quitting a driver
    endpoint = f"{BASE_URL}/quit_driver"
    # JSON payload with the driver_uuid
    payload = {"driver_uuid": driver_uuid}
    # Send POST request and get the response
    response = requests.post(endpoint, json=payload)
    print(f"Quit Driver Response: {response.json()}")

if __name__ == "__main__":
    # Step 1: Create a new driver instance
    create_driver()
    
    # Step 2: Get the page source for "http://example.com"
    get_page_source("http://example.com")
    
    # Step 3: Quit and remove the driver instance
    quit_driver()
