from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class PostgreSQLSettings(BaseSettings):
    """PostgreSQL database settings."""

    PG_URL: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class RedisSettings(BaseSettings):
    """Redis database settings."""

    REDIS_URL: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class RabbitMQSettings(BaseSettings):
    """RabbitMQ settings."""

    RABBITMQ_URL: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class SmtpSettings(BaseSettings):
    """SMTP settings."""

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: SecretStr
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class AuthSettings(BaseSettings):
    """Authentication settings."""

    JWT_SECRET_KEY: SecretStr
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_days: int
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


class Settings(BaseSettings):
    """Base Settings."""

    postgresql: PostgreSQLSettings = PostgreSQLSettings()
    redis: RedisSettings = RedisSettings()
    rabbitmq: RabbitMQSettings = RabbitMQSettings()
    smtp: SmtpSettings = SmtpSettings()
    auth: AuthSettings = AuthSettings()

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=".env", extra="allow"
    )


settings: Settings = Settings()
