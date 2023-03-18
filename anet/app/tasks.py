import asyncio
import traceback
# from aiohttp import ClientSession

NEWS = ['fb.com']
emails = ['email1', 'email2']

interval = 4
sem = asyncio.Semaphore(5)


async def _worker(url):
    print('Start parse')
    async with sem:
        await asyncio.sleep(2)
    print(url, 'end parse')
    return url


async def parser(app):
    loop = asyncio.get_running_loop()
    event = asyncio.Event()

    work = True

    async def _looper(news):
        while work:
            loop.call_later(interval, lambda e: e.set(), event)
            tasks = asyncio.gather(*[_worker(n) for n in news])
            await event.wait()
            event.clear()
            exc = tasks.exception()
            try:
                await tasks
            except asyncio.CancelledError:
                ...
            except RuntimeError:
                traceback.print_exc()
            else:
                print(tasks.result())

    def _done(task):
        try:
            task.result()
        except (asyncio.CancelledError, RuntimeError) as err:
            print(err)
            print('#' * 10)
            asyncio.create_task(_looper(NEWS)).add_done_callback(_done)

    asyncio.create_task(_looper(NEWS)).add_done_callback(_done)
    # task = asyncio.create_task(_looper(NEWS))
    yield
    work = False
    # event.set()
    # await task


async def sender(app):
    ...
