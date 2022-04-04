import threading
import win32api
import os
import cvar
from colorama import Fore

def _input_thread():
    while True:
        if (win32api.GetAsyncKeyState(ord(cvar.toggle_farm_key)) & 1) != 0:
            if cvar.farm_running:
                print(Fore.GREEN + "[+] Stopping Farm...")
            cvar.farm_running = not cvar.farm_running
        if (win32api.GetAsyncKeyState(ord(cvar.exit_program_key)) != 0):
            break
    
    print("[+] Exiting")
    print(Fore.WHITE)
    os._exit(1)

def StartInputScanThread():
    exit_thread = threading.Thread(target=_input_thread)
    exit_thread.start()