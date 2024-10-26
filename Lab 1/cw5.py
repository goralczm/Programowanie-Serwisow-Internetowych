import asyncio


async def fib(n: int, memo: dict = {}) -> int:
    if n == 0 or n == 1:
        return n

    if n == 2:
        return 1

    if n in memo:
        return memo[n]

    a = await fib(n - 1, memo)
    b = await fib(n - 2, memo)
    res = a + b
    memo[n] = res

    return res


async def fibonacci_sequence(n: int) -> None:
    for i in range(n + 1):
        res = await fib(i)
        print(res)
        await asyncio.sleep(1)


if __name__ == '__main__':
    with asyncio.Runner() as runner:
        runner.run(fibonacci_sequence(5))
