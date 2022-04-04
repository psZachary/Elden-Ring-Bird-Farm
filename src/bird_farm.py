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
        time.sleep(5.5)                                     #waiting for combat timer to open map
        
        #at this point any mouse movement will reset the mouse position on the menu (center it) we need to center it for further use
        game_player.MoveMouse(20, 20)

        time.sleep(0.5)                                     #error handling 
        game_player.OpenMap()                               #open map
        time.sleep(0.2)                                     #error handling
        game_player.MoveRight(0.05)                         #moving to grace on map
        time.sleep(0.3)                                     #error handling
        game_player.Aim(0.01)                               #open grace menu
        game_player.MoveMouse(30, -30)                      #moving mouse to travel button
        game_player.Shoot()                                 #click travel button
        time.sleep(0.5)                                     #error handling 
        game_player.MoveMouse(-100, 50)                     #moving mouse to travel confirmation button
        time.sleep(0.1)                                     #error handling
        game_player.Shoot()                                 #click travel confirmation button
        time.sleep(5.5)                                     #waiting for loading and respawn
        
        print(Fore.CYAN + "[+] Ready to farm")
    