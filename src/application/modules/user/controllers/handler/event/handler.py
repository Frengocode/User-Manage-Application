from dishka.integrations.faststream import FromDishka, inject
from faststream import FastStream
from faststream.rabbit import RabbitBroker

from src.application.common.shared.config.config import settings
from src.application.modules.user.constants.constants import (
    USER_CREATED_ROUTING_KEY,
    USERS_EXCHANGE,
)
from src.application.modules.user.infrastructure.handlers.user_created_handler import (
    UserCreatedEventHandler,
)
from src.application.modules.user.interfaces.events.payload.user_created_payload import (
    UserCreatedEventPayload,
)
from src.application.modules.user.interfaces.events.user_created_event import (
    UserCreatedEventPayload,
)

broker: RabbitBroker = RabbitBroker(settings.rabbitmq.RABBITMQ_URL.get_secret_value())
router: FastStream = FastStream(broker)


@broker.subscriber(exchange=USERS_EXCHANGE, queue=USER_CREATED_ROUTING_KEY)
@inject
async def user_created_handler(
    payload: UserCreatedEventPayload, handler: FromDishka[UserCreatedEventHandler]
) -> None:
    return await handler.handle(payload=payload)
