import time
import colorama
import win32api
import threading
import os
import pynput 
from player import Player
from colorama import Fore, Back, Style

run = False
mouse = pynput.mouse.Controller()
game_player = Player()

colorama.init()

def exit_function():
    global run
    while True:
        if (win32api.GetAsyncKeyState(ord('O')) & 1) != 0:
            run = not run
            print(Fore.GREEN + '[+] Farm is now ' + ('started' if run else 'stopped'))
        if (win32api.GetAsyncKeyState(ord('H')) != 0):
            break
    print("[+] Exiting")
    print(Fore.WHITE)
    os._exit(1)

x = threading.Thread(target=exit_function)
x.start()

print(Fore.BLUE + "[+] Welcome to Elden Ring bird farm\n")
print(Fore.CYAN + "[+] Travel to the \"Palace Approach Ledge-Road\" site of grace")
print("[+] Press 'H' at any time to exit")
print("[+] Press 'O' to start the farm\n")

run = False 

while True:
    if run:
        game_player.MoveMouse(-1700)                        #moving mouse toward cliff
        game_player.MoveForward(1.3)                        #walking to cliff 
        game_player.MoveMouse(-480, 450)                    #moving mouse toward bird
        time.sleep(0.2)                                     #waiting for bird to appear / error handling
        game_player.AimAndShoot(0)                          #aim and shoot bird
        time.sleep(6)                                       #waiting for combat timer to open map
        game_player.OpenMap()                               #open map
        time.sleep(0.2)                                     #error handling
        game_player.OpenSitesOfGrace()                      #open sites of grace
        game_player.Select()                                #select grace
        time.sleep(0.1)                                     #error handling
        game_player.Select()                                #teleport grace
        time.sleep(5.5)                                     #waiting for loading and respawn

        print(Fore.CYAN + "[+] Ready to farm")
    