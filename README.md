
# web_driver_server

`web_driver_server` is a server application designed to handle simultaneous requests for navigating, rendering, and returning page sources given a URL. Utilizing Selenium and undetected ChromeDriver, it provides an API to create, manage, and use web drivers for web scraping or automated testing purposes, supporting operations in a headless Chrome environment.

## Purpose

The primary goal of `web_driver_server` is to facilitate the automated interaction with web pages in a scalable and efficient manner. It enables users to perform web scraping, automated testing, and other browser-based tasks without the overhead of managing individual browser instances manually. By providing a RESTful API, it allows for easy integration with other applications and services, making it a versatile tool for developers and researchers who need to gather data from the web or test their web applications under different conditions.

## Features

- **Driver Management**: Create and manage isolated web driver instances identified by unique IDs.
- **Page Navigation**: Navigate to URLs and fetch page source code, with support for dynamic JavaScript-rendered content.
- **Flexible**: Uses both Selenium WebDriver and undetected ChromeDriver for improved undetectability and performance.
- **REST API**: Interact with the server using a simple REST API to control web drivers and retrieve data.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/web_driver_server.git
    ```

2. Navigate into the cloned repository directory.

    ```bash
    cd web_driver_server
    ```

3. Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask server.

    ```bash
    python app.py
    ```

Your server should now be running on `http://0.0.0.0:4444`.

## Usage

The server provides three main endpoints:

- **Create Driver**: `POST /create_driver` with a JSON body containing `{"driver_uuid": "your_unique_driver_id"}` to create a new driver instance.
- **Quit Driver**: `POST /quit_driver` with a JSON body containing `{"driver_uuid": "your_unique_driver_id"}` to quit and remove a driver instance.
- **Get Page Source**: `POST /get` with a JSON body containing `{"url": "https://example.com", "driver_uuid": "your_unique_driver_id"}` to navigate to a URL and return the page source.

### Example CURL Commands

**Creating a Driver Instance:**

```bash
curl -X POST http://0.0.0.0:4444/create_driver -H "Content-Type: application/json" -d '{"driver_uuid": "example_driver"}'
```

**Quitting a Driver Instance:**

```bash
curl -X POST http://0.0.0.0:4444/quit_driver -H "Content-Type: application/json" -d '{"driver_uuid": "example_driver"}'
```

**Fetching a Page Source:**

```bash
curl -X POST http://0.0.0.0:4444/get -H "Content-Type: application/json" -d '{"url": "https://example.com", "driver_uuid": "example_driver"}'
```

### Example Python Client Provided

In this repo, there is an example python client for you to use.
