import os
import argparse
import asyncio

from core.clicker.blum import BlumClicker
from core.logger.logger import logger
from core.config.config import set_config
from core.localization.localization import get_language

AUTOCLICKER_TEXT = """

██████╗░██╗░░░░░██╗░░░██╗███╗░░░███╗  ░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░░░██║░░░██║████╗░████║  ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
██████╦╝██║░░░░░██║░░░██║██╔████╔██║  ███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██╗██║░░░░░██║░░░██║██║╚██╔╝██║  ██╔══██║██║░░░██║░░░██║░░░██║░░██║
██████╦╝███████╗╚██████╔╝██║░╚═╝░██║  ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═════╝░╚══════╝░╚═════╝░╚═╝░░░░░╚═╝  ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░
"""


    
async def main() -> None:
    """
    The main function of the Blum AutoClicker.

    This function is responsible for initializing the program, clearing the console,
    printing the credits and donation information, and starting the BlumClicker.

    :return: None
    """

    os.system("cls" if os.name == "nt" else "clear")

    print(AUTOCLICKER_TEXT)
    print("\033[34m~ " + get_language("CREDITS") + "\033[0m")
    print("\033[34m~ Telegram: https://t.me/blogbutlazy & https://t.me/chatbutlazy\033[0m")
    print(
        "\033[1;33;48m"
        + get_language("DONATION")
        + "\033[1;37;0m "
        + "UQD2g_C_aIeZ7-zAJ7uOQJUsr538vPcd_GljLeA-iRZL7tzF\n"
    )


    clicker = BlumClicker()
    await clicker.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BAC (Blum Auto Clicker)")

    parser.add_argument(
        "--lang",
        "--setlang",
        type=str,
        help="Set language for the programm (e.g., --lang ua)",
    )
    parser.add_argument(
        "--replays",
        "--max-replays",
        "--tickets",
        type=int,
        help="Set the maximum number of replays (e.g., --replays 50)",
    )
    parser.add_argument(
        "--delay",
        "--replay-delay",
        type=int,
        help="Set the delay between replays in seconds (e.g., --delay 5)",
    )
    args = parser.parse_args()

    config_mapping = {
        "lang": ("LANGUAGE", args.lang),
        "replays": ("REPLAYS", args.replays),
        "delay": ("REPLAY_DELAY", args.delay)
    }

    for arg, (config_key, config_value) in config_mapping.items():
        set_config(config_key, config_value) if config_value else None

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error("Exited due to keyboard interrupt.")

