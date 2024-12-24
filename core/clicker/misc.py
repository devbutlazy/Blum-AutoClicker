import pyautogui
import pywinctl as pwc

from typing import Tuple, Any
from functools import wraps
from dataclasses import dataclass


def check_share_button(func):
    """
    Decorator to check if the share button is present on the screen.
    If the share button is visible, the function will return False,
    avoiding further actions like clicking.
    """

    @wraps(func)
    def wrapper(screen, rect, *args, **kwargs):
        width, height = screen.size
        share_button_check = screen.getpixel(
            (int(width * 0.16), int(height * 0.76))
        ) == (40, 40, 40)

        if share_button_check:
            return False

        return func(screen, rect, *args, **kwargs)

    return wrapper


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
    def get_window() -> Any:
        """
        Get the blum window.

        :return: The blum window
        """
        windows = next(
            (
                pwc.getWindowsWithTitle(opt)
                for opt in ["TelegramDesktop", "64Gram", "AyuGram", "telegram-desktop"]
                if pwc.getWindowsWithTitle(opt)
            ),
            None,
        )

        window = windows[0] if windows else None

        if window and not window.isActive:
            window.minimize()
            window.restore()

            return window

        return None
