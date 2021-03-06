# Elden Ring Bird Autofarm
![img](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![img](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)
![img](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
### Requirements
```
Python 3.0+ w/ Pip
coloram>=0.4.4+
pynput>=1.7.6
pywin32>=303
six>=1.16.0
```
### How To Use
1) Download as .ZIP from GitHub 
2) Open the program using RUN.bat
4) When loaded, go into elden ring and teleport to the "Palace Approach Ledge-Road" site of grace **DO NOT MOVE YOUR MOUSE**
5) Ensure that you only have your bow equipped, the arrows are in the correct slot and that it is being held with both hands. 
6) Press the farm toggle key around 0.5s after the "Mohgwyn Palace" text appears (after traveling to site of grace) 
7) Sit back, relax and enjoy the ruins
### Tutorial
![img](tutorial.gif)
### Notes
- Tested using the default Longbow
- Tested using Camera Speed of 7 Mouse Sensitivity of 5
- Tested with Fullscreen 1920x1080p
- Mouse DPI shouldn't matter
- Tested on Windows 10 21h1
- The script rest's at the grace nearby to refill arrows (must have auto refill for arrows on) every *rest_at_grace_interval* (config.ini) amount of birds killed
- If timing is off / you're shooting the bird and missing edit *load_time* (config.ini)
 ### Todo
 - [x] Use F then E then E instead of using keys and mouse to travel back to grace. (Access sites of grace menu)
 - [x] Automatic arrow refilling
