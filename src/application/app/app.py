from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from src.application.app.container import container
from src.application.modules.auth.controllers.api.v1.router import auth_api_v1_router
from src.application.modules.user.controllers.api.v1.router import users_api_v1_router
from src.application.modules.user.infrastructure.schedular.schedular import (
    SchedulerService,
)

app: FastAPI = FastAPI(title="User managment app")
app.include_router(users_api_v1_router)
app.include_router(auth_api_v1_router)


schedular: SchedulerService = SchedulerService(container=container)

setup_dishka(container=container, app=app)


@app.on_event("startup")
async def startup():
    schedular.start()
