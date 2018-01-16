
# Futures Shell

async/await and asyncio is the great feature for current Python.
However API complicated hard to understand.  This is to make it easy and simple.


## Example


```python
>>> from asyncio import (
...     get_event_loop,
...     sleep,
...     gather,
... )
>>> from futures_shell import (
...     futurify,
...     unwrap,
... )

>>> @futurify
... async def slow_operation(x, y):
...     print('calclating...')
...     await sleep(2)
...     return x + y


>>> @futurify
... def normal_operation(x, y):
...     return x + y


>>> result1 = slow_operation(10, 12)
>>> result1a = slow_operation(11, 22)


>>> loop = get_event_loop()


# TIP: run_until_complete returns unpacked result of Future
>>> loop.run_until_complete(gather(
...     result1,
...     result1a,
... ))
calclating...
calclating...
[22, 33]
>>> print(result1.result(), result1a.result())
22 33

>>> result_a = unwrap(loop, slow_operation(1, 2))
calclating...
>>> print('an unwraped: ', result_a)
an unwraped: 3

>>> result_x = slow_operation(1, 2)
>>> result_y = slow_operation(1, 3)
>>> result_z = slow_operation(1, 4)
>>> result_1 = normal_operation(10, 2)
>>> print(
...     'multiple unwraped',
...     unwrap(
...         loop,
...         result_x,
...         result_y,
...         result_z,
...         result_1,
...     ),
... )
calclating...
calclating...
calclating...
multiple unwraped [3, 4, 5, 12]

>>> result2 = normal_operation(10, 11)
>>> result2
<Future finished result=21>
>>> loop.run_until_complete(result2)
21
>>> print(result2.result())
21

>>> loop.close()

```


## Run Test

```sh
$ python test.py
```

