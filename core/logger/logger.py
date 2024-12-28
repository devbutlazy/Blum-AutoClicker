import sys
import os
from loguru import logger
from datetime import datetime


def logging_setup():
    logger.remove()

    logger.add(
        sys.stdout,
        colorize=True,
        format="<blue>{time:HH:mm:ss.SS}</blue> | <level>{message}</level>",
        level="DEBUG",
        filter=lambda record: record["level"].name == "DEBUG",
    )

    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:HH:mm:ss.SS}</green> | <level>{message}</level>",
        level="INFO",
        filter=lambda record: record["level"].name == "INFO",
    )

    logger.add(
        sys.stdout,
        colorize=True,
        format="<red>{time:HH:mm:ss.SS}</red> | <level>{message}</level>",
        level="ERROR",
        filter=lambda record: record["level"].name == "ERROR",
    )

    log_file_path = os.path.join(
        "logs", f"{datetime.now().strftime('%d_%m_%H_%M')}_logs.txt"
    )
    
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    logger.add(
        log_file_path,
        format="{time:YYYY-MM-DD HH:mm:ss.SS} | <level>{message}</level>",
        level="DEBUG",
        rotation="00:00",
        retention="7 days", 
        compression="zip", 
    )


logging_setup()
