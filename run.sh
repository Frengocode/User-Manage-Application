#!/bin/sh

alembic upgrade headd &

uvicorn src.application.app.app:app --reload --host 0.0.0.0 --port 8000 &

faststream run src.application.modules.user.controllers.handler.event.handler:router