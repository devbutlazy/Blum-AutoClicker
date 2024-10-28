import ujson
import os

from core.logger.logger import logger

from typing import Dict, Any
from enum import Enum

CONFIG_PATH = "core/config/config.json"


class Language(Enum):
    EN = "en"
    ENG = "en"
    GB = "en"  # Alias for EN

    UA = "ua"
    UKR = "ua"  # Alias for UA

    PL = "pl"
    POL = "pl"  # Alias for PL

    HU = "hu"  # Alias for HU
    HUN = "hu"

    FA = "fa"  # Alias for FA
    PR = "fa"

    @classmethod
    def is_valid(cls, lang: str) -> bool:
        """
        Check if the language string is a valid Language enum member.

        :param lang: The language string to check.
        :return: True if the language is valid, False otherwise.
        """
        return lang.upper() in cls.__members__

    @classmethod
    def normalize(cls, lang: str) -> str:
        """
        Normalize the language string to a valid Language enum member.

        :param lang: The language string to normalize.
        :return: The normalized language string.
        """
        member = cls.__members__.get(lang.upper(), cls.EN)
        return member.value


def set_config(key: str, value: Any) -> None:
    """
    Set a specific configuration key to a given value.

    :param key: The configuration key to update.
    :param value: The new value to set for the specified key.
    :return: None
    """
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config: Dict[str, Any] = ujson.load(f)

        if key == "LANGUAGE":
            value = Language.normalize(value)

        elif key == "COLLECT_DOGS":
            value = True if value.lower() == "true" else False

        config[key] = value

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            ujson.dump(config, f, indent=4)

    except (FileNotFoundError, ujson.JSONDecodeError) as e:
        logger.error(f"Error with config file: {e}")
        os._exit(1)

    except Exception as e:
        logger.error(f"An error occurred while updating the config: {e}")
        os._exit(1)


def get_config_value(key: str) -> str:
    """
    Get the value of a config key.

    :param: key (str): The key to get the value of.
    :return: str: The value of the config key or None if it doesn't exist.
    """
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config: Dict = ujson.load(f)

        return config.get(key, None)

    except (FileNotFoundError, ujson.JSONDecodeError) as e:
        logger.error(f"Error with config file: {e}")
        os._exit(1)

    except Exception as e:
        logger.error(f"An error occurred while getting the config value: {e}")
        os._exit(1)
