import logging
from dataclasses import dataclass
from email.message import EmailMessage

import aiosmtplib

from src.application.common.shared.config.config import settings
from src.application.modules.user.interfaces.confirmation.confirmation import (
    IAccountConfirmation,
)
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class AccountConfirmation(IAccountConfirmation):

    async def send_confirmation(self, recipient: str, subject: str, body: str) -> None:
        message: EmailMessage = EmailMessage()

        message["From"] = settings.smtp.SMTP_USER
        message["To"] = recipient
        message["Subject"] = subject

        message.set_content(body)

        await aiosmtplib.send(
            message,
            hostname=settings.smtp.SMTP_HOST,
            port=settings.smtp.SMTP_PORT,
            start_tls=True,
            username=settings.smtp.SMTP_USER,
            password=settings.smtp.SMTP_PASSWORD.get_secret_value(),
        )

        log.info("Message successfully was sended into %s", recipient)
