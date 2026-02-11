import asyncio

class Portal(asyncio.Barrier):
    def __init__(self, parties):
        super().__init__(parties)
        self._topic = None
        self._assigned_topic = None
        self._topic_lock = asyncio.Lock()
    
    @property
    def topic(self):
        return self._topic
    
    async def wait(self, topic = None):
        if topic is not None:
            async with self._topic_lock:
                if self._assigned_topic is None:
                    self._assigned_topic = topic
        
        try:
            result = await super().wait()
        except asyncio.BrokenBarrierError:
            async with self._topic_lock:
                self._assigned_topic = None
            raise
        
        if result == self.parties - 1:
            self._topic = self._assigned_topic
            async with self._topic_lock:
                self._assigned_topic = None

        await asyncio.sleep(0)
        
        return result
    
    async def reset(self):
        await asyncio.sleep(0)
        await super().reset()
        self._topic = None
        async with self._topic_lock:
            self._assigned_topic = None


