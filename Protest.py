# Created by @TheCcortex | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" #
# Please note: Although that this is for testing purposes, It may cause file loss#
# JUST FOR WINDOWS #
# Created by @TheCcortex | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" #
# Please note: Although that this is for testing purposes, It may cause file loss#
# JUST FOR WINDOWS #

import colorama as cm #Used for creating some sort of UI
import subprocess #Used for executing files a lot
import sys #Used like subprocess
import time #Used for time.sleep
import os #Used in different parts of the program 
import ctypes #Used in is_admin()

    
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
    CARE = input("Do you accept the potential"+cm.Fore.RED + " danger"+cm.Fore.RESET +" ["+cm.Fore.CYAN + "Y"+cm.Fore.RESET + "/" + cm.Fore.YELLOW + "N"+cm.Fore.RESET + "] ")
    if CARE == "Y":
        cls()
        Info_Style()
        print("This test has two modes [easy mode, hard mode]")
        rmode = input("Please choose the mode you want to use ["+cm.Fore.CYAN + "E"+cm.Fore.RESET +"/" + cm.Fore.YELLOW + "H"+cm.Fore.RESET + "] ")
        if rmode == "E":
            Ransom("E")
        elif rmode == "e":
            Ransom("E")
        else:
            Ransom("H")
    elif CARE == "y":
        Ransom()
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
        time.sleep(6)
        try:
            finalf = "The-Bad-Guys//"+file 
            if mode == "E":
                letssee = subprocess.call(["python",finalf])

            else:
                letssee = subprocess.call([sys.executable, finalf])
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
                print(
                    "Your anti-virus or firewall blocked us from adding the exclusions to your firewall!")
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
    for file in os.listdir("The-False-Guys"):
        ran = subprocess.Popen("start The-False-Guys\\"+file+"",stdout=subprocess.PIPE ,shell=True)
        (out, err) = ran.communicate()
        if err == 1 or err == 2:
            blocked+=1
        else:
            pass
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

def Spyware_test(): # Here we test if your anti-virus can block us from accessing your camera and microphone!
    try:
        file1="Spycam.py"
        file2="Spymic.py"
        cls()
        print(cm.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
""")
        Info_Style()
        print("Trying to access your camera to take a picture...")
        time.sleep(4)
        try:
            finalf = "The-Bad-Guys//"+file1 
            finalf2 = "The-Bad-Guys//"+file2
            letssee = subprocess.call(["python", finalf])
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
        if os.path.isfile("The-Bad-Guys//Oh-Spy.png"):
            spy1 = True
            Warning_Style()
            print("Spyware was able to take a picture from you!")
            os.remove("The-Bad-Guys//Oh-Spy.png")
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
            letssee = subprocess.call(["python", finalf2])
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
        if os.path.isfile("The-Bad-Guys//Oh-Spy.wav"):
            os.remove("The-Bad-Guys//Oh-Spy.wav")
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
    print(cm.Fore.CYAN + """   
██████╗░██████╗░░█████╗░████████╗███████╗░██████╗████████╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║░░██║░░░██║░░░█████╗░░╚█████╗░░░░██║░░░
██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║╚█████╔╝░░░██║░░░███████╗██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░""")
    print(cm.Fore.GREEN + "- Test your system's protection like a pro! ")
    print(cm.Fore.MAGENTA + "\n1- Test Ransomware Protection\n ")
    print(cm.Fore.MAGENTA +"2- Test Firewall Protection | Just windows firewall\n")
    print(cm.Fore.MAGENTA + "3- Roll back firewall test changes")
    print(cm.Fore.MAGENTA + "\n4- False Positive Test")
    print(cm.Fore.MAGENTA + "\n5- Spyware Test(camera and microphone)")
    print(cm.Fore.MAGENTA + "\n6- Exit")
    print(cm.Fore.GREEN + "\nBy @TheCcortex - MIT license")
    main_inp = input(cm.Fore.RESET + "Which one? ")
    if main_inp == "1":
        tell_the_danger()
    elif main_inp == "2":
        Info_Style()
        print("This test had two modes: [easy mode, hard mode]")
        eorh =input("Please choose the mode you want to use ["+cm.Fore.CYAN + "E"+cm.Fore.RESET +"/" + cm.Fore.YELLOW + "H"+cm.Fore.RESET + "] ")
        if eorh == "E" or eorh == "e":
            BrokenWall("E")
        else:
            BrokenWall("H")
    elif main_inp == "3":
        Roll_back()
    elif main_inp == "4":
        TellTheFalseDanger()
    elif main_inp == "5":
        Spyware_test()
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
        print("Error: Wrong option/input selected!")
        Great_Style()
        print("Please try again!")
        Info_Style()
        print("Going back to main menu in 6 seconds...")
        time.sleep(6)
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
