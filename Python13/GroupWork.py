import asyncio
from functools import wraps
from typing import List

class Loop:
    _instances: List['Loop'] = [] 
    _current_index: int = 0  
    _should_stop: bool = False 
    _queue = asyncio.Queue()  
    
    def __init__(self):
        self._func = None 
        self._index = len(Loop._instances)
        Loop._instances.append(self) 
    
    def __call__(self, func):
        self._func = func
        
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if self._index == 0:
                Loop._should_stop = False
                Loop._current_index = 0
                await Loop._queue.put(0)
            
            while not Loop._should_stop:
                next_index = await Loop._queue.get()
                
                if next_index != self._index:
                    await Loop._queue.put(next_index)
                    await asyncio.sleep(0) 
                    continue
                
                if Loop._should_stop:
                    return None
                
                result = await self._func(*args, **kwargs)

                if result is None:
                    Loop._should_stop = True
                    while not Loop._queue.empty():
                        try:
                            Loop._queue.get_nowait()
                        except:
                            pass
                    return None
                else:
                    Loop._current_index = (Loop._current_index + 1) % len(Loop._instances)
                    await Loop._queue.put(Loop._current_index)
                
                await asyncio.sleep(0)
            
            return None
        
        return wrapper
    
    @classmethod
    def reset(cls):
        cls._instances = []
        cls._current_index = 0
        cls._should_stop = False
        cls._queue = asyncio.Queue()

