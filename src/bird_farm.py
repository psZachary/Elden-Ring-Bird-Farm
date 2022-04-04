import time
import init
import cvar
from player import Player
from colorama import Fore

init.Initialize()

game_player = Player()

print(Fore.BLUE + "[+] Elden Ring Bird Auto Farm\n")
print(Fore.CYAN + "[+] Travel To The \"Palace Approach Ledge-Road\" Site Of Grace")
print(Fore.CYAN + "[+] Press '" + cvar.exit_program_key + "' At Any Time To Exit")
print(Fore.CYAN + "[+] Press '" + cvar.toggle_farm_key  + "' To Start The Farm\n")

def Farm():
    if False == game_player.MoveMouse(-1700): return            #moving mouse toward cliff
    if False == game_player.MoveForward(1.3): return            #walking to cliff 
    if False == game_player.MoveMouse(-480, 450): return        #moving mouse toward bird
    time.sleep(0.2)                                             #waiting for bird to appear / error handling
    if False == game_player.AimAndShoot(0): return              #aim and shoot bird
    time.sleep(6)                                               #waiting for combat timer to open map
    if False == game_player.OpenMap(): return                   #open map
    print(Fore.CYAN + "[+] Killed Bird")                        #bird is dead, map is opened
    time.sleep(0.2)                                             #error handling
    if False == game_player.OpenSitesOfGrace(): return          #open sites of grace
    if False == game_player.Select(): return                    #select grace
    time.sleep(0.1)                                             #error handling
    if False == game_player.Select(): return                    #teleport grace
    time.sleep(float(cvar.load_time))                           #waiting for loading and respawn
    print(Fore.CYAN + "[+] Finished Loading")                   #back at start of grace, finished loading

while True:
    if cvar.farm_running:
        print(Fore.GREEN + "[+] Starting Farm")
        Farm()
        print(Fore.GREEN + "[+] Stopped Farm")
        
    