import threading
import requests
import time
import asyncio
import aiohttp

def get_data_sync(urls):
    start_time = time.time()

    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time: ", elapsed_time, ".")

    return json_array

class ThreadingDownloader(threading.Thread):
    json_array = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())

        return self.json_array

    def get_data_threading(urls):
        st = time.time()

        threads = []

        for url in urls:
            t = ThreadingDownloader(url)
            t.start() # Runs the run() method.
            threads.append(t)

        for t in threads:
            t.join()
            print(t)

        et = time.time()
        elapsed_time = et - st
        print("Execution time: ", elapsed_time, ".")

async def get_data_async_as_wrapper(urls):
    st = time.time()

    json_array = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                json_array.append(await resp.json())

    et = time.time()
    elapsed_time = et - st
    print("Execution time: ", elapsed_time, ".")


# urls = ["https://postman-echo.com/delay/3"] # Takes 3 seconds to open the page.
urls = ["https://postman-echo.com/delay/3"] * 10

#get_data_sync(urls) # 35 Seconds.

# threads = ThreadingDownloader.get_data_threading(urls) # 4 Seconds.

asyncio.run(get_data_async_as_wrapper(urls))