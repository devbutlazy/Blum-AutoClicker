from lib import BlumClicker
from static import AUTOCLICKER_TEXT, DONATE_TEXT
import asyncio
import os


async def main() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(AUTOCLICKER_TEXT)
    print(DONATE_TEXT)

    clicker = BlumClicker()
    await clicker.run()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting due to keyboard interrupt.")
