# Python Async and Threading Practice

This project demonstrates how to use **synchronous**, **thread-based**, and **asynchronous (asyncio)** approaches to make HTTP requests in Python. It's designed as a simple exercise to better understand concurrency and performance differences between these methods.

## Requirements

- Python 3.13+
- `aiohttp`
- `requests`

You can install the required packages using pip:

```bash
pip install aiohttp requests
```

## Project Structure

The script compares the performance of three different approaches for fetching data from a set of URLs:

1. **Synchronous Requests (`requests`)**
2. **Multithreading (`threading`)**
3. **Asynchronous Requests (`asyncio` + `aiohttp`)**

Each method prints the total execution time, so you can observe how concurrency improves performance, especially with I/O-bound tasks like network calls.

## Running the Code

You can run different sections of the code by commenting/uncommenting the corresponding lines at the bottom of the script.

Example:

```python
# get_data_sync(urls)  # Takes ~30+ seconds

# ThreadingDownloader.get_data_threading(urls)  # Takes ~4 seconds

asyncio.run(get_data_async_as_wrapper(urls))  # Takes ~3 seconds
```

> **Note**: The script uses `https://postman-echo.com/delay/3`, which simulates a 3-second server response. The URL is repeated to simulate concurrent loading.

## Tested With

- Python 3.13
- PyCharm (IDE)
