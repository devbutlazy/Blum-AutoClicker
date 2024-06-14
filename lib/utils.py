import pyautogui

from typing import Literal, Tuple, Any
from dataclasses import dataclass


@dataclass
class Utilities:

    @staticmethod
    def get_rect(window) -> Tuple[int, int, int, int]:
        """
        Get the rectangle coordinates of the given window.

        :param window: The window object
        :return: A tuple containing the coordinates (left, top, width, height)
        """
        return (window.left, window.top, window.width, window.height)

    @staticmethod
    def capture_screenshot(rect: Tuple[int, int, int, int]) -> Any:
        """
        Capture a screenshot of the specified region.

        :param rect: A tuple containing the region coordinates (left, top, width, height)
        :return: A screenshot image of the specified region
        """
        return pyautogui.screenshot(region=rect)

    
    @staticmethod
    def custom_print(
        text: str,
        color: Literal["info", "debug", "error", "warn"] = "warn",
    ) -> None:
        """
        Print text with colors

        :param text: the text to print
        :param color: the color of the text
        :param print_bool: whether to print the text
        :param write_file: whether to write the text to a file
        :param file: the file to write the text to
        :return: 
        """
        colors = {
            "info": f"\033[1;32;48m{text}\033[1;37;0m ",
            "debug": f"\033[1;34;48m{text}\033[1;37;0m",
            "error": f"\033[1;31;48m{text}\033[1;37;0m",
            "warn": f"\033[1;33;48m{text}\033[1;37;0m",
        }

        print(colors[color])
        return 
