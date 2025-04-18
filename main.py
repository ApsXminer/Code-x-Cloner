from utils.innit import *
from func.cloner import *
from func.clone_stickers import *
from func.clone_emojis import *
from func.guild_info import *
from func.token_checker import *

async def menu():
    while True:
        clear()
        logo()
        o = f"""
                {b}[{w}01{b}]{w} Server Copy              {b}[{w}04{b}]{w} Server Status
                {b}[{w}02{b}]{w} Server Sticker Copy      {b}[{w}05{b}]{w} Token Checker
                {b}[{w}03{b}]{w} Server Emoji Copy """
        print(o)
        cs = input(f"                {b}[{w}Code X Cloner{b}]{w} >> ")

        if cs == "1":
            await cloner()
        elif cs == "2":
            await sticker_cloner()
        elif cs == "3":
            await emoji_cloner()
        elif cs == "4":
            await guild_info()
        elif cs == "5":
            await token_checker()


if __name__ == "__main__":
    asyncio.run(menu())