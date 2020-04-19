import asyncio


async def nested():
    return 42


async def main():

    print(await nested())

asyncio.run(main())
