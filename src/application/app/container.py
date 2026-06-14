from dishka import AsyncContainer, make_async_container

from src.application.common.shared.provider import SharedProvider
from src.application.modules.auth.provider import AuthModuleProvider
from src.application.modules.user.provider import UserProvider

container: AsyncContainer = make_async_container(
    SharedProvider(), UserProvider(), AuthModuleProvider()
)
