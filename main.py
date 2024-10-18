import os
import argparse
import asyncio

from core.clicker.blum import BlumClicker
from core.config.config import set_language
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
    parser = argparse.ArgumentParser(description="Blum Clicker Program")
    parser.add_argument(
        "--lang",
        "--setlang",
        type=str,
        help="Set language for the programm (e.g., --lang ua)",
    )
    args = parser.parse_args()

    if args.lang:
        set_language(args.lang)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        os._exit(0)
