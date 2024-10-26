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
        return lang in cls._value2member_map_

    @classmethod
    def normalize(cls, lang: str) -> str:
        aliases = {
            "ua": cls.UA.value,
            "ukr": cls.UA.value,
            "en": cls.EN.value,
            "gb": cls.EN.value,
            "pl": cls.PL.value,
            "pol": cls.PL.value,
            "hu": cls.HU.value,
            "hun": cls.HU.value,
            "fa": cls.FA.value,
            "pr": cls.FA.value
        }
        return aliases.get(lang.lower(), cls.EN.value)  # Default to English


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
