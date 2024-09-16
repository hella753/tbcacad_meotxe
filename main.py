import time
import asyncio
from thread_Version import ThreadVersion
from async_Version import AsyncVersion


def main():
    start = time.perf_counter()
    print(f"Start time: {start}")

    BASE_URL = "https://jsonplaceholder.typicode.com/posts/"

    # uncomment for thread version. ხან ერთი ვერსია ჯობს ხან მეორე
    # thread_v = ThreadVersion(BASE_URL)
    # thread_v.run_threads()

    # აღმოვაჩინე რომ პითონის 3.9 ვერსიაზე აერორებს ამის გარეშე
    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    async_v = AsyncVersion(BASE_URL)
    asyncio.run(async_v.main_async())

    end = time.perf_counter()
    print(f"End time: {round(end - start, 2)}")


if __name__ == "__main__":
    main()
