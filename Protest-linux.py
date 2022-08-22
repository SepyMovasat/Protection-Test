# Created by @TheCcortex | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" #
# Please note: Although that this is for testing purposes, It may cause file loss#
# JUST FOR LINUX #

import colorama #Used for creating some sort of UI
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
    print(colorama.Fore.RESET +"[" + colorama.Fore.GREEN + "+" + colorama.Fore.RESET + "] ", end="")


def Error_Style():
    print(colorama.Fore.RESET +"[" + colorama.Fore.RED + "!" + colorama.Fore.RESET + "] ", end="")


def Info_Style():
    print(colorama.Fore.RESET +"[" + colorama.Fore.BLUE + "i" + colorama.Fore.RESET + "] ", end="")


def Warning_Style():
    print(colorama.Fore.RESET +"[" + colorama.Fore.YELLOW + "!" + colorama.Fore.RESET + "] ", end="")


def No_Worry_Style():
    print(colorama.Fore.RESET +"[" + colorama.Fore.GREEN + "OK" + colorama.Fore.RESET + "] ", end="")


def Ask_Style():
    print(colorama.Fore.RESET +"[" + colorama.Fore.BLUE + "???" + colorama.Fore.RESET + "] ", end="")


def tell_the_danger():
    # Here we try to encrypt all data in the documents folder | SO TAKE CARE #
    Info_Style()
    print("In this part we test your anti-virus's ransomware protection")
    Info_Style()
    print("For doing that, we try to encrypt all data in the documents folder")
    Great_Style()
    print("For being safe from this, copy your files in any other folder(but the folder must have at least a file in it)!")
    Warning_Style()
    CARE = input("Do you accept the potential"+colorama.Fore.RED + " danger"+colorama.Fore.RESET +" ["+colorama.Fore.CYAN + "Y"+colorama.Fore.RESET + "/" + colorama.Fore.YELLOW + "N"+colorama.Fore.RESET + "] ")
    if CARE == "Y" or CARE == "y":
        cls()
        Info_Style()
        print("This test has two modes [easy mode, hard mode] for windows")
        Info_Style()
        print("But you are using linux and for linux, we just have the hard mode!")
        rmode = input("Do you wanna continue? ["+colorama.Fore.CYAN + "Y"+colorama.Fore.RESET +"/" + colorama.Fore.YELLOW + "N"+colorama.Fore.RESET + "] ")
        if rmode == "Y" or rmode == "y":
            Ransom()
        else:
            Info_Style()
            print("No problem! Going back to main menu in 6 seconds...")
            time.sleep(6)
            main_menu()
    else:
        No_Worry_Style()
        print("No need to worry, going back to the main menu...")
        time.sleep(5)
        main_menu()


def Ransom():
    # Here we try to encrypt all data in the documents folder | SO TAKE CARE #
    try:
        usr = os.getlogin()
        file = "Encrypt.py"
        cls()
        print(colorama.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀ 
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
    """)
        Info_Style()
        print("Starting the ransomware test...")
        time.sleep(6)
        try:
            finalf = "The-Bad-Guys//"+file 
            letssee = subprocess.call(["python",finalf])
            if letssee == 1 or letssee == 2:
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
                for r, d, files in os.walk("/home/"+usr+"/Documents"):
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
    except PermissionError:
            Warning_Style()
            print("The ransomware file can not be executed!")
            Great_Style()
            print("This maybe caused by your anti-virus")
            Info_Style()
            print("If that's true, your anti-virus has done great(probably with signatures)!")
            Info_Style()
            print("Going back to the main menu in 12 seconds...")
            time.sleep(12)
            main_menu()


def BrokenWall():
    # Here we test your firewall's protection | This part is not dangerous | Cause we roll back all the changes #
    try:
        Info_Style()
        print("Prerequisites: ufw installed and enabled!")
        x = input("Do you have it "+colorama.Fore.GREEN + 'installed'+colorama.Fore.RESET+" and "+colorama.Fore.CYAN + 'enabled'+colorama.Fore.RESET+"? ["+colorama.Fore.CYAN + "Y"+colorama.Fore.RESET +"/" + colorama.Fore.YELLOW + "N"+colorama.Fore.RESET + "] ")
        if x == "y" or x == "Y":
            file1 = "BrokenWall-l.sh"
            file2 = "BadExclusion-l.sh"
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
            proc = subprocess.Popen(["The-Bad-Guys//"+file1], stdout=subprocess.PIPE, shell=True)
            (res, err) = proc.communicate()
            proc = err
            if proc == 1 or proc == 2:
                Great_Style()
                print("Your anti-virus or firewall didn't allow us to turn the firewall off!")
                Info_Style()
                print("Until now it was great!")
                Info_Style()
                print("Now trying to add an exclusion to your firewall...")
                time.sleep(7)
                proc = subprocess.Popen(["The-Bad-Guys//"+file2], stdout=subprocess.PIPE, shell=True)
                (res, err) = proc.communicate()
                proc = err
                if proc == 1 or proc == 2:
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
                    print("Your firewall/anti-Virus blocked us from turning it off!")
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
                proc1 = subprocess.Popen(["The-Good-Guys//WallStatus-l.sh"], stdout=subprocess.PIPE, shell=True)
                (result, err) = proc1.communicate()
                result = str(result)
                if not "inactive" in result:
                    Warning_Style()
                    print("The backdoor was running!")
                    Great_Style()
                    print("But it was unable to turn off the firewall")
                    Info_Style()
                    print("Now trying to add an exclusion to your firewall...")
                    time.sleep(7)
                    proc = subprocess.Popen(["The-Bad-Guys//"+file2], stdout=subprocess.PIPE, shell=True)
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
                        print("You can always relay on your firewall protection! 95%")
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
                        print("You can almost relay on your firewall protection! 85%")
                        Info_Style()
                        print("Going back to main menu in 15 seconds...")
                        time.sleep(15)
                        main_menu()
                else:
                    Warning_Style()
                    print("The backdoor was running!")
                    Warning_Style()
                    print("And it was able to turn off your firewall!")
                    Info_Style()
                    print("Now trying to add an exclusion to your firewall...")
                    proc = subprocess.Popen(["The-Bad-Guys//"+file2], stdout=subprocess.PIPE, shell=True)
                    (res, err) = proc.communicate()
                    proc = err
                    time.sleep(7)
                    if proc == 1 or proc == 2:
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
                        print("And it was able to turn off your firewall")
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
                        print("And it was able to turn off the firewall")
                        Warning_Style()
                        print("Also, we were able to add an exclusion to your firewall!")
                        Info_Style()
                        print("You can never relay on your firewall protection! 5%")
                        Info_Style()
                        print("Going back to main menu in 15 seconds...")
                        time.sleep(15)
                        main_menu()
        else:
            Info_Style()
            print("To install ufw, run this command: sudo apt install ufw -y")
            Info_Style()
            print("To enable ufw, run this command: sudo ufw enable")
            Info_Style()
            print("Going back to main menu in 8 seconds...")
            time.sleep(8)
            main_menu()
    except PermissionError:
        pass

def Roll_back():
    # Roll back firewall test changes :)
    try:
        cls()
        print(colorama.Fore.GREEN + """
█▀█ █▀█ █░░ █░░ █ █▄░█ █▀▀   █▄▄ ▄▀█ █▀▀ █▄▀
█▀▄ █▄█ █▄▄ █▄▄ █ █░▀█ █▄█   █▄█ █▀█ █▄▄ █░█ ▄ ▄ ▄
""")
        Great_Style()
        print("Enabling ufw back on...")
        time.sleep(3)
        subprocess.check_output("The-Good-Guys//FirewallBack-l.sh", shell=True)
        Great_Style()
        print("Removing the backdoor from exclusions...")
        time.sleep(3)
        subprocess.check_output("The-Good-Guys//NoBackdoor-l.sh", shell=True)
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
    print(colorama.Fore.MAGENTA +"2- Test Firewall Protection | Just ufw\n")
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
        print("Going back to main menu in 6 seconds...")
        time.sleep(6)
        main_menu()


if __name__ == "__main__":
    if is_admin():
        if sys.platform == "win32":
            Warning_Style()
            print("This is the mac/linux version of the program")
            Info_Style()
            print("But your os is windows, so go and download the windows version")
            Info_Style()
            print("Exiting in 7 seconds...")
            time.sleep(7)
        else:
            main_menu()
    else:
        Error_Style()
        print("To run this python file, you need to run it as administrator/root")
        Great_Style()
        print("See you after you ran me as admin!")
        Info_Style()
        print("Exiting in 7 seconds...")
        time.sleep(7)