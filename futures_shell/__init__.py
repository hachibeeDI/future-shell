import typing

from functools import partial
from asyncio import (
    gather,
    ensure_future,
    iscoroutinefunction,
    Future,
)


def futurify(func):

    def __wrapper(*args, **kw):
        if iscoroutinefunction(func):
            return ensure_future(func(*args, **kw))

        future = Future()
        future.set_result(func(*args, **kw))
        return future

    return __wrapper
