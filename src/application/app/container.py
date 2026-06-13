from dishka import make_async_container, AsyncContainer
from src.application.common.shared.provider import SharedProvider
from src.application.modules.user.provider import UserProvider

container: AsyncContainer = make_async_container(SharedProvider(), UserProvider())
