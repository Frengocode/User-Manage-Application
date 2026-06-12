import logging

logging.basicConfig(level=logging.INFO)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the specified name."""

    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
