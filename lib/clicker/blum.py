import asyncio
from itertools import product
import random

import keyboard
import pygetwindow as gw
from pynput.mouse import Button, Controller

from typing import Tuple, Any
from lib.utils import Utilities
from lib.logger import logger
from static import WINDOW_NOT_FOUND


class BlumClicker:
    def __init__(self):
        self.mouse: Controller = Controller()
        self.utils = Utilities()

        self.paused: bool = True
        self.window: str = None

    async def click(self, x: int, y: int) -> None:
        """
        Click the mouse.

        :param x: the x coordinate
        :param y: the y coordinate
        :return: None
        """
        self.mouse.position = (x, y + random.randint(1, 3))
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)

    async def handle_input(self) -> bool:
        """
        Handles the input.

        :return: whether the input was handled
        """

        if keyboard.is_pressed("s") and self.paused:
            self.paused = False
            logger.info("Started 5 threads.")
            logger.info("Press 'p' for pausing the program.")
            await asyncio.sleep(0.2)

        elif keyboard.is_pressed("p"):
            self.paused = not self.paused
            logger.info("Paused. To resume press 'p'" if self.paused else "Resumed. To pause press 'p'")
            await asyncio.sleep(0.2)

        return self.paused

    def activate_window(self, window: Any) -> None:
        """
        Activate the window.

        :param window: the window
        :return: None
        """
        if not window:
            return

        try:
            window.activate()
        except (Exception, ExceptionGroup):
            window.minimize()
            window.restore()

    async def click_on_found(
        self, screen: Any, rect: Tuple[int, int, int, int]
    ) -> bool:
        """
        Click on the found image.

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
                await self.click(screen_x + 4, screen_y)
                return True

        return False

    async def click_on_play_button(self, screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the 'Play (nn left)' button if found.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the button was found and clicked
        """
        width, height = screen.size

        for x, y in product(range(0, width, 20), range(0, height, 20)):
            r, g, b = screen.getpixel((x, y))

            if (r, g, b) == (255, 255, 255):  # Assuming the button has white text
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                await self.click(screen_x, screen_y)
                return True

        return False
    
    

    async def run(self) -> None:
        """
        Runs the clicker.
        :return:
        """

        self.window = "TelegramDesktop"
        window = gw.getWindowsWithTitle(self.window)

        if not window:
            logger.error(WINDOW_NOT_FOUND)
            return

        logger.info("Initialized blum-clicker!")
        logger.info(f"Found {self.window}")
        logger.info("Press 's' to start the program.")

        while True:
            if await self.handle_input():
                continue

            rect = self.utils.get_rect(window[0])
            self.activate_window(window[0])

            screenshot = self.utils.capture_screenshot(rect)

            tasks = []
            for _ in range(10):
                tasks.append(self.click_on_found(screenshot, rect))

            await asyncio.gather(*tasks)
            await self.click_on_play_button(screenshot, rect)
