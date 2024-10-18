import ujson

from core.logger.logger import logger

from typing import Dict
from enum import Enum

CONFIG_PATH = "core/config/config.json"


class Language(Enum):
    EN = "en"
    GB = "en"  # Alias for EN

    UA = "ua"
    UKR = "ua"  # Alias for UA

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

        logger.info(f"Language set to: {normalized_language}")

    except (FileNotFoundError, ujson.JSONDecodeError) as e:
        logger.error(f"Error with config file: {e}")

    except Exception as e:
        logger.error(f"An error occurred while updating the config: {e}")
