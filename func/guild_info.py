from utils.innit import *

async def guild_info():
    clear()
    logo()
    guild_id = input(f"                {b}[{w}SERVER ID : {b}]{w} >> ")
    clear()
    logo()
    
    with open('token.txt') as f:
        token = f.readline().strip()
    
    headers = {
        "Authorization": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    guild_url = f"https://discord.com/api/v10/guilds/{guild_id}"
    response = requests.get(guild_url, headers=headers)
    
    if response.status_code == 200:
        guild = response.json()
        
        guild_name = guild['name']
        guild_icon = guild.get('icon')
        guild_owner_id = guild['owner_id']
        guild_region = guild.get('region', 'N/A')
        guild_afk_channel_id = guild.get('afk_channel_id', 'None')
        guild_afk_timeout = guild.get('afk_timeout', 'None')
        guild_verification_level = guild['verification_level']
        guild_max_members = guild['max_members']
        guild_premium_tier = guild['premium_tier']
        guild_description = guild.get('description', 'No Description')
        guild_banner = guild.get('banner')
        guild_features = guild['features']
        
        guild_icon_url = (
            f"https://cdn.discordapp.com/icons/{guild_id}/{guild_icon}.png" 
            if guild_icon 
            else "No Icon"
        )

        guild_banner_url = (
            f"https://cdn.discordapp.com/banners/{guild_id}/{guild_banner}.png?size=512" 
            if guild_banner 
            else "No Banner"
        )
        t = current_time()
        print(f"\n                {b}[{w}{t}{b}]{w} {g}[+]{w} Server Information:")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Server Name: {guild_name}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Server Icon: {guild_icon_url}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Server Owner ID: {guild_owner_id}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Area: {guild_region}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} AFK Channel ID: {guild_afk_channel_id}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} AFK Timeout: {guild_afk_timeout}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Verification Level: {guild_verification_level}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Maximum Members: {guild_max_members}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Boost Tier: {guild_premium_tier}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Guild Description: {guild_description}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Banner: {guild_banner_url}")
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Features: {', '.join(guild_features)}")
        input(f"                {b}[{w}#{b}]{w} Press ENTER to Return.")
    else:
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Server information could not be retrieved: {response.status_code} - {response.text}")
    time.sleep(2)