# Created by @TheCcortex | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" #
# Please note: Although that this is for testing purposes, It may create problems or file loss#
# SO PLEASE USE THIS PYTHON SCRIPT WITH A LOT OF CARE #
# JUST FOR WINDOWS #

import colorama
import subprocess
import sys
import time
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def cls():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def Great_Style(): 
    print( colorama.Fore.RESET + "[" + colorama.Fore.GREEN + "+" + colorama.Fore.RESET + "] ",end="")

def Error_Style(): 
    print(colorama.Fore.RESET + "[" + colorama.Fore.RED + "!" + colorama.Fore.RESET + "] ",end="")

def Info_Style(): 
    print(colorama.Fore.RESET + "[" + colorama.Fore.BLUE + "i" + colorama.Fore.RESET + "] ",end="")
        
def Warning_Style(): 
    print(colorama.Fore.RESET + "[" + colorama.Fore.YELLOW + "!" + colorama.Fore.RESET + "] ",end="")

def No_Worry_Style(): 
    print(colorama.Fore.RESET + "[" + colorama.Fore.GREEN + "OK" + colorama.Fore.RESET + "] ",end="")

def Ask_Style(): 
    print(colorama.Fore.RESET + "[" + colorama.Fore.BLUE + "???" + colorama.Fore.RESET + "] ",end="")

def tell_the_danger():
    # Here we try to encrypt all data in the documents folder | SO TAKE CARE #
    Info_Style()
    print("In this part we test your anti-virus's ransomware protection")
    Info_Style()
    print("For doing that, we try to encrypt all data in the documents folder")
    Great_Style()
    print("For being safe from this, copy your files in any other folder!")
    Warning_Style()
    CARE = input("Do you accept the potential"+colorama.Fore.RED + " danger"+colorama.Fore.RESET + " ["+colorama.Fore.CYAN + "Y"+colorama.Fore.RESET + "/" +colorama.Fore.YELLOW + "N"+colorama.Fore.RESET +"] ")
    if CARE == "Y":
        Info_Style()
        print(colorama.Fore.GREEN + "Let's test it!")
        time.sleep(1.5)
        Ransom()
    elif CARE == "y":
        Info_Style()
        print(colorama.Fore.GREEN + "Let's test it!")
        time.sleep(1.5)
        Ransom()
    else:
        No_Worry_Style()
        print("No need to worry, going back to the main menu...")
        time.sleep(5)
        main_menu()

def Ransom():
    # Here we try to encrypt all data in the documents folder | SO TAKE CARE #
    usr = os.getlogin()
    cls()
    print("""
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀ 
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
    """)
    Info_Style()
    print("Starting the ransomware test")
    time.sleep(6)
    letssee = subprocess.call([sys.executable, "Python//The-Bad-Guys/Encrypt.py"])
    if letssee == "1":
        cls()
        print(colorama.Fore.MAGENTA +"""
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
        Warning_Style()
        print("Ransomware was able to load in memory")
        Info_Style()
        print("Trying to encrypt the files now...")
        time.sleep(8)
        for r, d, files in os.walk("C:\\Users\\"+usr+"\\Documents"):
            for file in files:
                lfile = os.path.join(r, file)
                if not "desktop.ini" in lfile:
                    if lfile.endswith(".WOW"):
                        cls()
                        print(colorama.Fore.RED + """
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
                        print(colorama.Fore.GREEN + """
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

def BrokenWall():
    # Here we test your firewall's protection | This part is not dangerous | Cause we roll back all the changes #
    cls()
    print(colorama.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
    """)
    Info_Style()
    print("Stating the test...")
    Info_Style()
    print("Trying to disable your firewall...")
    time.sleep(7)
    proc = subprocess.Popen(["The-Bad-Guys\\BrokenWall.bat"], stdout=subprocess.PIPE, shell=True)
    (res,err) = proc.communicate()
    proc = err
    if proc == 1:
        Great_Style()
        print("Your Anti-virus or firewall didn't allow us to turn the firewall off!")
        Info_Style()
        print("Until now it was great!")
        Info_Style()
        print("Now trying to add an exclusion to your firewall...")
        time.sleep(7)
        proc = subprocess.Popen(["The-Bad-Guys\\BadExclusion.bat"], stdout=subprocess.PIPE, shell=True)
        (res,err) = proc.communicate()
        proc = err
        if proc == 1:
            cls()
            print(colorama.Fore.MAGENTA + """
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
            print(colorama.Fore.GREEN + """
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
            print("So, you can almost relay on your firewall protection! 90%")
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
        (result,err) = proc1.communicate()
        result = str(result)
        if result.count("On") == 3:
            Warning_Style()
            print("The backdoor was running!")
            Great_Style()
            print("But it was unable to turn off the firewall")
            Info_Style()
            print("Now trying to add an exclusion to your firewall...")
            time.sleep(7)
            proc = subprocess.Popen(["The-Bad-Guys\\BadExclusion.bat"], stdout=subprocess.PIPE, shell=True)
            (res,err) = proc.communicate()
            proc = err
            if proc == 1:
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
                print(colorama.Fore.GREEN + """
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
            proc = subprocess.Popen(["The-Bad-Guys\\BadExclusion.bat"], stdout=subprocess.PIPE, shell=True)
            (res,err) = proc.communicate()
            proc = err
            time.sleep(7)
            if proc == 1:
                cls()
                print(colorama.Fore.GREEN + """
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
                print(colorama.Fore.YELLOW + """
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
            proc = subprocess.Popen(["The-Bad-Guys\\BadExclusion.bat"], stdout=subprocess.PIPE, shell=True)
            (res,err) = proc.communicate()
            proc = err
            time.sleep(7)
            if proc == 1:
                cls()
                print(colorama.Fore.RED + """
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
                print(colorama.Fore.RED + """
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
            proc = subprocess.Popen(["The-Bad-Guys\\BadExclusion.bat"], stdout=subprocess.PIPE, shell=True)
            (res,err) = proc.communicate()
            proc = err
            time.sleep(7)
            if proc == 1:
                cls()
                print(colorama.Fore.RED + """
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
                print(colorama.Fore.MAGENTA + """
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

def Roll_back():
    cls()
    print(colorama.Fore.GREEN + """
█▀█ █▀█ █░░ █░░ █ █▄░█ █▀▀   █▄▄ ▄▀█ █▀▀ █▄▀
█▀▄ █▄█ █▄▄ █▄▄ █ █░▀█ █▄█   █▄█ █▀█ █▄▄ █░█ ▄ ▄ ▄
""")
    Great_Style()
    print("Enabling windows firewall back on...")
    time.sleep(3)
    subprocess.check_output("start The-Good-Guys\\FirewallBack.bat",shell=True)
    Great_Style()
    print("Removing the backdoor from exclusions...")
    time.sleep(3)
    subprocess.check_output("start The-Good-Guys\\NoBackdoor.bat",shell=True)
    Info_Style()
    print("Roll Back completed!")
    Info_Style()
    print("Going back to main menu in 10 seconds...")
    time.sleep(10)
    main_menu()


def main_menu():
    cls()
    print(colorama.Fore.CYAN + """   
██████╗░██████╗░░█████╗░████████╗███████╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░░░██║░░░█████╗░░╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░███████╗██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░""")
    print(colorama.Fore.GREEN + "- Test your system's protection like a pro! ")
    print(colorama.Fore.MAGENTA + "\n1- Test Ransomware Protection\n ")
    print(colorama.Fore.MAGENTA + "2- Test Firewall Protection\n")
    print(colorama.Fore.MAGENTA + "3- Roll back firewall test changes")
    print(colorama.Fore.MAGENTA + "\n4- Exit")
    print(colorama.Fore.GREEN + "\nBy @TheCcortex - MIT license")
    main_inp = input(colorama.Fore.RESET + "Which one? ")
    if main_inp == "1":
        tell_the_danger()
    elif main_inp == "2":
        BrokenWall()
    elif main_inp == "3":
        Roll_back()
    elif main_inp == "4":
        cls()
        print(colorama.Fore.GREEN + """
░██████╗███████╗███████╗  ██╗░░░██╗░█████╗░██╗░░░██╗██╗
██╔════╝██╔════╝██╔════╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██║
╚█████╗░█████╗░░█████╗░░  ░╚████╔╝░██║░░██║██║░░░██║██║
░╚═══██╗██╔══╝░░██╔══╝░░  ░░╚██╔╝░░██║░░██║██║░░░██║╚═╝
██████╔╝███████╗███████╗  ░░░██║░░░╚█████╔╝╚██████╔╝██╗
╚═════╝░╚══════╝╚══════╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝
""")
        print(colorama.Fore.RESET + "Exiting in 4 seconds...")
        time.sleep(4)
        exit()
    else:
        cls()
        print("""
░██╗░░░░░░░██╗██╗░░██╗░█████╗░████████╗░█████╗░░█████╗░
░██║░░██╗░░██║██║░░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
░╚██╗████╗██╔╝███████║███████║░░░██║░░░╚═╝███╔╝╚═╝███╔╝
░░████╔═████║░██╔══██║██╔══██║░░░██║░░░░░░╚══╝░░░░╚══╝░
░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║░░░██║░░░░░░██╗░░░░░██╗░░
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░╚═╝░░
""")
        Error_Style()
        print("Error: Wrong option/input selected!")
        Great_Style()
        print("Please try again!")
        Info_Style()
        print("Going back to main menu in 7 seconds...")
        time.sleep(7)
        main_menu()

if __name__ == "__main__":
    if is_admin():
        main_menu()
    else:
        Error_Style()
        print("To run this python file, you need to run it as administrator")
        Great_Style()
        print("See you after you ran me as admin!")
        Info_Style()
        print("Exiting in 7 seconds...")
        time.sleep(7)
