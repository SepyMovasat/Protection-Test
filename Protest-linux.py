# Created by @Sepy_Movasat | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" #
# Please note: Although that this is for testing purposes, It may cause file loss(if used without care)#
# JUST FOR LINUX #

import colorama as cm #Used for creating some sort of UI
import subprocess #Used for executing files a lot
import sys #Used like subprocess
import time #Used for time.sleep
import os #Used in different parts of the program 
import ctypes #Used in is_admin()
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
    if CARE == "Y" or CARE == "y":
        cls()
        Info_Style()
        print("This test has six modes for windows")
        Info_Style()
        print("But you are using linux and for linux, we just have the hard mode!")
        rmode = input("Do you wanna continue? ["+cm.Fore.CYAN + "Y"+cm.Fore.RESET +"/" + cm.Fore.YELLOW + "n"+cm.Fore.RESET + "] ")
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
        print(cm.Fore.GREEN + """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀ 
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█ ▄ ▄ ▄
    """)
        Info_Style()
        print("Starting the ransomware test...")
        time.sleep(5)
        try:
            finalf = "The-Bad-Guys/"+file 
            letssee = subprocess.call(["python3",finalf])
            time.sleep(1.5)
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
                for r, d, files in os.walk("/home/"+usr+"/Documents"):
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
        x = input("Do you have it "+cm.Fore.GREEN + 'installed'+cm.Fore.RESET+" and "+cm.Fore.CYAN + 'enabled'+cm.Fore.RESET+"? ["+cm.Fore.CYAN + "Y"+cm.Fore.RESET +"/" + cm.Fore.YELLOW + "n"+cm.Fore.RESET + "] ")
        if x == "y" or x == "Y":
            file1 = "BrokenWall-l.sh"
            file2 = "BadExclusion-l.sh"
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
            proc = subprocess.Popen(["sh ./The-Bad-Guys/"+file1], stdout=subprocess.PIPE, shell=True)
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
                proc = subprocess.Popen(["sh ./The-Bad-Guys/"+file2], stdout=subprocess.PIPE, shell=True)
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
                proc1 = subprocess.Popen(["sh ./The-Good-Guys/WallStatus-l.sh"], stdout=subprocess.PIPE, shell=True)
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
                    proc = subprocess.Popen(["sh ./The-Bad-Guys/"+file2], stdout=subprocess.PIPE, shell=True)
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
                    proc = subprocess.Popen(["sh ./The-Bad-Guys/"+file2], stdout=subprocess.PIPE, shell=True)
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
                        print(cm.Fore.YELLOW + """
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
        print(cm.Fore.GREEN + """
█▀█ █▀█ █░░ █░░ █ █▄░█ █▀▀   █▄▄ ▄▀█ █▀▀ █▄▀
█▀▄ █▄█ █▄▄ █▄▄ █ █░▀█ █▄█   █▄█ █▀█ █▄▄ █░█ ▄ ▄ ▄
""")
        Great_Style()
        print("Enabling ufw back on...")
        time.sleep(3)
        subprocess.check_output("sh ./The-Good-Guys/FirewallBack-l.sh", shell=True)
        Great_Style()
        print("Removing the backdoor from exclusions...")
        time.sleep(3)
        subprocess.check_output("sh ./The-Good-Guys/NoBackdoor-l.sh", shell=True)
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
            finalf = "The-Bad-Guys/"+file1 
            finalf2 = "The-Bad-Guys/"+file2
            letssee = subprocess.call(["python3", finalf])
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
        if os.path.isfile("The-Bad-Guys/Oh-spy.png"):
            spy1 = True
            Warning_Style()
            print("Spyware was able to take a picture from you!")
            os.remove("The-Bad-Guys/Oh-spy.png")
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
            letssee = subprocess.call(["python3", finalf2])
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
        if os.path.isfile("The-Bad-Guys//Oh-spy.wav"):
            os.remove("The-Bad-Guys//Oh-spy.wav")
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
    c1 = cm.Fore.RED + """                 .-:     .-.                 
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
@#+"""+cm.Fore.LIGHTMAGENTA_EX + "Cool" +cm.Fore.YELLOW+"""+==*@=::::::::::::::.....:....:@#++"""+cm.Fore.LIGHTMAGENTA_EX + "Pro!"+cm.Fore.YELLOW+"""+++@
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
    print(random.choice([c1,c2,c3,c4]))
    print(cm.Fore.MAGENTA + "\n1- Test Ransomware Protection\n ")
    print(cm.Fore.MAGENTA +"2- Test Firewall Protection | Just ufw\n")
    print(cm.Fore.MAGENTA + "3- Roll back firewall test changes")
    print(cm.Fore.MAGENTA + "\n4- Spyware Test(camera and microphone)")
    print(cm.Fore.MAGENTA + "\n5- Exit")
    print(cm.Fore.YELLOW + "Note: You are using linux, and for linux, lot's of tests are limited!")
    main_inp = input(cm.Fore.RESET + "Which one? ")
    if main_inp == "1":
        tell_the_danger()
    elif main_inp == "2":
        Info_Style()
        print("This test has six modes for windows")
        Info_Style()
        print("But you are using Linux, and for linux, we only have the hard mode")
        x = input("Do you wanna continue? ["+cm.Fore.CYAN + "Y"+cm.Fore.RESET +"/" + cm.Fore.YELLOW + "n"+cm.Fore.RESET + "] ")
        if x == "y" or x == "Y":
            BrokenWall()
        else:
            print("No problem! Going back to main menu in 5 seconds...")
            time.sleep(5)
            main_menu()
    elif main_inp == "3":
        Roll_back()
    elif main_inp == "4":
        Spyware_test()
    elif main_inp == "5":
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
            print("But your os is windows, so go and run the windows version")
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