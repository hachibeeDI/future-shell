import typing

from functools import partial
from asyncio import (
    gather,
    ensure_future,
    iscoroutinefunction,
    Future,
)


async def _set_result_to_future(future, async_func, *args, **kw) -> None:
    result = await async_func(*args, **kw)
    future.set_result(result)


def futurify(func):
    def __wrapper(*args, **kw):
        future = Future()
        if iscoroutinefunction(func):
            ensure_future(_set_result_to_future(future, func, *args, **kw))
        else:
            future.set_result(func(*args, **kw))
        return future
    return __wrapper


def unwrap(loop, *futures):
    if len(futures) == 1:
        future = futures[0]
    else:
        future = gather(*futures)
    loop.run_until_complete(future)
    return future.result()
