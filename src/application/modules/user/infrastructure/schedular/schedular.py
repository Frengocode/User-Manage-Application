# src/infrastructure/scheduler/scheduler.py

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dishka import AsyncContainer, Scope

from src.application.modules.user.interfaces.services.iuser_service import IUserService


class SchedulerService:
    def __init__(self, container: AsyncContainer):
        self.container = container
        self.scheduler = AsyncIOScheduler()

    def start(self):
        self.scheduler.add_job(
            self.run_delete_users,
            "interval",
            minutes=1,  # 👈 каждые 1 минуту
        )
        self.scheduler.start()

    async def run_delete_users(self):
        async with self.container(scope=Scope.REQUEST) as c:
            service: IUserService = await c.get(IUserService)
            await service.delete_not_activated_users()
