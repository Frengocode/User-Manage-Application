from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from src.application.common.shared.database.sqlalchemy.mixin import \
    SQLAlchemyMixin
from src.application.common.shared.database.sqlalchemy.sqlalchemy_database import \
    SQLAlchemyBase
from src.application.modules.user.domain.value_objects.role import RoleEnum


class SQLAlchemyUser(SQLAlchemyBase, SQLAlchemyMixin):

    email: Mapped[str] = mapped_column(String, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[RoleEnum] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=True)
    surname: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, index=True, default=False)
