# my_namespace/m1/m1.py
import asyncio


async def fn():
    print('This is ')
    await asyncio.sleep(1)
    print('asynchronous programming')
    await asyncio.sleep(1)
    print('and not multi-threading')


asyncio.run(fn())
if __name__ == "__main__":
    asyncio.run(fn())

