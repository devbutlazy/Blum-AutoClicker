import os
import argparse
import asyncio

from core.clicker.blum import BlumClicker
from core.config.config import set_language, set_dogs
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
        "--dogs",
        "--dogs-collect",
        type=str,
        help="Set the value for collecting p (e.g., --dogs true/false)",
    )
    args = parser.parse_args()

    if args.lang:
        set_language(args.lang)
    elif args.dogs:
        set_dogs(True if args.dogs.lower() == "true" else False)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        os._exit(0)
