from utils.innit import *
import time

async def emoji_cloner():
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

    emojis_url = f"https://discord.com/api/v10/guilds/{guild_id}/emojis"
    response = requests.get(emojis_url, headers=headers)

    if response.status_code in [200, 204]:
        data = response.json()
        guild_info_url = f"https://discord.com/api/v10/guilds/{guild_id}"
        guild_info_response = requests.get(guild_info_url, headers=headers)

        if guild_info_response.status_code in [200, 204]:
            guild_name = guild_info_response.json().get("name", "UnknownGuild").replace("/", "_")
            folder_name = f"emojis_{guild_name}"

            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            for emoji in data:
                emoji_id = emoji['id']
                emoji_name = emoji['name'].replace("/", "_")
                is_animated = emoji.get('animated', False)

                file_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.webp?size=56"
                if is_animated:
                    file_url += "&animated=true"
                    file_ext = "webp"
                else:
                    file_ext = "webp"

                num = random.randint(1, 20000)
                file_path = os.path.join(folder_name, f"{num}.{file_ext}")

                with open(file_path, "wb") as f:
                    emoji_data = requests.get(file_url, headers=headers).content
                    f.write(emoji_data)
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Downloaded: {emoji_name} ({emoji_id})")
        else:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Could Not Create Folder")
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Folder Created")