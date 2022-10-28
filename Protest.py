# Created by @Sepy_Movasat | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" #
# Please note: Although that this is for testing purposes, It may cause file loss(if used without care)#
# JUST FOR WINDOWS #

import colorama as cm #Used for creating some sort of UI
import subprocess #Used for executing files a lot
import sys #Used like subprocess
import time #Used for time.sleep
import os #Used in different parts of the program 
import ctypes #Used in is_admin()
from alive_progress import * #Used for creating a nice, cool progress bar ;)
import random #Used for random selecting a logo
    
def is_admin():
    #Some parts of the program need admin privileges to work properly
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin


def cls():
    #Clear the screen!
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

#In a good UI, anything has it's own style :)
def Great_Style():
    print(cm.Fore.CYAN +"[" + cm.Fore.GREEN + "+" + cm.Fore.CYAN + "] " + cm.Fore.RESET, end="")


def Error_Style():
    print(cm.Fore.YELLOW +"[" + cm.Fore.RED + "!" + cm.Fore.YELLOW + "] " + cm.Fore.RESET, end="")


def Info_Style():
    print(cm.Fore.CYAN +"[" + cm.Fore.BLUE + "i" + cm.Fore.CYAN + "] " + cm.Fore.RESET, end="")


def Warning_Style():
    print(cm.Fore.RED +"[" + cm.Fore.YELLOW + "!" + cm.Fore.RED + "] " + cm.Fore.RESET, end="")


def No_Worry_Style():
    print(cm.Fore.CYAN +"[" + cm.Fore.GREEN + "OK" + cm.Fore.CYAN + "] " + cm.Fore.RESET, end="")


def Ask_Style():
    print(cm.Fore.RESET +"[" + cm.Fore.BLUE + "???" + cm.Fore.RESET + "] ", end="")


def tell_the_danger():
    # Here we try to encrypt all data in the documents folder | SO TAKE CARE #
    Info_Style()
    print("In this part we test your anti-virus's ransomware protection")
    Info_Style()
    print("For doing that, we try to encrypt all data in the documents folder")
    Great_Style()
    print("For being safe from this, copy your files in any other folder(but the folder must have at least a file in it)!")
    Warning_Style()
    CARE = input("Do you accept the potential"+cm.Fore.RED + " danger"+cm.Fore.RESET +" ["+cm.Fore.CYAN + "Y"+cm.Fore.RESET + "/" + cm.Fore.YELLOW + "n"+cm.Fore.RESET + "] ")
    if CARE == "Y" or CARE == "y":
        cls()
        Info_Style()
        print("This test has six modes [easy mode, normal mode, hard mode, super hard mode, super super hard mode, ultra hard mode]")
        print(""+cm.Fore.LIGHTGREEN_EX + "Easy mode:"+ cm.Fore.RESET+" A simple exe file that tries to encrypt ur files(easy to detect both using signatures and behavioral protection)")
        print(""+cm.Fore.GREEN + "Normal mode:"+ cm.Fore.RESET +" An exe file that is packed by upx and tries to encrypt ur files(harder to detect using signatures)")
        print(cm.Fore.YELLOW + "Hard mode:" + cm.Fore.RESET + " An exe filed that is packed by upx but more than usual (upx --ultra-brute) - (even harder to detect using signatures)")
        print(cm.Fore.LIGHTYELLOW_EX + "Super hard mode:" + cm.Fore.RESET + " An exe file that is protected by VMProtect (Super hard to detect both by signatures and behavioral protection)")
        print(cm.Fore.RED + "Super super hard mode:" + cm.Fore.RESET + " An exe file that is protected by enigma protector (Super super hard to detect by any protection system - It is so unique)")
        print(cm.Fore.LIGHTRED_EX + "Ultra hard mode:"+ cm.Fore.RESET+ " A python file that tries to encrypt ur files(almost impossible to detect by signatures - just behavioral protection)")
        mode = input("Please choose the mode you want to use ["+cm.Fore.LIGHTGREEN_EX + "E"+cm.Fore.RESET +"/" + cm.Fore.GREEN + "N"+cm.Fore.RESET+"/" +cm.Fore.YELLOW + "H" + cm.Fore.RESET + "/" + cm.Fore.LIGHTYELLOW_EX + "SH" + cm.Fore.RESET + "/" + cm.Fore.RED  + "SSH" + cm.Fore.RESET + "/" + cm.Fore.LIGHTRED_EX + "UH" + cm.Fore.RESET + "] ")
        if mode == "E" or mode == "e":
            Ransom("E")
        elif mode == "N" or mode == "n":
            Ransom("N")
        elif mode == "H" or mode == "h":
            Ransom("H")
        elif mode == "SH" or mode == "sh" or mode == "Sh" or mode == "sH":
            Ransom("SH")
        elif mode == "SSH" or mode == "ssh" or mode == "Ssh" or mode == "SSh" or mode == "sSH" or mode == "sSh" or mode == "SsH":
            Ransom("SSH")
        elif mode == "UH" or mode == "uh" or mode == "Uh" or mode == "uH":
            Ransom("UH")
        else:
            cls()
            print(cm.Fore.RED + """
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░█████╗░░█████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚═╝███╔╝╚═╝███╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░░░╚══╝░░░░╚══╝░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░░░░██╗░░░░░██╗░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░
""")
            Error_Style()
            print("Error: Wrong mode selected!")
            Great_Style()
            print("Please try again!")
            Info_Style()
            print("Going back to main menu in 5 seconds...")
            time.sleep(5)
            main_menu()
    else:
        No_Worry_Style()
        print("No need to worry, going back to the main menu...")
        time.sleep(5)
        main_menu()


def Ransom(mode):
    # Here we try to encrypt all data in the documents folder | SO TAKE CARE #
    try:
        if mode == "E":
            file = "Encrypt.exe"
        elif mode == "N":
            file ="Encrypt-upx.exe"
        elif mode == "H":
            file="Encrypt-hard-upx.exe"
        elif mode == "SH":
            file="Encrypt-vmp.exe"
        elif mode == "SSH":
            file="Encrypt-enigma.exe"
        else:
            file = "Encrypt.py"
        usr = os.getlogin()
        cls()
        print(cm.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀ 
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
    """)
        Info_Style()
        print("Starting the ransomware test...")
        time.sleep(5)
        try:
            finalf = "The-Bad-Guys\\"+file 
            if mode == "UH":
                letssee = subprocess.call(["python",finalf])
                time.sleep(1.5)
            else:
                letssee = subprocess.call([finalf])
                time.sleep(1.5)
        except FileNotFoundError:
            Warning_Style()
            print("The ransomware file was not found!")
            Great_Style()
            print("This maybe caused by your anti-virus software")
            Info_Style()
            print("If that's true, your anti-virus has done great(probably with signatures)!")
            Info_Style()
            print("Going back to the main menu in 12 seconds...")
            time.sleep(12)
            main_menu()
        if letssee == 1 or letssee == 2:
            cls()
            print(cm.Fore.MAGENTA + """
██╗░░░██╗███████╗░█████╗░██╗
██║░░░██║██╔════╝██╔══██╗██║
██║░░░██║█████╗░░██║░░██║██║
██║░░░██║██╔══╝░░██║░░██║╚═╝
╚██████╔╝██║░░░░░╚█████╔╝██╗
░╚═════╝░╚═╝░░░░░░╚════╝░╚═╝
        """)
            Great_Style()
            print("Ransomware was unable to load in memory!")
            Ask_Style()
            print("Hmmm... Has your anti-virus cheated?")
            Great_Style()
            print("If not, you have a great anti-virus!")
            Info_Style()
            print("Maybe a UFO Anti-virus?!")
            Info_Style()
            print("Going back to the main menu in 15 seconds...")
            time.sleep(15)
            main_menu()
        else:
            time.sleep(10)
            for r, d, files in os.walk("C:\\Users\\"+usr+"\\Documents"):
                for file in files:
                    lfile = os.path.join(r, file)
                    if not "desktop.ini" in lfile:
                        if lfile.endswith(".WOW"):
                            cls()
                            print(cm.Fore.RED + """
░█████╗░██╗░░░██╗░█████╗░██╗░░██╗██╗
██╔══██╗██║░░░██║██╔══██╗██║░░██║██║
██║░░██║██║░░░██║██║░░╚═╝███████║██║
██║░░██║██║░░░██║██║░░██╗██╔══██║╚═╝
╚█████╔╝╚██████╔╝╚█████╔╝██║░░██║██╗
░╚════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝
                        """)
                            Error_Style()
                            print("Ransomware was able to encrypt your files")
                            Info_Style()
                            print("Your anti-virus may do good with signatures")
                            Warning_Style()
                            print("But don't trust it's protection for zero-day malware/ransomware")
                            Info_Style()
                            print("Test Completed!")
                            Info_Style()
                            print("Going back to the main menu in 15 seconds...")
                            time.sleep(15)
                            main_menu()
                        else:
                            cls()
                            print(cm.Fore.GREEN + """
░██████╗░██████╗░███████╗░█████╗░████████╗██╗
██╔════╝░██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║
██║░░██╗░██████╔╝█████╗░░███████║░░░██║░░░██║
██║░░╚██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░╚═╝
╚██████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██╗
░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝
                    """)
                            Info_Style()
                            print("Although the ransomware was able to load in memory, encryption was blocked")
                            Great_Style()
                            print("And that's good!")
                            Info_Style()
                            print("So, you can almost trust your anti-virus zero-day protection")
                            Great_Style()
                            print("Test Completed!")
                            Info_Style()
                            print("Going back to the main menu in 15 seconds...")
                            time.sleep(15)
                            main_menu()
    except PermissionError:
            Warning_Style()
            print("The ransomware file can not execute!")
            Great_Style()
            print("This maybe caused by your anti-virus")
            Info_Style()
            print("If that's true, your anti-virus has done great(probably with signatures)!")
            Info_Style()
            print("Going back to the main menu in 12 seconds...")
            time.sleep(12)
            main_menu()


def BrokenWall(mode):
    # Here we test your firewall's protection | This part is not dangerous | Cause we roll back all the changes #
    try:
        if mode == "E":
            file1 = "BrokenWall.exe"
            file2 = "BadExclusion.exe"
        elif mode == "N":
            file1 = "BrokenWall-upx.exe"
            file2 = "BadExclusion-upx.exe"
        elif mode == "H":
            file1="BrokenWall-hard-upx.exe"
            file2="BadExclusion-hard-upx.exe"
        elif mode == "SH":
            file1="BrokenWall-vmp.exe"
            file1="BadExclusion-vmp.exe"
        elif mode == "SSH":
            file1="BrokenWall-themida.exe"
            file2="BadExclusion-themida.exe"
        else:
            file1 = "BrokenWall.bat"
            file2 = "BadExclusion.bat"
        cls()
        print(cm.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
    """)
        Info_Style()
        print("Stating the test...")
        Info_Style()
        print("Trying to disable your firewall...")
        time.sleep(7)
        proc = subprocess.Popen(["The-Bad-Guys\\"+file1], stdout=subprocess.PIPE, shell=True)
        (res, err) = proc.communicate()
        proc = err
        if proc == 1 or proc == 2:
            Great_Style()
            print("Your Anti-virus or firewall didn't allow us to turn the firewall off!")
            Info_Style()
            print("Until now it was great!")
            Info_Style()
            print("Now trying to add an exclusion to your firewall...")
            time.sleep(7)
            proc = subprocess.Popen(["The-Bad-Guys\\"+file2], stdout=subprocess.PIPE, shell=True)
            (res, err) = proc.communicate()
            proc = err
            if proc == 1 or proc == 2:
                cls()
                print(cm.Fore.MAGENTA + """
██╗░░░██╗███████╗░█████╗░██╗
██║░░░██║██╔════╝██╔══██╗██║
██║░░░██║█████╗░░██║░░██║██║
██║░░░██║██╔══╝░░██║░░██║╚═╝
╚██████╔╝██║░░░░░╚█████╔╝██╗
░╚═════╝░╚═╝░░░░░░╚════╝░╚═╝
""")
                Great_Style()
                print("Your anti-virus or firewall blocked us from adding the exclusions to your firewall!")
                Great_Style()
                print("Also, it blocked us from turning the firewall off!")
                Info_Style()
                print("Don't worry about any kind of backdoor and attacker at all!")
                Info_Style()
                print("Going back to main menu in 15 seconds...")
                time.sleep(15)
                main_menu()
            else:
                cls()
                print(cm.Fore.GREEN + """
░██████╗░░█████╗░░█████╗░██████╗░██╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║
██║░░██╗░██║░░██║██║░░██║██║░░██║██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║╚═╝
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═╝
""")
                Great_Style()
                print("Your firewall/Anti-Virus blocked us from turning it off!")
                Warning_Style()
                print("By the way, the exclusion seems to be added to your firewall!")
                Info_Style()
                print("So, you can almost relay on your firewall protection! 85%")
                Info_Style()
                print("Going back to main menu in 15 seconds...")
                time.sleep(15)
                main_menu()
        else:
            Warning_Style()
            print("The backdoor script seems to be running...")
            Info_Style()
            print("Checking the firewall status...")
            time.sleep(7)
            proc1 = subprocess.Popen(["The-Good-Guys\\WallStatus.bat"], stdout=subprocess.PIPE, shell=True)
            (result, err) = proc1.communicate()
            result = str(result)
            if result.count("On") == 3:
                Warning_Style()
                print("The backdoor was running!")
                Great_Style()
                print("But it was unable to turn off the firewall")
                Info_Style()
                print("Now trying to add an exclusion to your firewall...")
                time.sleep(7)
                proc = subprocess.Popen(["The-Bad-Guys\\"+file2], stdout=subprocess.PIPE, shell=True)
                (res, err) = proc.communicate()
                proc = err
                if proc == 1 or proc == 2:
                    cls()
                    print("""
░██████╗░██████╗░███████╗░█████╗░████████╗██╗
██╔════╝░██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║
██║░░██╗░██████╔╝█████╗░░███████║░░░██║░░░██║
██║░░╚██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░╚═╝
╚██████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██╗
░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Great_Style()
                    print("But it was unable to turn off the firewall")
                    Great_Style()
                    print("And as well it blocked us from adding an exclusion to your firewall")
                    Info_Style()
                    print("You can relay on your firewall protection! 90%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
                else:
                    cls()
                    print(cm.Fore.GREEN + """
░██████╗░░█████╗░░█████╗░██████╗░██╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║
██║░░██╗░██║░░██║██║░░██║██║░░██║██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║╚═╝
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Great_Style()
                    print("But it was unable to turn off the firewall")
                    Warning_Style()
                    print("But we were able to add an exclusion to your firewall!")
                    Info_Style()
                    print("You can almost relay on your firewall protection! But not that much! 75%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
            elif result.count("On") == 2:
                Warning_Style()
                print("The backdoor was running!")
                Warning_Style()
                print("And it was able to turn off 1/3 parts of your firewall")
                Info_Style()
                print("Now trying to add an exclusion to your firewall...")
                proc = subprocess.Popen(["The-Bad-Guys\\"+file2], stdout=subprocess.PIPE, shell=True)
                (res, err) = proc.communicate()
                proc = err
                time.sleep(7)
                if proc == 1 or proc == 2:
                    cls()
                    print(cm.Fore.GREEN + """
░██████╗░░█████╗░░█████╗░██████╗░██╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║
██║░░██╗░██║░░██║██║░░██║██║░░██║██║
██║░░╚██╗██║░░██║██║░░██║██║░░██║╚═╝
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Warning_Style()
                    print("And it was able to turn off 1/3 parts of the firewall")
                    Great_Style()
                    print("But we were unable to add an exclusion to your firewall!")
                    Info_Style()
                    print("You can almost relay on your firewall protection! But not that much! 75%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
                else:
                    cls()
                    print(cm.Fore.YELLOW + """
███╗░░██╗░█████╗░████████╗  ██████╗░░█████╗░██████╗░██╗
████╗░██║██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██║
██╔██╗██║██║░░██║░░░██║░░░  ██████╦╝███████║██║░░██║██║
██║╚████║██║░░██║░░░██║░░░  ██╔══██╗██╔══██║██║░░██║╚═╝
██║░╚███║╚█████╔╝░░░██║░░░  ██████╦╝██║░░██║██████╔╝██╗
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Warning_Style()
                    print("And it was able to turn off 1/3 parts of the firewall")
                    Warning_Style()
                    print("Also, we were able to add an exclusion to your firewall!")
                    Info_Style()
                    print("You can not relay on your firewall protection that much! 60%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
            elif result.count("On") == 1:
                Warning_Style()
                print("The backdoor was running!")
                Warning_Style()
                print("And it was able to turn off 2/3 parts of your firewall")
                Info_Style()
                print("Now trying to add an exclusion to your firewall...")
                proc = subprocess.Popen(["The-Bad-Guys\\"+file2], stdout=subprocess.PIPE, shell=True)
                (res, err) = proc.communicate()
                proc = err
                time.sleep(7)
                if proc == 1 or proc == 2:
                    cls()
                    print(cm.Fore.RED + """
██████╗░░█████╗░██████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║
██████╦╝███████║██║░░██║██║
██╔══██╗██╔══██║██║░░██║╚═╝
██████╦╝██║░░██║██████╔╝██╗
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Warning_Style()
                    print("And it was able to turn off 2/3 parts of the firewall")
                    Great_Style()
                    print("But we were unable to add an exclusion to your firewall!")
                    Info_Style()
                    print("You can not almost relay on your firewall protection!  50%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
                else:
                    cls()
                    print(cm.Fore.RED + """
░██████╗░█████╗░  ██████╗░░█████╗░██████╗░██╗
██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║
╚█████╗░██║░░██║  ██████╦╝███████║██║░░██║██║
░╚═══██╗██║░░██║  ██╔══██╗██╔══██║██║░░██║╚═╝
██████╔╝╚█████╔╝  ██████╦╝██║░░██║██████╔╝██╗
╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Warning_Style()
                    print("And it was able to turn off 2/3 parts of the firewall")
                    Warning_Style()
                    print("Also, we were able to add an exclusion to your firewall!")
                    Info_Style()
                    print("You can not relay on your firewall protection! 40%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
            elif result.count("On") == 0:
                Warning_Style()
                print("The backdoor was running!")
                Warning_Style()
                print("And it was able to turn off your whole firewall")
                Info_Style()
                print("Now trying to add an exclusion to your firewall...")
                proc = subprocess.Popen(["The-Bad-Guys\\"+file2], stdout=subprocess.PIPE, shell=True)
                (res, err) = proc.communicate()
                proc = err
                time.sleep(7)
                if proc == 1 or proc == 2:
                    cls()
                    print(cm.Fore.RED + """
░██████╗░█████╗░  ██████╗░░█████╗░██████╗░██╗
██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██║
╚█████╗░██║░░██║  ██████╦╝███████║██║░░██║██║
░╚═══██╗██║░░██║  ██╔══██╗██╔══██║██║░░██║╚═╝
██████╔╝╚█████╔╝  ██████╦╝██║░░██║██████╔╝██╗
╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Warning_Style()
                    print("And it was able to turn off 3/3 parts of the firewall")
                    Great_Style()
                    print("But we were unable to add an exclusion to your firewall!")
                    Info_Style()
                    print("You can not relay on your firewall protection! 30%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
                else:
                    cls()
                    print(cm.Fore.MAGENTA + """
██╗░░██╗░█████╗░██████╗░██████╗░██╗██████╗░██╗░░░░░███████╗██╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔════╝██║
███████║██║░░██║██████╔╝██████╔╝██║██████╦╝██║░░░░░█████╗░░██║
██╔══██║██║░░██║██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔══╝░░╚═╝
██║░░██║╚█████╔╝██║░░██║██║░░██║██║██████╦╝███████╗███████╗██╗
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚══════╝╚═╝
""")
                    Warning_Style()
                    print("The backdoor was running!")
                    Warning_Style()
                    print("And it was able to turn off 3/3 parts of the firewall")
                    Warning_Style()
                    print("Also, we were able to add an exclusion to your firewall!")
                    Info_Style()
                    print("You must never relay on your firewall's protection! 0%")
                    Info_Style()
                    print("Going back to main menu in 15 seconds...")
                    time.sleep(15)
                    main_menu()
    except PermissionError:
        pass


def Roll_back():
    # Roll back firewall test changes :)
    try:
        cls()
        print(cm.Fore.GREEN + """
█▀█ █▀█ █░░ █░░ █ █▄░█ █▀▀   █▄▄ ▄▀█ █▀▀ █▄▀
█▀▄ █▄█ █▄▄ █▄▄ █ █░▀█ █▄█   █▄█ █▀█ █▄▄ █░█ ▄ ▄ ▄
""")
        Great_Style()
        print("Enabling windows firewall back on...")
        time.sleep(3)
        subprocess.check_output("start The-Good-Guys\\FirewallBack.bat", shell=True)
        Great_Style()
        print("Removing the backdoor from exclusions...")
        time.sleep(3)
        subprocess.check_output("start The-Good-Guys\\NoBackdoor.bat", shell=True)
        Info_Style()
        print("Roll Back completed!")
        Info_Style()
        print("Going back to main menu in 10 seconds...")
        time.sleep(10)
        main_menu()
    except subprocess.CalledProcessError:
        Error_Style()
        print("An error has occurred while trying to roll back the firewall test changes!")
        Info_Style()
        print("Going back to main menu in 7 seconds...")
        time.sleep(7)
        main_menu()


def TellTheFalseDanger():
    # Telling the false danger to the user :) And as well having some fun!
    Info_Style()
    print("There is no danger in this test!")
    Info_Style()
    print("By the way, you may encounter some 'false dangers' like this:")
    print("Some annoying pop-ups from your antivirus!")
    Great_Style()
    print(":)")
    lol = input("Do you want to continue with the 'false danger'? (Y/N) ")
    if lol == "Y" or lol == "y":
        FalseButPositive()
    elif lol == "N" or lol == "n":
        cls()
        print(cm.Fore.GREEN + """
██╗░░░░░░█████╗░██╗░░░░░  ██╗██╗░░
██║░░░░░██╔══██╗██║░░░░░  ╚═╝╚██╗░
██║░░░░░██║░░██║██║░░░░░  ░░░░╚██╗
██║░░░░░██║░░██║██║░░░░░  ░░░░██╔╝
███████╗╚█████╔╝███████╗  ██╗██╔╝░
╚══════╝░╚════╝░╚══════╝  ╚═╝╚═╝░░
""")
        Great_Style()
        print("I know, getting pop-ups from your antivirus is the worst nightmare ever!")
        Info_Style()
        print("Going back to main menu in 6 seconds...")
        time.sleep(6)
        main_menu()
    else:
        Error_Style()
        print("Invalid input!")
        Info_Style()
        print("Going back to main menu in 5 seconds...")
        time.sleep(5)
        main_menu()


def FalseButPositive():
    # False positive virus test :)
    cls()
    print(cm.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
    """)
    Great_Style()
    print("Trying to run all the false positives...")
    Info_Style()
    print("You may see some pop-ups open, don't forget close all of them, else we can not continue the test!")
    time.sleep(7)
    blocked = 0
    with alive_bar(len(os.listdir("The-False-Guys")), spinner="dots_waves", theme="classic",length=30,receipt=False,dual_line=True) as bar:
        for file in os.listdir("The-False-Guys"):
            bar.text(cm.Fore.CYAN + "Running "+cm.Fore.GREEN + file + cm.Fore.RESET)
            ran = subprocess.Popen("start The-False-Guys\\"+file+"",stdout=subprocess.PIPE ,shell=True)
            (out, err) = ran.communicate()
            if err == 1 or err == 2:
                blocked+=1
            else:
                pass
            time.sleep(0.35)
            bar()
    time.sleep(0.7)
    if blocked <= 1:
        cls()
        print(cm.Fore.MAGENTA + """
██╗░░░██╗███████╗░█████╗░██╗
██║░░░██║██╔════╝██╔══██╗██║
██║░░░██║█████╗░░██║░░██║██║
██║░░░██║██╔══╝░░██║░░██║╚═╝
╚██████╔╝██║░░░░░╚█████╔╝██╗
░╚═════╝░╚═╝░░░░░░╚════╝░╚═╝
""")
        Great_Style()
        print("Your anti-virus blocked one or none of our false positives! 99%")
        Info_Style()
        print("You can always relay on that the files blocked by your anti-virus are not false positives!")
        Info_Style()
        print("Going back to main menu in 12 seconds...")
        time.sleep(12)
        main_menu()
    elif blocked <= 3:
        cls()
        print(cm.Fore.GREEN + """
░██████╗░██████╗░███████╗░█████╗░████████╗██╗
██╔════╝░██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║
██║░░██╗░██████╔╝█████╗░░███████║░░░██║░░░██║
██║░░╚██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░╚═╝
╚██████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██╗
░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝
""")
        Great_Style()
        print("Your anti-virus blocked 2 or 3 of our false positives! 80%")
        Info_Style()
        print("You can mostly relay on that the files blocked by your anti-virus are not false positives!")
        Info_Style()
        print("Going back to main menu in 12 seconds...")
        time.sleep(12)
    elif blocked <= 5:
        cls()
        print(cm.Fore.YELLOW + """
███╗░░██╗░█████╗░████████╗  ██████╗░░█████╗░██████╗░██╗
████╗░██║██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗██║
██╔██╗██║██║░░██║░░░██║░░░  ██████╦╝███████║██║░░██║██║
██║╚████║██║░░██║░░░██║░░░  ██╔══██╗██╔══██║██║░░██║╚═╝
██║░╚███║╚█████╔╝░░░██║░░░  ██████╦╝██║░░██║██████╔╝██╗
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝
""")
        Warning_Style()
        print("Your anti-virus blocked 4 or 5 of our false positives! 45%")
        Info_Style()
        print("You can almost(not that much) relay on that the files blocked by your anti-virus are not false positives!")
        Info_Style()
        print("Going back to main menu in 12 seconds...")
        time.sleep(12)
    elif blocked <= 7:
        cls()
        print(cm.Fore.RED + """
██████╗░░█████╗░██████╗░██╗
██╔══██╗██╔══██╗██╔══██╗██║
██████╦╝███████║██║░░██║██║
██╔══██╗██╔══██║██║░░██║╚═╝
██████╦╝██║░░██║██████╔╝██╗
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝
        """)
        Warning_Style()
        print("Your anti-virus blocked 6 or 7 of our false positives! 20%")
        Info_Style()
        print("You can not relay on that the files blocked by your anti-virus are not false positives!")
        Info_Style()
        print("Going back to main menu in 12 seconds...")
        time.sleep(12)
    elif blocked <= 8:
        cls()
        print(cm.Fore.RED + """
██╗░░██╗░█████╗░██████╗░██████╗░██╗██████╗░██╗░░░░░███████╗██╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔════╝██║
███████║██║░░██║██████╔╝██████╔╝██║██████╦╝██║░░░░░█████╗░░██║
██╔══██║██║░░██║██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔══╝░░╚═╝
██║░░██║╚█████╔╝██║░░██║██║░░██║██║██████╦╝███████╗███████╗██╗
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚══════╝╚═╝
        """)
        Error_Style()
        print("Your anti-virus blocked all of our false positives! 0%")
        Info_Style()
        print("You can never relay on that the files blocked by your anti-virus are not false positives!")
        Info_Style()
        print("Going back to main menu in 12 seconds...")
        time.sleep(12)
        main_menu()

def Spyware_test(mode): # Here we test if your anti-virus can block us from accessing your camera and microphone!
    try:
        if mode == "UH":
            file1="Spycam.py"
            file2="Spymic.py"
        elif mode == "SSH":
            file1="Spycam-themida.exe"
            file2="Spymic-themida.exe"
        elif mode == "SH":
            file1="Spycam-vmp.exe"
            file2="Spymic-vmp.exe"
        elif mode == "H":
            file1="Spycam-hard-upx.exe"
            file2="Spymic-hard-upx.exe"
        elif mode == "N":
            file1="Spycam-upx.exe"
            file2="Spymic-upx.exe"
        else:
            file1="Spycam.exe"
            file2="Spymic.exe"
        cls()
        print(cm.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
""")
        Info_Style()
        print("Trying to access your camera to take a picture...")
        time.sleep(4)
        try:
            finalf = "The-Bad-Guys\\"+file1 
            finalf2 = "The-Bad-Guys\\"+file2
            if mode == "UH":
                letssee = subprocess.call(["python", finalf],stdout=subprocess.PIPE, shell=True)
            else:
                letssee = subprocess.call(finalf,stdout=subprocess.PIPE, shell=True)
        except FileNotFoundError:
            Warning_Style()
            print("The spyware file was not found!")
            Great_Style()
            print("This maybe caused by your anti-virus software")
            Info_Style()
            print("If that's true, your anti-virus has done great(probably with signatures)!")
            Info_Style()
            print("Going back to the main menu in 12 seconds...")
            time.sleep(12)
            main_menu()
        if os.path.isfile("The-Bad-Guys\\Oh-Spy.png"):
            spy1 = True
            Warning_Style()
            print("Spyware was able to take a picture from you!")
            os.remove("The-Bad-Guys\\Oh-Spy.png")
            Info_Style()
            print("Trying to access your microphone to record a voice...")
            time.sleep(3)
        else:
            spy1 = False
            Great_Style()
            print("The spyware seems to be blocked to take a picture from you!")
            Info_Style()
            print("Trying to access your microphone to record a voice...")
            time.sleep(3)
        try:
            if mode == "H":
                letssee = subprocess.call(["python", finalf2])
            else:
                letssee= subprocess.call(finalf2,stdout=subprocess.PIPE, shell=True)
        except FileNotFoundError:
            Warning_Style()
            print("The spyware file was not found!")
            Great_Style()
            print("This maybe caused by your anti-virus software")
            Info_Style()
            print("If that's true, your anti-virus has done great(probably with signatures)!")
            Info_Style()
            print("Going back to the main menu in 12 seconds...")
            time.sleep(12)
            main_menu()   
        if os.path.isfile("The-Bad-Guys\\Oh-Spy.wav"):
            os.remove("The-Bad-Guys\\Oh-Spy.wav")
            spy2 = True
        else:
            spy2 = False

        if spy1 == True and spy2 == True:
            cls()
            print(cm.Fore.MAGENTA + """
██╗░░██╗░█████╗░██████╗░██████╗░██╗██████╗░██╗░░░░░███████╗██╗
██║░░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔════╝██║
███████║██║░░██║██████╔╝██████╔╝██║██████╦╝██║░░░░░█████╗░░██║
██╔══██║██║░░██║██╔══██╗██╔══██╗██║██╔══██╗██║░░░░░██╔══╝░░╚═╝
██║░░██║╚█████╔╝██║░░██║██║░░██║██║██████╦╝███████╗███████╗██╗
╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚══════╝╚═╝
""")
            Error_Style()
            print("The spyware was able to take a picture and record an audio from you!")
            Info_Style()
            print("You must never relay on your anti-virus's spyware protection(or camera/microphone shield)! 0%")
            Info_Style()
            print("Going back to main menu in 12 seconds...")
            time.sleep(12)
            main_menu()
        elif spy1 == True and spy2 == False:
            cls()
            print(cm.Fore.YELLOW + """
███╗░░░███╗███████╗██████╗░██╗██╗░░░██╗███╗░░░███╗
████╗░████║██╔════╝██╔══██╗██║██║░░░██║████╗░████║
██╔████╔██║█████╗░░██║░░██║██║██║░░░██║██╔████╔██║
██║╚██╔╝██║██╔══╝░░██║░░██║██║██║░░░██║██║╚██╔╝██║
██║░╚═╝░██║███████╗██████╔╝██║╚██████╔╝██║░╚═╝░██║
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░╚═════╝░╚═╝░░░░░╚═╝
""")
            Great_Style()
            print("The spyware was able to take a picture but it was unable to record your voice!")
            Info_Style()
            print("You can almost relay on your anti-virus's spyware protection(or camera/microphone shield)! 50%")
            Info_Style()
            print("Going back to main menu in 12 seconds...")
            time.sleep(12)
            main_menu()
        elif spy1 == False and spy2 == True:
            cls()
            print(cm.Fore.YELLOW + """
███╗░░░███╗███████╗██████╗░██╗██╗░░░██╗███╗░░░███╗
████╗░████║██╔════╝██╔══██╗██║██║░░░██║████╗░████║
██╔████╔██║█████╗░░██║░░██║██║██║░░░██║██╔████╔██║
██║╚██╔╝██║██╔══╝░░██║░░██║██║██║░░░██║██║╚██╔╝██║
██║░╚═╝░██║███████╗██████╔╝██║╚██████╔╝██║░╚═╝░██║
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░╚═════╝░╚═╝░░░░░╚═╝
""")
            Great_Style()
            print("The spyware was unable to take a picture but it was able to record your voice!")
            Info_Style()
            print("You can almost relay on your anti-virus's spyware protection(or camera/microphone shield)! 50%")
            Info_Style()
            print("Going back to main menu in 12 seconds...")
            time.sleep(12)
            main_menu()
        elif spy1 == False and spy2 == False:
            cls()
            print(cm.Fore.GREEN + """
░██████╗░██████╗░███████╗░█████╗░████████╗██╗
██╔════╝░██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║
██║░░██╗░██████╔╝█████╗░░███████║░░░██║░░░██║
██║░░╚██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░╚═╝
╚██████╔╝██║░░██║███████╗██║░░██║░░░██║░░░██╗
░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝
""")
            Great_Style()
            print("The spyware was unable to take a picture or record a voice!")
            Info_Style()
            print("You can always relay on your anti-virus's spyware protection(or camera/microphone shield)! 100%")
            Info_Style()
            print("Going back to main menu in 12 seconds...")
            time.sleep(12)
            main_menu()

    except PermissionError:
        Warning_Style()
        print("The spyware file can not execute!")
        Great_Style()
        print("This maybe caused by your anti-virus")
        Info_Style()
        print("If that's true, your anti-virus has done great(probably with signatures)!")
        Info_Style()
        print("Going back to the main menu in 12 seconds...")
        time.sleep(12)
        main_menu()

def main_menu():
    cls()   
    c1 = cm.Fore.RED + """                 .-:     :-.                 
              :+#+         =#+:              
          .-*@@+   """+cm.Fore.CYAN + "PROTEST"+cm.Fore.RED +"""   =@@*=.          
          %@@# """+cm.Fore.LIGHTCYAN_EX + "Protection Test"+cm.Fore.RED+""" #@@%          
          @@@%                 #@@@          
          @@@@ """+cm.Fore.GREEN + "By @SepyMovasat"+cm.Fore.RED+""" @@@@          
          @@@@:    :=#@#+:    :@@@@.         
         .@@@@+ -*@@@#+#@@@*- =@@@@:         
         -@@@@%++++-     -++++%@@@@=         
      :+%@@@@@@@@@%*=: :=*%@@@@@@@@@@*:      
   :*@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@*-   
-*@@@@@@#+--+#@@@@:       :@@@@#+-:+#@@@@@@*-
@@@%*-.    +@#:+@@@-     -@@@+-#@+    .-+%@@@
@@-        +@@.  -=+=   =+=-  .@@+        :@@
@#         +@@.   =@@* *@@=   :@@+         #@
@:         -%@@%+::@@@@@@@::+%@@%-         .@
*    """+cm.Fore.LIGHTMAGENTA_EX + "Cool" +cm.Fore.RED+"""    .=#@@-@@@@@@@-@@#=.    """+cm.Fore.LIGHTMAGENTA_EX + "Pro!"+cm.Fore.RED+"""    *
.                -:#@@@@@#:-                .
                .+%@@@@@@@%+.                
   :.         -#@@@@@@%@@@@@@#-         .:   
    .=*#*+=-*@@@@@%+-   -+%@@@@@*-=+*#*=.    
        -*@@@@%*-   """+cm.Fore.LIGHTMAGENTA_EX + "Easy"+cm.Fore.RED+"""   -*%@@@@*-                     
"""

    c2 = cm.Fore.YELLOW + """                      =#%%#=                      
                    :%#-::-#@:                    
                    -=::::::+@-                   
              .:  :@+::::::::+@:  :.              
            =%#*%+%#::::::::..*@+%**%=            
           +@=::-@|||"""+cm.Fore.CYAN + "PROTEST"+cm.Fore.YELLOW+"""|||@@:..:%*           
 .*%%%####%@+:::-"""+cm.Fore.LIGHTCYAN_EX + "Protection Test"+cm.Fore.YELLOW+"""-....-@%#####%%*: 
=@#+++====#@-::::::::::::.............@#=======*@=
@#++++====#@-::::::::::::.............%#========#@
@#++"""+cm.Fore.LIGHTMAGENTA_EX + "Cool" +cm.Fore.YELLOW+"""==*@=::::::::::::::.....:....:@#++"""+cm.Fore.LIGHTMAGENTA_EX + "Pro!"+cm.Fore.YELLOW+"""+++@
@#+++++++++%%-::--"""+cm.Fore.GREEN + "By @SepyMovasat"+cm.Fore.YELLOW+"""--..#%+++++++++#@
@#++++++++++%%=::::::::::::........:%%++++++++++#@
@@%%%%%%@@%%%%@#=-:::::::::::....-#@%%%%@@%%%%%%@@
@*------%%++++=+#@##+=-"""+cm.Fore.LIGHTMAGENTA_EX + "Easy"+cm.Fore.YELLOW+"""-=+*%#+------*@++++++#@
@*------%%++++====+*#%%%%%%%%#*=--------*@++++++#@
@*------%%++++++========%%======--------*@++++++#@
@*------%%++++++++++++++%%==============#@++++++#@
@*------%%++++++++++++++%%==============#@++++++#@
@@%%%%%%@@%%%%%%@@%%%%%%%%%%%%%%%@%%%%%%%@%%%%%%@@
@#++++==========%%====--"""+cm.Fore.BLUE + "MIT"+cm.Fore.YELLOW+"""-----#@++++==========*@
@#++++==========%%===="""+cm.Fore.RED + "License"+cm.Fore.YELLOW+"""---#@++++==========*@
@#+++++=========%%=====---------#@++++++========*@
@%++++++++++++++%%==============#@++++++++++++++#@
-@#+++++++++++++%%==============#@+++++++++++++#@-
 .+#%%%%%%%%%%%%@@%%%%%%%%%%%%%%@@%%%%%%%%%%%%#+."""

    c3 = cm.Fore.GREEN + """                       =%%-                       
                     .#%.:%#.                     
                   -##-    -%*:                   
                -*%+:  :@@.  :*%*-                
             -##=:      --      :+##+-.           
      -+*##:          """+cm.Fore.CYAN + "PROTEST"+cm.Fore.GREEN+"""       :=*##*+-      
     *%:.         """+cm.Fore.LIGHTCYAN_EX + "Protection Test"+cm.Fore.GREEN+"""        .:%*     
     ##  *%+           :--:           +%*  ##     
     *%  -+:        .*%+==+%*.        :+-  %*     
     =@             %* """+cm.Fore.LIGHTMAGENTA_EX + "Pro!"+cm.Fore.GREEN+""" *%            .@-     
      @+   """+cm.Fore.LIGHTMAGENTA_EX + "Easy"+cm.Fore.GREEN+"""    :@=::::::=@:   """+cm.Fore.LIGHTMAGENTA_EX + "Cool" +cm.Fore.GREEN+"""    +@      
      =@.        :@*++++++++++*@.        .@=      
       ##        =@     --     @=        ##       
        %+       =@    -@@-    @=       .+        
        .@+      =@     --     @=      =:         
+%%#:    .%*     :@*==========*@:     *%.   ..*%%+
#%*@+%*:::-@#      ::::::::::::      #@-::-*%+%###
 ::   -=====*%.                    :%*=====:   :: 
#%*@+++++++++@@=  """+cm.Fore.RED + "By @SepyMovasat" + cm.Fore.GREEN+""" =@%+++++++++%###
+%%#:.:**=....:##               .##:....=**:..*%%+
      %%+@######%@=     :.     =@%######@+%%      
      .=+-     ::-@%.  -@@.  :%%-::     -+=.      
        +%##-+%+++++%+  .  .*%+++++%+-##%+        
        #%#%=-       +@+  +@=       -=%#%*        
          .            +##+            ."""
          
    c4 = cm.Fore.GREEN + """ .=+=:                                      :=+=: 
+@@@@@#                                    *@@@@@*
@@@+@@@+-:                              :-=@@@=@@@
.*@@@@@@@@@@=-#+                  =%-=@@@@@@@@@@#.
    *@@=.-*@@@@#:     """+cm.Fore.CYAN + "PROTEST"+cm.Fore.GREEN+"""    .*@@@@#-.-@@#    
    .@@%:-%@@@@#: """+cm.Fore.LIGHTCYAN_EX + "Protection Test"+cm.Fore.GREEN+""".*@@@@%-:%@@:    
     =%@@@@#:-%@@*+*#%@@@@@@%#*+*@@%=:#@@@@%=     
     :%@@@@@++#@@@@%#*+*@@#+*#%@@@@%+=@@@@@%-     
      -*:.+@@@%*=.     =@@+     .-*%@@@*..*=      
          .@@#  """+cm.Fore.LIGHTMAGENTA_EX + "Easy"+cm.Fore.GREEN+"""  .+@@*.  """+cm.Fore.LIGHTMAGENTA_EX + "Cool" +cm.Fore.GREEN+"""  *@@:          
           @@@    -#@@@@@@@@@@#=    %@@.          
           %@@.   -@@#::...:#@@=    @@@           
           +@@=    @@@ """+cm.Fore.LIGHTMAGENTA_EX + "Pro!"+cm.Fore.GREEN+""" %@@.   -@@*           
           .@@%    +@@+    =@@*    #@@:           
            *@@-    %@@:  .@@@    :@@#            
            .@@@.   :@@@..%@@:    %@@:            
           .*@@@#    :@@@@@@-    #@@@%-           
         .*@@%*@@#    .%@@%:    *@@**@@%=         
       .*@@%=  #@@%.   =@@+    #@@@: :*@@%-       
     .*@@%=  =@@@@@@-  =@@+  :@@@%@@#: .*@@%=     
   .*@@%=  =@@@*..#@@#.=@@+.*@@#. -%@@*: .*@@%=   
  *@@%=  =@@@*.    -%@@%@@%@@@-     -%@@#: .*@@@: 
  @@@  =@@@*.        =%@@@@%=         -%@@#:.*@@- 
  #@@@@@@*.            :++:             -%@@@@@@. 
  .-==++.         """+cm.Fore.RED + "By @SepyMovasat" + cm.Fore.GREEN+"""         -=--:.  """
          
    print(random.choice([c1,c1,c1,c2,c2,c3,c3,c4,c4]))
    print(cm.Fore.MAGENTA + "\n1- Test Ransomware Protection\n ")
    print(cm.Fore.MAGENTA +"2- Test Windows Firewall Protection vs. Backdoor\n")
    print(cm.Fore.MAGENTA + "3- Roll back firewall test changes")
    print(cm.Fore.MAGENTA + "\n4- False Positive Test")
    print(cm.Fore.MAGENTA + "\n5- Spyware Test(camera and microphone)")
    print(cm.Fore.MAGENTA + "\n6- Exit")
    main_inp = input(cm.Fore.RESET + "Which one? ")
    if main_inp == "1":
        tell_the_danger()
    elif main_inp == "2":
        Info_Style()
        print("This test has six modes [easy mode, normal mode, hard mode, super hard mode, super super hard mode, ultra hard mode]")
        print(""+cm.Fore.LIGHTGREEN_EX + "Easy mode:"+ cm.Fore.RESET+" A simple exe file that tries to spy on you(easy to detect both using signatures and behavioral protection)")
        print(""+cm.Fore.GREEN + "Normal mode:"+ cm.Fore.RESET +" An exe file that is packed by upx and tries to spy on you(harder to detect using signatures)")
        print(cm.Fore.YELLOW + "Hard mode:" + cm.Fore.RESET + " An exe filed that is packed by upx but more than usual (upx --ultra-brute) - (even harder to detect using signatures)")
        print(cm.Fore.LIGHTYELLOW_EX + "Super hard mode:" + cm.Fore.RESET + " An exe file that is protected by VMProtect (Super hard to detect both by signatures and behavioral protection)")
        print(cm.Fore.RED + "Super super hard mode:" + cm.Fore.RESET + " An exe file that is protected by Themida (Super super hard to detect by any protection system - It is so unique)")
        print(cm.Fore.LIGHTRED_EX + "Ultra hard mode:"+ cm.Fore.RESET+ " A python file that tries to encrypt ur files(almost impossible to detect by signatures - just behavioral protection)")
        mode =input("Please choose the mode you want to use ["+cm.Fore.LIGHTGREEN_EX+ "E"+cm.Fore.RESET +"/" + cm.Fore.GREEN+ "N"+cm.Fore.RESET+"/" +cm.Fore.YELLOW + "H" + cm.Fore.RESET + "/" + cm.Fore.LIGHTYELLOW_EX + "SH" + cm.Fore.RESET + "/" + cm.Fore.RED  + "SSH" + cm.Fore.RESET + "/" + cm.Fore.LIGHTRED_EX + "UH" + cm.Fore.RESET + "] ")
        if mode == "E" or mode == "e":
            BrokenWall("E")
        elif mode == "N" or mode == "n":
            BrokenWall("N")
        elif mode == "H" or mode == "h":
            BrokenWall("H")
        elif mode == "SH" or mode == "sh" or mode == "Sh" or mode == "sH":
            BrokenWall("SH")
        elif mode == "SSH" or mode == "ssh" or mode == "Ssh" or mode == "SSh" or mode == "sSH" or mode == "sSh" or mode == "SsH":
            BrokenWall("SSH")
        elif mode == "UH" or mode == "uh" or mode == "Uh" or mode == "uH":
            BrokenWall("UH")
        else:
            cls()
            print(cm.Fore.RED + """
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░█████╗░░█████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚═╝███╔╝╚═╝███╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░░░╚══╝░░░░╚══╝░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░░░░██╗░░░░░██╗░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░
""")
            Error_Style()
            print("Error: Wrong mode selected!")
            Great_Style()
            print("Please try again!")
            Info_Style()
            print("Going back to main menu in 5 seconds...")
            time.sleep(5)
    elif main_inp == "3":
        Roll_back()
    elif main_inp == "4":
        TellTheFalseDanger()
    elif main_inp == "5":
        print("This test has six modes [easy mode, normal mode, hard mode, super hard mode, super super hard mode, ultra hard mode]")
        print(""+cm.Fore.LIGHTGREEN_EX + "Easy mode:"+ cm.Fore.RESET+" A simple exe file that tries to spy on you(easy to detect both using signatures and behavioral protection)")
        print(""+cm.Fore.GREEN + "Normal mode:"+ cm.Fore.RESET +" An exe file that is packed by upx and tries to spy on you(harder to detect using signatures)")
        print(cm.Fore.YELLOW + "Hard mode:" + cm.Fore.RESET + " An exe filed that is packed by upx but more than usual (upx --ultra-brute) - (even harder to detect using signatures)")
        print(cm.Fore.LIGHTYELLOW_EX + "Super hard mode:" + cm.Fore.RESET + " An exe file that is protected by VMProtect (Super hard to detect both by signatures and behavioral protection)")
        print(cm.Fore.RED + "Super super hard mode:" + cm.Fore.RESET + " An exe file that is protected by Themida (Super super hard to detect by any protection system - It is so unique)")
        print(cm.Fore.LIGHTRED_EX + "Ultra hard mode:"+ cm.Fore.RESET+ " A python file that tries to encrypt ur files(almost impossible to detect by signatures - just behavioral protection)")
        mode =input("Please choose the mode you want to use ["+cm.Fore.LIGHTGREEN_EX+ "E"+cm.Fore.RESET +"/" + cm.Fore.GREEN+ "N"+cm.Fore.RESET+"/" +cm.Fore.YELLOW + "H" + cm.Fore.RESET + "/" + cm.Fore.LIGHTYELLOW_EX + "SH" + cm.Fore.RESET + "/" + cm.Fore.RED  + "SSH" + cm.Fore.RESET + "/" + cm.Fore.LIGHTRED_EX + "UH" + cm.Fore.RESET + "] ")
        if mode == "E" or mode == "e":
            Spyware_test("E")
        elif mode == "N" or mode == "n":
            Spyware_test("N")
        elif mode == "H" or mode == "h":
            Spyware_test("H")
        elif mode == "SH" or mode == "sh" or mode == "Sh" or mode == "sH":
            Spyware_test("SH")
        elif mode == "SSH" or mode == "ssh" or mode == "Ssh" or mode == "SSh" or mode == "sSH" or mode == "sSh" or mode == "SsH":
            Spyware_test("SSH")
        elif mode == "UH" or mode == "uh" or mode == "Uh" or mode == "uH":
            Spyware_test("UH")
        else:
            cls()
            print(cm.Fore.RED + """
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░█████╗░░█████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚═╝███╔╝╚═╝███╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░░░╚══╝░░░░╚══╝░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░░░░██╗░░░░░██╗░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░
""")
            Error_Style()
            print("Error: Wrong mode selected!")
            Great_Style()
            print("Please try again!")
            Info_Style()
            print("Going back to main menu in 5 seconds...")
            time.sleep(5)
            main_menu()
    elif main_inp == "6":
        cls()
        print(cm.Fore.GREEN + """
░██████╗███████╗███████╗  ██╗░░░██╗░█████╗░██╗░░░██╗██╗
██╔════╝██╔════╝██╔════╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██║
╚█████╗░█████╗░░█████╗░░  ░╚████╔╝░██║░░██║██║░░░██║██║
░╚═══██╗██╔══╝░░██╔══╝░░  ░░╚██╔╝░░██║░░██║██║░░░██║╚═╝
██████╔╝███████╗███████╗  ░░░██║░░░╚█████╔╝╚██████╔╝██╗
╚═════╝░╚══════╝╚══════╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝
""")
        Great_Style()
        print(cm.Fore.RESET + "Exiting in 4 seconds...")
        time.sleep(4)
        exit()
    else:
        cls()
        print(cm.Fore.RED + """
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░█████╗░░█████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚═╝███╔╝╚═╝███╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░░░╚══╝░░░░╚══╝░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░░░░██╗░░░░░██╗░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░
""")
        Error_Style()
        print("Error: Wrong option selected!")
        Great_Style()
        print("Please try again!")
        Info_Style()
        print("Going back to main menu in 5 seconds...")
        time.sleep(5)
        main_menu()

if __name__ == "__main__":
    if is_admin():
        if sys.platform == "win32":
            main_menu()
        else:
            Warning_Style()
            print("This is the windows version of the program")
            Info_Style()
            print("But you are using Linux/Mac")
            Info_style()
            print("Exiting...")
            time.sleep(4)
            exit()
    else:
        Error_Style()
        print("To run this python file, you need to run it as administrator")
        Great_Style()
        print("See you after you ran me as admin!")
        Info_Style()
        print("Exiting in 7 seconds...")
        time.sleep(7) 