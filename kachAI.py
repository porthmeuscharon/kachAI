import requests
import urllib.parse
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define the social media platforms dictionary
social_media_platforms = {
    "Twitter": {
        "url": "https://nitter.it/{}",
        "username_claimed": ""
    },
    "Instagram": {
        "url": "https://www.instagram.com/{}",
        "username_claimed": ""
    },
    "Facebook": {
        "url": "https://www.facebook.com/{}",
        "username_claimed": ""
    },
    "Roblox": {
        "url": "https://www.roblox.com/user.aspx?username={}",
        "username_claimed": ""
    },
    "rblx.trade": {
        "url": "https://rblx.trade/p/{}",
        "username_claimed": ""
    },
    "YouTube": {
        "url": "https://www.youtube.com/@{}",
        "username_claimed": ""
    },
    "Twitch": {
        "url": "https://www.twitch.tv/{}",
        "username_claimed": ""
    },
    "Snapchat": {
        "url": "https://www.snapchat.com/add/{}",
        "username_claimed": ""
    },
    "Snapchat Stories": {
        "url": "https://story.snapchat.com/s/{}",
        "username_claimed": ""
    },
    "Telegram": {
        "url": "https://t.me/{}",
        "username_claimed": ""
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "username_claimed": ""
    },
    "Doxbin": {
        "url": "https://doxbin.com/user/{}",
        "username_claimed": ""
    }
}

# Create a function to check if a username is available on a social media platform
def check_username(website: str, username: str) -> bool:
    url = website.format(urllib.parse.quote(username))
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False

# ASCII art for "hello"
ascii_art = f"{Fore.LIGHTCYAN_EX}" + r"""
             ,. - .,               .·¨'`;        ,.·´¨;\                   ,.,   '           ,. -  .,                     , ·. ,.-·~·.,   ‘               ,.         ,·´'; '  
        ,·'´ ,. - ,   ';\          ';   ;'\       ';   ;::\                ;´   '· .,        ,' ,. -  .,  `' ·,             /  ·'´,.-·-.,   `,'‚          ;'´*´ ,'\       ,'  ';'\° 
    ,·´  .'´\:::::;'   ;:'\ '       ;   ;::'\      ,'   ;::';             .´  .-,    ';\      '; '·~;:::::'`,   ';\         /  .'´\:::::::'\   '\ °        ;    ';::\      ;  ;::'\ 
   /  ,'´::::'\;:-/   ,' ::;  '     ;  ;::_';,. ,.'   ;:::';°           /   /:\:';   ;:'\'     ;   ,':\::;:´  .·´::\'    ,·'  ,'::::\:;:-·-:';  ';\‚       ;      '\;'      ;  ;:::; 
 ,'   ;':::::;'´ ';   /\::;' '     .'     ,. -·~-·,   ;:::'; '         ,'  ,'::::'\';  ;::';     ;  ·'-·'´,.-·'´:::::::';  ;.   ';:::;´       ,'  ,':'\‚     ,'  ,'`\   \      ;  ;:::;  
 ;   ;:::::;   '\*'´\::\'  °     ';   ;'\::::::::;  '/::::;       ,.-·'  '·~^*'´¨,  ';::;   ;´    ':,´:::::::::::·´'    ';   ;::;       ,'´ .'´\::';‚    ;  ;::;'\  '\    ;  ;:::;  
 ';   ';::::';    '\::'\/.'         ;  ';:;\;::-··;  ;::::;        ':,  ,·:²*´¨¯'`;  ;::';    ';  ,    `·:;:-·'´         ';   ':;:   ,.·´,.·´::::\;'°   ;  ;:::;  '\  '\ ,'  ;:::;'  
  \    '·:;:'_ ,. -·'´::::::\'       \:::::\    \·.'::::;         ,' ,'::::\·²*'´¨¯':,'\:;     \·-;::\:::::'`:·-.,';        \\:¯::\:::::::;:·´        ;.'\::;        \`*´\::\; °  
   '\:` ·  .,.  -·:´::::::\'       \:::::\    \·.'::::;         ,' ,'::::\·²*'´¨¯':,'\:;     \·-;::\:::::'`:·-.,';        \\:¯::\:::::::;:·´        ;.'\::;        \`*´\::\; °  
     \:::::::\:::::::;:·'´'          \;:·´     \:\::';          \`¨\:::/          \::\'      \::\:;'` ·:;:::::\::\'       `\:::::\;:::´  °         \:::\'          '\:::\:' '    
       `· :;::\;::-·´                          `·\;'            '\::\;'            '\;'  '     '·-·'       `' · -':::''          ¯                      \:'             `*´'‚      
                                                  '               `¨'                                                        ‘                                                
""" + f"{Style.RESET_ALL}"

print(ascii_art)

# Get the usernames from the user
print(f"{Fore.LIGHTBLUE_EX}Type usernames here (space them out){Style.RESET_ALL} ")
code = input(":")

# Find the usernames in the code
usernames = code.split()

# Print the usernames
print(f"\n{Fore.RED}Korror himself is searching up usernames:{Style.RESET_ALL}")
for username in usernames:
    print(username)

# Check if the usernames are available on the social media platforms
for username in usernames:
    for platform, data in social_media_platforms.items():
        # Get the URL for the username on the platform
        url = data["url"].format(username)

        # Check if the username is available on the platform
        if check_username(url, username):
            print(f"\n{Fore.LIGHTCYAN_EX}{username} is available on {platform}")
            print(f"Profile URL: {Fore.MAGENTA}{url}{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.LIGHTRED_EX}{username} is not available on {platform}{Style.RESET_ALL}")
            
