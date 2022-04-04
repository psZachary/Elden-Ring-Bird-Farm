from dis import show_code
from faulthandler import dump_traceback
import direct_keyboard
import time
import pynput 
import win32api
import win32con
from direct_keyboard import KEYS 

_mouse = pynput.mouse.Controller()


class Player:    
    def __PressExtended(self, key, duration):
        direct_keyboard.PressKey(key)
        time.sleep(duration)
        direct_keyboard.ReleaseKey(key)
    def OpenMap(self):
        self.__PressExtended(KEYS.DIK_G, 0.05)
    def OpenSitesOfGrace(self):
        self.__PressExtended(KEYS.DIK_F, 0.05)
    def Select(self):
        self.__PressExtended(KEYS.DIK_E, 0.05)
    def MoveForward(self, duration=0):
        self.__PressExtended(KEYS.DIK_W, duration)
    def MoveLeft(self, duration=0):
        self.__PressExtended(KEYS.DIK_A, duration)
    def MoveRight(self, duration=0):
        self.__PressExtended(KEYS.DIK_D, duration)
    def MoveBackward(self, duration=0):
        self.__PressExtended(KEYS.DIK_S, duration)
    def Aim(self, duration=0):
        _mouse.press(pynput.mouse.Button.right)
        time.sleep(duration)
        _mouse.release(pynput.mouse.Button.right)
    def Shoot(self):
        _mouse.press(pynput.mouse.Button.left)
        time.sleep(0.2)
        _mouse.release(pynput.mouse.Button.left)
    def AimAndShoot(self, duration):
        _mouse.press(pynput.mouse.Button.right)
        time.sleep(duration)
        self.Shoot()
        time.sleep(1)
        _mouse.release(pynput.mouse.Button.right)
    def MoveMouse(self, x=0, y=0):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
