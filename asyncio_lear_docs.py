import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def main():
    await asyncio.gather(
        factorial("C", 4),
        factorial("B", 3),
        factorial("A", 2),
    )

asyncio.run(main())
