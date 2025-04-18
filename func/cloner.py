from utils.innit import *                                                                                                                                                                         # MADE BY CODE X
import time

async def cloner():
    clear()
    logo()
    g_id = input(f"                {b}[{w}Provide Server ID You Want To Copy : {b}]{w} >> ")
    p_id = input(f"                {b}[{w}Provide Server ID You Want To Replicate : {b}]{w} >> ")
    clear()
    logo()
                                                                                                                                                                                                                # MADE BY CODE X
    with open('token.txt') as f:
        token = f.readline().strip()

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    channel_url = f"https://discord.com/api/v9/guilds/{p_id}/channels"
    response = requests.get(channel_url, headers=headers)
                                                                                                                                                                                                    # MADE BY CODE X
    if response.status_code == 200:
        channels = response.json() 
        for channel in channels:
            delete_channel_url = f"https://discord.com/api/v9/channels/{channel['id']}"
            delete_channel = requests.delete(delete_channel_url, headers=headers)
            if delete_channel.status_code in [200, 204]:  
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Deleted channel: {channel['name']}")
                                                                                                                                                                                                            # MADE BY CODE X
            else:
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Delete Channel {channel['name']}: {delete_channel.status_code}")
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Fetch Channels: {response.status_code}")

    role_url = f"https://discord.com/api/v9/guilds/{p_id}/roles"
    response = requests.get(role_url, headers=headers)
                                                                                                                                                                                                                    # MADE BY CODE X
    if response.status_code == 200:
        roles = response.json()
        for role in roles:
            delete_role_url = f"https://discord.com/api/v9/guilds/{p_id}/roles/{role['id']}"
            while True:  
                delete_response = requests.delete(delete_role_url, headers=headers)
                if delete_response.status_code in [200, 204]:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Deleted Role: {role['name']}")
                    break
                elif delete_response.status_code == 429:
                    retry_after = int(delete_response.headers.get("Retry-After", 1))
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Rate Limit : {retry_after} Second")
                    time.sleep(retry_after)
                elif delete_response.status_code == 400:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Named Role: {role['name']} (Probably @everyone)")
                    break
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Delete Role: {role['name']} = {delete_response.status_code}")
                    break
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Roles Couldn't Be Provided: {response.status_code}")

    guild_url = f"https://discord.com/api/v9/guilds/{g_id}"
    response = requests.get(guild_url, headers=headers)

    if response.status_code == 200:
        guild = response.json()
        guild_name_url = f"https://discord.com/api/v9/guilds/{p_id}"
        if guild['icon']:
            icon_url = f"https://cdn.discordapp.com/icons/{g_id}/{guild['icon']}.png"
            icon_response = requests.get(icon_url)

            if icon_response.status_code == 200:
                icon_base64 = base64.b64encode(icon_response.content).decode('utf-8')
                icon_data = f"data:image/png;base64,{icon_base64}"
            else:
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Failed to fetch server icon. Continuing without icon.")
                icon_data = None
        else:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} The server has no icon. Continuing without the icon.")
            icon_data = None

        payload = {
            "name": guild['name']
        }
        if icon_data:
            payload["icon"] = icon_data

        change_name = requests.patch(guild_name_url, headers=headers, json=payload)
        if change_name.status_code == 200:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Server Name Changed to: {guild['name']}")
            if icon_data:
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Server Icon Updated.")
        else:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Change Server Name/Icon: {change_name.status_code}")
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Retrieve Server Details: {response.status_code}")

    get_channels_url = f"https://discord.com/api/v9/guilds/{g_id}/channels"
    response = requests.get(get_channels_url, headers=headers)

    if response.status_code == 200:
        source_channels = response.json()
        
        categories = [ch for ch in source_channels if ch['type'] == 4]
        channels = [ch for ch in source_channels if ch['type'] != 4]

        categories.sort(key=lambda x: x['position'])
        channels.sort(key=lambda x: x['position'])

        created_categories = {}
        for category in categories:
            payload = {
                "name": category['name'],
                "type": 4,  
                "permission_overwrites": category['permission_overwrites']
            }
            create_category_url = f"https://discord.com/api/v9/guilds/{p_id}/channels"
            while True:
                create_response = requests.post(create_category_url, headers=headers, json=payload)
                if create_response.status_code == 201:
                    created_category = create_response.json()
                    created_categories[category['id']] = created_category['id']  
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Category Created: {category['name']}")
                    break
                elif create_response.status_code == 429:
                    retry_after = int(create_response.headers.get("Retry-After", 1))
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Rate ​​Limit. {retry_after} Second")
                    time.sleep(retry_after)
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Category Could Not Be Created: {category['name']} = {create_response.status_code}")
                    break

        for channel in channels:
            payload = {
                "name": channel['name'],
                "type": channel['type'],
                "parent_id": created_categories.get(channel['parent_id']),  
                "permission_overwrites": channel['permission_overwrites'],
                "topic": channel.get('topic', ''),
                "nsfw": channel.get('nsfw', False),
                "rate_limit_per_user": channel.get('rate_limit_per_user', 0),
            }
            create_channel_url = f"https://discord.com/api/v9/guilds/{p_id}/channels"
            while True:
                create_response = requests.post(create_channel_url, headers=headers, json=payload)
                if create_response.status_code == 201:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Created Channel: {channel['name']}")
                    break
                elif create_response.status_code == 429:
                    retry_after = int(create_response.headers.get("Retry-After", 1))
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Rate Limit {retry_after} Second")
                    time.sleep(retry_after)
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Channel Could Not Be Created: {channel['name']} = {create_response.status_code}")
                    break
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Fetch Channels from Source Server: {response.status_code}")

    get_roles_url = f"https://discord.com/api/v9/guilds/{g_id}/roles"
    response = requests.get(get_roles_url, headers=headers)

    if response.status_code == 200:
        source_roles = response.json()
        source_roles.sort(key=lambda x: x['position'], reverse=True)                                                                                                                                                            # MADE BY CODE X

        for role in source_roles:
            payload = {
                "name": role['name'],
                "permissions": role['permissions'],
                "color": role['color'],
                "hoist": role['hoist'],
                "mentionable": role['mentionable']                                                                                                                                                          # MADE BY CODE X
            }
            create_role_url = f"https://discord.com/api/v9/guilds/{p_id}/roles"
            while True:
                create_response = requests.post(create_role_url, headers=headers, json=payload)
                if create_response.status_code in [201, 200]:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Created Role: {role['name']}")
                    break
                elif create_response.status_code == 429:
                    retry_after = int(create_response.headers.get("Retry-After", 1))
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Rate ​​Limit {retry_after} Second")                                                                                             # MADE BY CODE X
                    time.sleep(retry_after)
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Create Role: {role['name']} {create_response.status_code}")
                    break                                                                                                                                                                                                                                       # MADE BY CODE X
            time.sleep(2)
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to Get Roles from Source Server: {response.status_code}")                                                                                                                            # MADE BY CODE X