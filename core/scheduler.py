from apscheduler.schedulers.asyncio import AsyncIOScheduler

class Scheduler:
    def __init__(self):
        self.obj = AsyncIOScheduler()
        self.obj.start()
    def object(self):
        return self.obj
