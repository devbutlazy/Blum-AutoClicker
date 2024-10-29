import os
import asyncio
import time
import random
from itertools import product

import keyboard
import mouse
import pyautogui

from core.clicker.misc import Utilities
from core.logger.logger import logger
from core.localization.localization import get_language
from core.config.config import get_config_value

from typing import Tuple, Any


class BlumClicker:
    def __init__(self):
        self.utils = Utilities()

        self.paused: bool = True
        self.window_options: str | None = None
        self.replays: int = 0

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

        # 589

        for x, y in product(range(0, width, 20), range(0, int(height * 0.8272), 20)):
            r, g, b = screen.getpixel((x, y))
            greenish_range = (b < 125) and (102 <= r < 220) and (200 <= g < 255)

            if greenish_range:
                # if (r, g, b) == (196, 248, 92):
                #     return False

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
    def collect_pumpkin(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found point.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size

        for x, y in product(range(0, width, 20), range(0, height, 20)):
            r, g, b = screen.getpixel((x, y))
            pamkin_range = (35 < b < 63) and (220 <= r < 233) and (114 <= g < 128)

            if pamkin_range:
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)

                return True

        return False

    def detect_replay(self, screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the 'Play (nn left)' button.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """

        max_replays = get_config_value("REPLAYS")
        replay_delay = get_config_value("REPLAY_DELAY")

        screen_x = rect[0] + int(screen.size[0] * 0.3075)
        screen_y = rect[1] + int(screen.size[1] * 0.87)

        color = pyautogui.pixel(screen_x, screen_y)

        if not color == (255, 255, 255):
            return False

        if self.replays >= max_replays:
            logger.error(
                get_language("REPLAY_LIMIT_REACHED").format(replays=max_replays)
            )
            os._exit(0)

        logger.debug(
            f"Detected the replay button. Remaining replays: {max_replays - self.replays}"
        )
        time.sleep(random.randint(replay_delay, replay_delay + 3) + random.random())

        mouse.move(
            screen_x + random.randint(1, 10),
            screen_y + random.randint(1, 10),
            absolute=True,
        )
        mouse.click(button=mouse.LEFT)

        time.sleep(0.5)

        self.replays += 1
        return True

    async def run(self) -> None:
        """
        Runs the clicker.
        """
        try:
            window = self.utils.get_window()
            if not window:
                return logger.error(get_language("WINDOW_NOT_FOUND"))

            logger.info(get_language("CLICKER_INITIALIZED"))
            logger.info(get_language("FOUND_WINDOW").format(window=window.title))
            logger.info(get_language("PRESS_S_TO_START"))

            while True:
                if await self.handle_input():
                    continue

                rect = self.utils.get_rect(window)

                screenshot = self.utils.capture_screenshot(rect)

                self.collect_pumpkin(screenshot, rect)
                self.collect_green(screenshot, rect)
                self.collect_freeze(screenshot, rect)
                
                self.detect_replay(screenshot, rect)

        except (Exception, ExceptionGroup) as error:
            logger.error(get_language("WINDOW_CLOSED").format(error=error))
