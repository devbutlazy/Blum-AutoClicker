import asyncio
import time
import random
import math
from itertools import product

import keyboard
import mouse
import pyautogui
import pywinctl as pwc

from core.clicker.misc import Utilities, check_share_button
from core.logger.logger import logger
from core.localization.localization import get_language
from core.config.config import get_config_value

from typing import Tuple, Any


class BlumClicker:
    def __init__(self):
        self.utils = Utilities()
        self.window = None

        self.paused: bool = True
        self.replay_limit_logged = False

        self.window_options: str | None = None
        self.replays: int = 0

    async def handle_input(self) -> bool:
        """
        Handles the input for pausing or starting the clicker.

        :return: whether the input was handled
        """
        if keyboard.is_pressed(get_config_value("START_HOTKEY")) and self.paused:
            self.paused = False
            logger.info(get_language("PRESS_P_TO_PAUSE"))
            await asyncio.sleep(0.2)

        elif keyboard.is_pressed(get_config_value("TOGGLE_HOTKEY")):
            self.paused = not self.paused
            logger.info(
                get_language("PROGRAM_PAUSED")
                if self.paused
                else get_language("PROGRAM_RESUMED")
            )
            await asyncio.sleep(0.2)

        return self.paused

    @staticmethod
    @check_share_button
    def collect_green(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found point.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size
        x_ranges = [(0, width // 2), (width // 2, width)]
        y_start, y_end = (
            (0, height) if random.random() < 0.03 else (int(height * 0.25), height)
        )

        points = (
            (x, y)
            for x_start, x_end in x_ranges
            for x, y in product(range(x_start, x_end, 20), range(y_start, y_end, 20))
        )

        for x, y in points:
            r, g, b = screen.getpixel((x, y))

            if (r, g, b) == (196, 247, 94):
                continue

            if (b < 125) and (102 <= r < 220) and (200 <= g < 255):
                screen_x, screen_y = rect[0] + x, rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)

                return True

        return False

    @staticmethod
    @check_share_button
    def collect_purple(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found point.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size
        x_ranges = [(25, width // 2), (width // 2, width - 15)]
        start_y = int(height * 0.1885)  # remove Y area from count pixel clicks

        points = (
            (x, y)
            for x_start, x_end in x_ranges
            for x, y in product(range(x_start, x_end, 10), range(start_y, height, 10))
        )

        for x, y in points:
            r, g, b = screen.getpixel((x, y))

            if (r > 170) and (0 <= g < 20) and (130 <= b < 200):
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)
                return True

        return False

    @staticmethod
    @check_share_button
    def collect_brown(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found point.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size
        x_ranges = [(25, width // 2), (width // 2, width - 15)]
        start_y = int(height * 0.1885)  # remove Y area from count pixel clicks

        points = (
            (x, y)
            for x_start, x_end in x_ranges
            for x, y in product(range(x_start, x_end, 10), range(start_y, height, 10))
        )

        for x, y in points:
            r, g, b = screen.getpixel((x, y))

            if (135 < r < 250) and (50 <= g < 200) and (10 <= b < 150):
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)
                return True

        return False

    @staticmethod
    @check_share_button
    def collect_yellow(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found point.

        :param screen: the screenshot in BGR format
        :param rect: the bounding rectangle of the screen
        :return: whether the item was found
        """
        width, height = screen.size
        x_ranges = [(25, width // 2), (width // 2, width - 15)]
        start_y = int(height * 0.7)  # remove Y area from clicks on replay button

        points = (
            (x, y)
            for x_start, x_end in x_ranges
            for x, y in product(range(x_start, x_end, 10), range(start_y, height, 10))
        )

        for x, y in points:
            r, g, b = screen.getpixel((x, y))

            if (200 <= r <= 255) and (100 <= g <= 200) and (0 <= b <= 100):
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)
                return True

        return False

    @staticmethod
    @check_share_button
    def collect_white(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Detect and click on the dog's face based on its specific color.
        :param screen: the screenshot in BGR format
        :param rect: the bounding rectangle of the screen
        :return: whether the dog was found
        """
        width, height = screen.size
        x_ranges = [(25, width // 2), (width // 2, width - 15)]
        start_y = int(height * 0.7)  # remove Y area from clicks on replay button

        points = (
            (x, y)
            for x_start, x_end in x_ranges
            for x, y in product(
                range(x_start, x_end, 10), range(start_y, int(height * 0.7), 10)
            )
        )
        for x, y in points:
            r, g, b = screen.getpixel((x, y))

            if (r > 220) and (g > 220) and (b > 220):
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)
                return True

        return False

    @staticmethod
    @check_share_button
    def collect_freeze(screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the found freeze.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """
        width, height = screen.size
        x_ranges = [(0, width // 2), (width // 2, width)]

        points = (
            (x, y)
            for x_start, x_end in x_ranges
            for x, y in product(range(x_start, x_end, 10), range(0, height, 10))
        )

        for x, y in points:
            r, g, b = screen.getpixel((x, y))

            if (215 < b < 255) and (100 <= r < 166) and (220 <= g < 254):
                screen_x = rect[0] + x
                screen_y = rect[1] + y
                mouse.move(screen_x, screen_y, absolute=True)
                mouse.click(button=mouse.LEFT)
                return True

        return False

    @staticmethod
    def detect_reload_screen(screen: Any) -> bool:
        """
        Reload app.

        :param screen: the screenshot
        :return: whether the reload screen found
        """
        width, height = screen.size

        x1, y1 = (math.ceil(width * 0.43781), math.ceil(height * 0.60252))
        x2, y2 = (math.ceil(width * 0.24626), math.ceil(height * 0.429775))

        reload_button = screen.getpixel((x1, y1))
        white_pixel = screen.getpixel((x2, y2))

        if reload_button == (40, 40, 40) and white_pixel == (255, 255, 255):
            time.sleep(0.5)
            keyboard.press_and_release("F5")
            return True

        return False

    def close_extra_windows(self):
        """
        Close Telegram app.

        :return: None
        """
        window = pwc.getActiveWindow()
        if window.title != self.window.title and not window.title in ["Terminal", "Powershell", "cmd"]: 
            window.hide()
            logger.error(f"Unwanted window hidden ({window.title})")

    @staticmethod
    def reload_overrides() -> None:
        """
        Reload app with window focus handling.

        :return: None
        """
        try:
            if not pwc.getActiveWindow():
                raise Exception("No active window found to reload")

            keyboard.press_and_release("f12")
            time.sleep(2)

            devtools_window = next(
                (
                    window
                    for window in pwc.getAllWindows()
                    if "DevTools" in window.title
                ),
                None,
            )
            if not devtools_window:
                raise Exception(
                    "Telegram Inspect WebView window not found. Try enabling Web Inspecting in experimental features."
                )
            devtools_window.activate()

            keyboard.press_and_release("ctrl+f5")
            time.sleep(5)

            keyboard.press_and_release("alt+f4")

            pwc.getActiveWindow().activate()
            logger.debug("Refreshed the game for better performance")
        except BaseException as error:
            logger.error(f"Error during reload: {error}")

    def detect_replay(self, screen: Any, rect: Tuple[int, int, int, int]) -> bool:
        """
        Click on the 'Play (nn left)' button.

        :param screen: the screenshot
        :param rect: the rectangle
        :return: whether the image was found
        """

        max_replays = get_config_value("REPLAYS")
        replay_delay = get_config_value("REPLAY_DELAY")

        left_check_x, left_check_y = (
            rect[0] + int(screen.size[0] * 0.142),
            rect[1] + int(screen.size[1] * 0.86),
        )
        right_check_x, right_check_y = (
            rect[0] + int(screen.size[0] * 0.794),
            rect[1] + int(screen.size[1] * 0.85),
        )
        left_pixel = pyautogui.pixel(left_check_x, left_check_y)
        right_pixel = pyautogui.pixel(right_check_x, right_check_y)

        if left_pixel != (255, 255, 255) or right_pixel != (255, 255, 255):
            return False

        if self.replays >= max_replays:
            return (
                logger.error(
                    get_language("REPLAY_LIMIT_REACHED").format(replays=max_replays)
                )
                if not self.replay_limit_logged
                else None
            )

        delay = random.randint(replay_delay, replay_delay + 3) + random.random()
        logger.debug(
            f"Detected the replay button. Remaining replays: {max_replays - self.replays} // Delay: {delay:.2f}"
        )

        self.close_extra_windows()
        time.sleep(delay)

        if (
            self.replays != 0
            and self.replays % get_config_value("GAMES_BETWEEN_REFRESH") == 0
        ):
            self.reload_overrides()

        mouse.move(
            left_check_x + random.randint(1, 10),
            right_check_y,
            absolute=True,
        )
        mouse.click(button=mouse.LEFT)

        time.sleep(1)
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
                
                self.window = window
                self.close_extra_windows()
                
                rect = self.utils.get_rect(window)

                screenshot = self.utils.capture_screenshot(rect)

                self.collect_green(screenshot, rect)
                self.collect_purple(screenshot, rect)
                self.collect_brown(screenshot, rect)
                self.collect_white(screenshot, rect)
                self.collect_yellow(screenshot, rect)
                # self.collect_freeze(screenshot, rect)

                self.detect_replay(screenshot, rect)
                self.detect_reload_screen(screenshot)

        except (Exception, ExceptionGroup) as error:
            logger.error(get_language("WINDOW_CLOSED").format(error=error))
