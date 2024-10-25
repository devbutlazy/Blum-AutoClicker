import asyncio
from itertools import product

import keyboard
import mouse
import cv2
import numpy as np

from typing import Tuple, Any
from core.clicker.misc import Utilities
from core.logger.logger import logger
from core.localization.localization import get_language
from core.config.config import get_config_value


class BlumClicker:
    def __init__(self):
        self.utils = Utilities()
        self.paused: bool = True
        self.window_options: str | None = None

    async def handle_input(self) -> bool:
        """
        Handles the input for pausing or starting the clicker.

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
    def collect_green(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found point.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size
        avoid_color = (196, 247, 94)

        for x, y in product(range(0, width, 20), range(0, height, 20)):
            r, g, b = screen.getpixel((x, y))
            greenish_range = (b < 125) and (102 <= r < 220) and (200 <= g < 255)

            if (r, g, b) == avoid_color:
                continue

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

    @staticmethod
    def collect_dog(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Detepct and click on the dog's face based on its specific color.

        :param screen: the screenshot in BGR format
        :param rect: the bounding rectangle of the screen
        :return: whether the dog was found
        """
        hsv = cv2.cvtColor(
            cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2HSV
        )

        lower_white = np.array([0, 0, 200], dtype=np.uint8)
        upper_white = np.array([180, 55, 255], dtype=np.uint8)

        mask = cv2.inRange(hsv, lower_white, upper_white)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if 500 < area < 3000:
                x, y, w, h = cv2.boundingRect(contour)
                screen_x = rect[0] + x + w // 2
                screen_y = rect[1] + y + h // 2

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
                return logger.error(get_language("WINDOW_NOT_FOUND"))

            logger.info(get_language("CLICKER_INITIALIZED"))
            logger.info(get_language("p").format(window=window.title))
            logger.info(get_language("PRESS_S_TO_START"))

            while True:
                if await self.handle_input():
                    continue

                rect = self.utils.get_rect(window)

                screenshot = self.utils.capture_screenshot(rect)

                self.collect_green(screenshot, rect)
                self.collect_freeze(screenshot, rect)

                if get_config_value("COLLECT_DOGS"):
                    self.collect_dog(screenshot, rect)

        except (Exception, ExceptionGroup) as error:
            logger.error(get_language("WINDOW_CLOSED").format(error=error))
