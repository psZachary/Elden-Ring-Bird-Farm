import colorama
from input_threading import StartInputScanThread

def Initialize():
    colorama.init()
    StartInputScanThread()
