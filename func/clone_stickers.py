from utils.innit import *
import time

async def sticker_cloner():
    clear()
    logo()
    guild_id = input(f"                {b}[{w}Server You Want to Copy : {b}]{w} >> ")
    clear()
    logo()

    with open('token.txt') as f:
        token = f.readline().strip()

    headers = {
        "Authorization": token,
        "User-Agent": "DiscordBot (https://discord.com, v1)"
    }

    stickers_url = f"https://discord.com/api/v10/guilds/{guild_id}/stickers"
    response = requests.get(stickers_url, headers=headers)

    if response.status_code in [200, 204]:
        data = response.json()
        guild_info_url = f"https://discord.com/api/v10/guilds/{guild_id}"
        guild_info_response = requests.get(guild_info_url, headers=headers)

        if guild_info_response.status_code in [200, 204]:
            guild_name = guild_info_response.json().get("name", "UnknownGuild").replace("/", "_")
            folder_name = f"stickers_{guild_name}"

            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            for sticker in data:
                sticker_id = sticker['id']
                sticker_name = sticker['name'].replace("/", "_")

                if sticker['format_type'] == 4:
                    file_url = f"https://media.discordapp.net/stickers/{sticker_id}.gif?size=240"
                    file_ext = "gif"
                elif sticker['format_type'] == 1:
                    file_url = f"https://media.discordapp.net/stickers/{sticker_id}.webp?size=240&quality=lossless"
                    file_ext = "webp"
                else:
                    continue

                num = random.randint(1, 20000)
                file_path = os.path.join(folder_name, f"{num}.{file_ext}")

                with open(file_path, "wb") as f:
                    sticker_data = requests.get(file_url, headers=headers).content
                    f.write(sticker_data)
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Downloaded: {sticker_name} ({sticker_id})")
        else:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Could Not Create Folder")
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Folder Created")