import logging
import os

_configured = False


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, include_time: bool = True) -> None:
        super().__init__()
        self.include_time = include_time
        fmt = "%(levelname)-8s | %(message)s"
        if include_time:
            fmt = "%(asctime)s | " + fmt

        self.FORMATS = {
            logging.DEBUG: self.grey + fmt + self.reset,
            logging.INFO: self.green + fmt + self.reset,
            logging.WARNING: self.yellow + fmt + self.reset,
            logging.ERROR: self.red + fmt + self.reset,
            logging.CRITICAL: self.bold_red + fmt + self.reset,
        }

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with colors and indentation.

        Args:
            record: The log record to format.
        """
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        formatted = formatter.format(record)
        indent = 37 if self.include_time else 11
        return formatted.replace("\n", "\n" + " " * indent)


def configure_logging() -> None:
    global _configured
    if _configured:
        return

    handler = logging.StreamHandler()
    log_time = os.getenv("LOG_TIME", "true").lower() == "true"
    handler.setFormatter(CustomFormatter(include_time=log_time))

    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    root = logging.getLogger()
    if root.handlers:
        for h in list(root.handlers):
            root.removeHandler(h)

    logging.basicConfig(level=log_level, handlers=[handler])
    _configured = True


configure_logging()
