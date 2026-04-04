# Concurrency → dealing with multiple tasks at once (but not necessarily at the same exact time)

"""
Concurrency is useful when tasks spend time waiting (I/O-bound tasks), like:

API calls
File reading/writing
Network requests
"""

import asyncio


async def task(name, delay):
    print(f"Start {name}")
    await asyncio.sleep(delay)
    print(f"End {name}")


async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 1),
        task("Task 3", 3)
    )

asyncio.run(main())


"""
🔹 Real-world use case (Concurrency)

👉 Web scraping / API calls

Example:

Fetching data from 100 websites
Instead of waiting one-by-one, you send all requests together

Used in:

Chat apps (handling many users)
Web servers
Bots
"""
