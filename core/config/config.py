import ujson
import os

from core.logger.logger import logger

from typing import Dict
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

    HU = "hu" # Alias for HU
    HUN = "hu"

    FA = "fa" # Alias for FA
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


def set_language(language: str) -> None:
    """
    Set the language for the program.

    :param: language (str): The language to set.
    :return: None
    """
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config: Dict = ujson.load(f)

        normalized_language = Language.normalize(language)

        config["LANGUAGE"] = normalized_language

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            ujson.dump(config, f, indent=4)

    except (FileNotFoundError, ujson.JSONDecodeError) as e:
        logger.error(f"Error with config file: {e}")
        os._exit(1)

    except Exception as e:
        logger.error(f"An error occurred while updating the config: {e}")
        os._exit(1)


def set_dogs(value: bool) -> None:
    """
    Set the value for collecting dogs.

    :param: value (bool): The value to set.
    :return: None
    """
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config: Dict = ujson.load(f)

        config["COLLECT_DOGS"] = value

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            ujson.dump(config, f, indent=4)

    except (FileNotFoundError, ujson.JSONDecodeError) as e:
        logger.error(f"Error with config file: {e}")
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
