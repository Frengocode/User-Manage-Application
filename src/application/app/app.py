from fastapi import FastAPI
from src.application.modules.user.controllers.api.v1.router import users_api_v1_router
from src.application.app.container import container
from dishka.integrations.fastapi import setup_dishka

app: FastAPI = FastAPI(title="User managment app")
app.include_router(users_api_v1_router)


setup_dishka(container=container, app=app)
