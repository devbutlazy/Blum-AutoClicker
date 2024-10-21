import pyautogui
import pygetwindow as gw

from typing import Tuple, Any
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
        return window.left, window.top, window.width, window.height

    @staticmethod
    def capture_screenshot(rect: Tuple[int, int, int, int]) -> Any:
        """
        Capture a screenshot of the specified region.

        :param rect: A tuple containing the region coordinates (left, top, width, height)
        :return: A screenshot image of the specified region
        """
        return pyautogui.screenshot(region=rect)

    @staticmethod
    def get_window() -> Any:
        """
        Get the blum window.

        :return: The blum window
        """
        windows = next(
            (
                gw.getWindowsWithTitle(opt)
                for opt in ["TelegramDesktop", "64Gram", "Nekogram", "AyuGram"]
                if gw.getWindowsWithTitle(opt)
            ),
            None,
        )

        if windows and not windows[0].isActive:
            windows[0].minimize()
            windows[0].restore()

            return windows[0]

        return None
