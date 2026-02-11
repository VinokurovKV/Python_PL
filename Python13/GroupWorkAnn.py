import asyncio
from functools import wraps

class Loop:
    _tasks = []
    _current = 0
    _stop = False
    _lock = asyncio.Lock()
    
    def __init__(self):
        self.idx = len(Loop._tasks)
        Loop._tasks.append(None)
    
    def __call__(self, func):
        Loop._tasks[self.idx] = func
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if self.idx == 0:
                async with Loop._lock:
                    Loop._current = 0
                    Loop._stop = False
            
            while not Loop._stop:
                while True:
                    async with Loop._lock:
                        if Loop._stop:
                            return None
                        if Loop._current == self.idx:
                            break
                    await asyncio.sleep(0)
                
                try:
                    result = await func(*args, **kwargs)
                except Exception:
                    async with Loop._lock:
                        Loop._stop = True
                    raise
                
                async with Loop._lock:
                    if result is None:
                        Loop._stop = True
                        return None
                    else:
                        Loop._current = (Loop._current + 1) % len(Loop._tasks)
                
                await asyncio.sleep(0)
            
            return None
        
        return wrapper
    
    @classmethod
    def reset(cls):
        cls._tasks = []
        cls._current = 0
        cls._stop = False


from random import randrange, seed
N, M = 15557, 15558
coros = []
stat = 0
for i in range(M):
    @Loop()
    async def pA(i=i):
        global stat
        stat += i
        return randrange(N) or None
    coros.append(pA)

async def Run(*coros):
    async with asyncio.TaskGroup() as tg:
        for coro in coros:
            tg.create_task(coro())
    print(stat)

seed(1337)
asyncio.run(Run(*coros))