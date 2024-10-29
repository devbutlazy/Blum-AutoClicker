import sys
import pyautogui
import subprocess
import pkg_resources
import pywinctl as pwc

from typing import Tuple, Any
from dataclasses import dataclass

from core.logger.logger import logger


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
                pwc.getWindowsWithTitle(opt)
                for opt in ["TelegramDesktop", "64Gram", "Nekogram", "AyuGram"]
                if pwc.getWindowsWithTitle(opt)
            ),
            None,
        )

        if windows and not windows[0].isActive:
            windows[0].minimize()
            windows[0].restore()

            return windows[0]

        return None

    @staticmethod
    def install_dependencies() -> None:
        with open("requirements.txt") as f:
            requirements = f.read().splitlines()

        installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}

        for requirement in requirements:
            if not requirement or requirement.startswith("#"):
                continue

            package_name = requirement.split("==")[0]  
            try:
                required_version = requirement.split("==")[
                    1
                ]  
            except IndexError:
                required_version = None

            if package_name not in installed_packages:
                logger.info(f"Installing {requirement}, status: not installed")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", requirement]
                )
            elif (
                required_version
                and installed_packages[package_name] != required_version
            ):
                logger.info(
                    f"Installing {requirement}, status: outdated (installed: {installed_packages[package_name]})"
                )
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", requirement]
                )
            else:
                logger.info(
                    f"{package_name} is up to date (version: {installed_packages[package_name]})"
                )
