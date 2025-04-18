from utils.innit import *

async def token_checker():
    clear()
    logo()

    valid = 0
    invalid = 0

    with open('token.txt')as f:
        token = f.readline().strip()
    
    headers = {
        "Authorization": token
    }

    url = "https://discord.com/api/v9/users/@me"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        valid += 1
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Token Valid")
    else:
        t = current_time()
        invalid += 1
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Token Invalid")
    
    final = f"""
                {b}[{w}{valid}{b}]{w} {g}Valid{w}
                {b}[{w}{invalid}{b}]{w} {r}Invalid{w}
                """
    clear()
    logo()
    print(final)
    input(f"                {b}[{w}#{b}]{w} Press ENTER to Return.")