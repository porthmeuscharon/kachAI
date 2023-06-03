# -*- coding: utf-8 -*-
import requests
import time
import sys
import os
from colorama import init, Fore, Style


# Initialize Colorama
init()

# Light green color code
LIGHT_GREEN = Fore.LIGHTGREEN_EX
NORMAL_YELLOW = Fore.YELLOW
RESET_ALL = Style.RESET_ALL
LIGHT_RED = Fore.LIGHTRED_EX

# ASCII art
ascii_art = r'''
             ,. - .,               .·¨'`;        ,.·´¨;\                   ,.,   '           ,. -  .,                     , ·. ,.-·~·.,   ‘               ,.         ,·´'; '  
        ,·'´ ,. - ,   ';\          ';   ;'\       ';   ;::\                ;´   '· .,        ,' ,. -  .,  `' ·,             /  ·'´,.-·-.,   `,'‚          ;'´*´ ,'\       ,'  ';'\° 
    ,·´  .'´\:::::;'   ;:'\ '       ;   ;::'\      ,'   ;::';             .´  .-,    ';\      '; '·~;:::::'`,   ';\         /  .'´\:::::::'\   '\ °        ;    ';::\      ;  ;::'\ 
   /  ,'´::::'\;:-/   ,' ::;  '     ;  ;::_';,. ,.'   ;:::';°           /   /:\:';   ;:'\'     ;   ,':\::;:´  .·´::\'    ,·'  ,'::::\:;:-·-:';  ';\‚       ;      '\;'      ;  ;:::; 
 ,'   ;':::::;'´ ';   /\::;' '     .'     ,. -·~-·,   ;:::'; '         ,'  ,'::::'\';  ;::';     ;  ·'-·'´,.-·'´:::::::';  ;.   ';:::;´       ,'  ,':'\‚     ,'  ,'`\   \      ;  ;:::; 
 ;   ;:::::;   '\*'´\::\'  °     ';   ;'\::::::::;  '/::::;       ,.-·'  '·~^*'´¨,  ';::;   ;´    ':,´:::::::::::·´'    ';   ;::;       ,'´ .'´\::';‚    ;  ;::;'\  '\    ;  ;:::;  
 ';   ';::::';    '\::'\/.'         ;  ';:;\;::-··;  ;::::;        ':,  ,·:²*´¨¯'`;  ;::';    ';  ,    `·:;:-·'´         ';   ':;:   ,.·´,.·´::::\;'°   ;  ;:::;  '\  '\ ,'  ;:::;'  
  \    '·:;:'_ ,. -·'´.·´\‘       ':,.·´\;'    ;' ,' :::/  '       ,'  / \::::::::';  ;::';    ; ,':\'`:·.,  ` ·.,         \·,   `*´,.·'´::::::;·´     ,' ,'::;'     '\   ¨ ,'\::;'   
   '\:` ·  .,.  -·:´::::::\'       \:::::\    \·.'::::;         ,' ,'::::\·²*'´¨¯':,'\:;     \·-;::\:::::'`:·-.,';        \\:¯::\:::::::;:·´        ;.'\::;        \`*´\::\; °  
     \:::::::\:::::::;:·'´'          \;:·´     \:\::';          \`¨\:::/          \::\'      \::\:;'` ·:;:::::\::\'       `\:::::\;::·'´  °         \:::\'          '\:::\:' '    
       `· :;::\;::-·´                          `·\;'            '\::\;'            '\;'  '     '·-·'       `' · -':::''          ¯                      \:'             `*´'‚      
                                                  '               `¨'                                                        ‘                                                                                                                                                  '         '        
'''



ascii_art2 = r'''
                                       _                
            .-""""-""-.              .' ;               
          .'           `.          .'  /                
         /               `-:     .'   /-.               
        /                  ;_  .'   .'  /               
     .-'    .-"-.("-._      7 / /     .'                
     "-,:  /     "--. ; .-,: / :     ')  ___            
      /  \:        _ `:/  ;;:  ;    .'  /   l           
      L_ ;  / _    6`    // ; :    ';.-'   /            
        \:.: :6         ;" :  ;.--""    _ (             
         `-`.    `     j  _;-"       .-" `.\            
         ..--\    -'  / `"        .-"      "            
.----"""" __  '-.___.'         .-"                      
'...___     "":+"             :                         
   '--..__  .'                ;                         
       '._.'                  K                         
  .-.   .'   .-";              A                        
 /   '-'  .-"   :               C                       
 `-._  .-"       ;               H.                     
    /.'          C       6         "-.                  
    "             H                   "-.               
                   A                     ""--.._.-.     
                    R.        . \l-._              "-._ 
                      O.   _._`;-'   ""---...__        l
                       N      l__.-.           """""""" 
                        \     :     \                   
                         `.      .'  \                  
                           `._.-" `.  ;
'''

# Print ASCII art in light green color
print(LIGHT_GREEN + ascii_art + Style.RESET_ALL)
print(NORMAL_YELLOW + "Type the email here" + RESET_ALL)


# Rest of your code...
from colorama import init, Fore, Style

# Initialize Colorama
init()

# Define color codes
BRIGHT_CYAN = Style.BRIGHT + Fore.CYAN
NORMAL_YELLOW = Fore.YELLOW
LIGHT_GREEN = Fore.LIGHTGREEN_EX
LIGHT_CYAN = Fore.LIGHTCYAN_EX
NORMAL_GREEN = Fore.GREEN
RESET_ALL = Style.RESET_ALL

email = input(": ")

# Print loading text in yellow
print(NORMAL_YELLOW + "kachAI is thinking..." + RESET_ALL)


url = "https://www.duolingo.com/2017-06-30/users?email=" + email

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"})
    if response.status_code == 200:
        data = response.json()
        if len(data["users"]) == 0:
            print(LIGHT_RED + "This email address does not seem to be associated with a Duolingo account." + RESET_ALL)
        else:
            # Wait for 3 second
            time.sleep(3)
            # Clear the console screen
            os.system('cls' if os.name == 'nt' else 'clear')
            user = data["users"][0]
            print(LIGHT_RED + ascii_art + Style.RESET_ALL)



            print(NORMAL_GREEN + "Name:", LIGHT_GREEN + str(user.get("name", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Username:", LIGHT_GREEN + str(user.get("username", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Bio:", LIGHT_GREEN + str(user.get("bio", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Profile Picture:", LIGHT_GREEN + str(user.get("picture", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Learning Language:", LIGHT_GREEN + str(user.get("learningLanguage", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Creation Date:", LIGHT_GREEN + str(user.get("creationDate", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Country:", LIGHT_GREEN + str(user.get("profileCountry", "None")) + RESET_ALL)
            print(BRIGHT_CYAN + "Facebook:", LIGHT_CYAN + str(user.get("hasFacebookId", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Phone Number:", LIGHT_GREEN + str(user.get("hasPhoneNumber", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "XP:", LIGHT_GREEN + str(user.get("totalXp", "None")) + RESET_ALL)
            print(NORMAL_GREEN + "Courses:")
            for course in user.get("courses", []):
                print(NORMAL_GREEN + "  - Title:", LIGHT_GREEN + str(course.get("title", "Unknown")) + RESET_ALL)
                print(NORMAL_GREEN + "    Learning Language:", LIGHT_GREEN + str(course.get("learningLanguage", "Unknown")) + RESET_ALL)
                print(NORMAL_GREEN + "    XP:", LIGHT_GREEN + str(course.get("xp", "Unknown")) + RESET_ALL)
                print(NORMAL_GREEN + "    Crowns:", LIGHT_GREEN + str(course.get("crowns", "Unknown")) + RESET_ALL)
            



                print(LIGHT_RED + ascii_art2 + Style.RESET_ALL)
    else:
        print("An unexpected error occurred while accessing the Duolingo website.")
except requests.exceptions.RequestException as e:
    print("An error occurred while making the HTTP request:", e)
