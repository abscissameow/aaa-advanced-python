import asyncio
from typing import Coroutine


async def limit_execution_time(
        coro: Coroutine, max_execution_time: float) -> None:
    task = asyncio.create_task(coro)
    try:
        await asyncio.wait_for(task, timeout=max_execution_time)
    except asyncio.TimeoutError:
        task.cancel()
        await task


async def limit_execution_time_many(
        *coros: Coroutine, max_execution_time: float) -> None:
    tasks = [asyncio.create_task(coro) for coro in coros]
    try:
        await asyncio.wait(tasks, timeout=max_execution_time)
    except asyncio.TimeoutError:
        pass

    for task in tasks:
        if not task.done():
            task.cancel()
            await task
