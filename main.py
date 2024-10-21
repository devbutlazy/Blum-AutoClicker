import os
import argparse
import asyncio

from core.clicker.blum import BlumClicker
from core.config.config import set_language
from core.localization.localization import get_language
from core.logger.logger import logger


AUTOCLICKER_TEXT = """

██████╗░██╗░░░░░██╗░░░██╗███╗░░░███╗  ░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░░░██║░░░██║████╗░████║  ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
██████╦╝██║░░░░░██║░░░██║██╔████╔██║  ███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██╗██║░░░░░██║░░░██║██║╚██╔╝██║  ██╔══██║██║░░░██║░░░██║░░░██║░░██║
██████╦╝███████╗╚██████╔╝██║░╚═╝░██║  ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═════╝░╚══════╝░╚═════╝░╚═╝░░░░░╚═╝  ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░
"""


async def main() -> None:
    os.system("cls" if os.name == "nt" else "clear")

    print(AUTOCLICKER_TEXT)
    print("\033[34m" + get_language("CREDITS") + "\033[0m")
    print(
        "\033[1;33;48m"
        + get_language("DONATION")
        + "\033[1;37;0m "
        + "UQBTHDZJnuDr4-v6oc_cDRXYdqggIoQA_tLGv5z2li4DC7GI\n"
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
        "--maxreplays",
        type=str,
        help="Set max number of replays for the programm (e.g., --replays 100)",
    )
    parser.add_argument(
        "--max_clicks",
        "--maxclicks",
        type=str,
        help="Set max number of clicks for the programm per game (e.g., --max_clicks 100)",
    )
    args = parser.parse_args()

    if args.lang:
        set_language(args.lang)
    elif args.replays:
        logger.info("Sorry, replays are not supported yet.")
    elif args.max_clicks:
        logger.info("Sorry, max_clicks amount customization is not supported yet.")

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        os._exit(0)
