from datetime import UTC, datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declarative_mixin,
    declared_attr,
    mapped_column,
)


@declarative_mixin
class SQLAlchemyMixin(DeclarativeBase):
    """Mixin for SqlAlchemy models."""

    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), onupdate=lambda: datetime.now(UTC)
    )
