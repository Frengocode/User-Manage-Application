from dishka import Provider, Scope, provide

from src.application.common.shared.auth.infrastructure.token.access_token_generator import (
    AccessTokenGenerator,
)
from src.application.common.shared.auth.infrastructure.token.refresh_token_generator import (
    RefreshTokenGenerator,
)
from src.application.common.shared.auth.interfaces.token import (
    refresh_token_generator,
    token_generator,
)
from src.application.modules.auth.use_cases.login import LoginUseCase
from src.application.modules.auth.use_cases.refresh_token import RefreshTokenUseCase
from src.application.modules.user.interfaces.use_cases.iget_auth_user import (
    IGetAuthUserUseCase,
)


class AuthModuleProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def login_use_case(
        self,
        get_auth_user_use_case: IGetAuthUserUseCase,
        token_generator: token_generator.ITokenGenerator,
        refresh_token_generator: refresh_token_generator.IRefreshTokenGenerator,
    ) -> LoginUseCase:

        return LoginUseCase(
            get_auth_user_use_case=get_auth_user_use_case,
            token_generator=token_generator,
            refresh_token_generator=refresh_token_generator,
        )

    @provide(scope=Scope.REQUEST)
    def access_token_generator_provider(self) -> token_generator.ITokenGenerator:
        return AccessTokenGenerator()

    @provide(scope=Scope.REQUEST)
    def refresh_token_generator_provider(
        self,
    ) -> refresh_token_generator.IRefreshTokenGenerator:
        return RefreshTokenGenerator()

    @provide(scope=Scope.REQUEST)
    def refresh_token_use_case(
        self, token_generator: token_generator.ITokenGenerator
    ) -> RefreshTokenUseCase:
        return RefreshTokenUseCase(token_generator=token_generator)
