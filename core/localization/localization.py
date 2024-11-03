import ujson
from pathlib import Path

from core.logger.logger import logger

from typing import Dict, Union


def load_json_file(file_path: Union[str, Path]) -> Dict:
    """
    Load a JSON file and return its contents as a dictionary.

    :param file_path: The path to the JSON file.

    :return: Parsed JSON content, or an empty dictionary if an error occurs.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return ujson.load(file)

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")

    except ujson.JSONDecodeError:
        logger.error(f"Failed to decode JSON in file: {file_path}")

    return {}


def get_config_value(key: str) -> str:
    """
    Retrieve a value from the configuration JSON file.

    :param key: The key to look up in the configuration file.

    :return: The value associated with the key, or None if not found.
    """
    config_path = Path("core/config/config.json")
    config_data = load_json_file(config_path)

    return config_data.get(key)


def get_language(key: str) -> str:
    """
    Retrieve a localized string based on the key from the language file
    defined in the configuration.

    :param key: The key to look up in the language file.

    :return: The localized string or an error message if the key is not found.
    """
    lang: str = get_config_value("LANGUAGE") or "en"  # Fallback to 'en' if LANGUAGE not found
    file_path: Path = Path(f"core/localization/langs/{lang}.json")

    data: Dict = load_json_file(file_path) or load_json_file("core/localization/langs/en.json")

    return ujson.dumps(
        data.get(key, f"Localization error: '{key}' not found."), 
        ensure_ascii=False, 
        indent=4
    ) if lang == "fa" else data.get(key, f"Localization error: '{key}' not found.")
