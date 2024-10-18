import asyncio
from time import time
from itertools import product

import keyboard
import mouse
import pygetwindow as gw

from typing import Tuple, Any
from core.clicker.misc import Utilities
from core.logger.logger import logger
from core.localization.localization import get_language


class BlumClicker:
    def __init__(self):
        self.utils = Utilities()

        self.paused: bool = True
        self.window_options: str | None = None
        self.game_active: bool = False  # To track game state (active or ended)

    async def handle_input(self) -> bool:
        """
        Handles the input.

        :return: whether the input was handled
        """

        if keyboard.is_pressed("s") and self.paused:
            self.paused = False
            logger.info(get_language("PRESS_P_TO_PAUSE"))
            await asyncio.sleep(0.2)

        elif keyboard.is_pressed("p"):
            self.paused = not self.paused
            logger.info(
                get_language("PROGRAM_PAUSED")
                if self.paused
                else get_language("PROGRAM_RESUMED")
            )
            await asyncio.sleep(0.2)

        return self.paused

    @staticmethod
    def collect_point(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found point.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size

        for x, y in product(range(0, width, 20), range(0, height, 20)):
            r, g, b = screen.getpixel((x, y))

            greenish_range = (b < 125) and (102 <= r < 220) and (200 <= g < 255)

            if greenish_range:
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)

                return True

        return False

    @staticmethod
    def collect_freeze(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found freeze.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size

        for x, y in product(range(0, width, 20), range(0, height, 20)):
            r, g, b = screen.getpixel((x, y))

            blueish_range = (215 < b < 255) and (100 <= r < 166) and (220 <= g < 254)

            if blueish_range:
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)
                return True

        return False

    async def run(self) -> None:
        """
        Runs the clicker.
        """

        try:
            window = self.utils.get_window()
            if not window:
                logger.error(get_language("WINDOW_NOT_FOUND"))
                return

            logger.info(get_language("CLICKER_INITIALIZED"))
            logger.info(get_language("FOUND_WINDOW").format(window=window.title))
            logger.info(get_language("PRESS_S_TO_START"))

            while True:
                if await self.handle_input():
                    continue

                rect = self.utils.get_rect(window)

                screenshot = self.utils.capture_screenshot(rect)

                self.collect_point(screenshot, rect)
                self.collect_freeze(screenshot, rect)

        except gw.PyGetWindowException as error:
            logger.error(get_language("WINDOW_CLOSED").format(error=error))
