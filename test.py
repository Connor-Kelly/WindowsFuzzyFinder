# from subprocess import Popen, PIPE, STDOUT

# p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
# grep_stdout = p.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
# print(grep_stdout.decode())

# import subprocess

# # windows=$(py getAllWindows.py)


# windows = 'getAllWindows.py - WindowFuzzyFinder - Visual Studio Code\nsubprocess  Subprocess management  Python 3.11.5 documentation  Mozilla Firefox\nTask Manager\nMail\nInbox - Rice Student - Mail\nSettings\nSettings\neM Client\nLenovoWidget\nOpenVPN GUI\nWindows Input Experience\ngrandson - WWIII\nResume V2-12.pdf - Foxit PDF Reader\nhttps://discord.com/app?_=1693160430714 - Discord\nWindows PowerShell\nProgram Manager'


# # echo -e $windows | fzf

# subprocess.run(['echo', '-e', windows, '|', 'fzf'], capture_output=True)


import pyautogui
import os
import subprocess
import ctypes
from ctypes import wintypes
import time
# These SW_ constants are used for ShowWindow() and are documented at
# https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-showwindow#parameters
SW_MINIMIZE = 6
SW_MAXIMIZE = 3
SW_HIDE = 0
SW_SHOW = 5
SW_RESTORE = 9

enumWindows = ctypes.windll.user32.EnumWindows
enumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
# ctypes.windll.user32.EnumWindows()
# def getAllWindows():
windows = pyautogui.getAllWindows()
# windowsList = list(filter(lambda s: s != "", map(lambda w: w.title, windows)))
# windowsStrings = '\n'.join(windowsList)
# print(repr(windowsStrings))
# print(windowsStrings)
for w in windows:
    if "Resume" in w.title:
        print(f'showing window\n\ttitle: {w.title}\n\thWnd: {w._hWnd}')
        print(f'ret: {ctypes.windll.user32.ShowWindow(w._hWnd, SW_RESTORE)}')
        # print(f'ret: {ctypes.windll.user32.ShowWindow(w._hWnd, SW_SHOW)}')
        print(f'ret: {ctypes.windll.user32.SetForegroundWindow(w._hWnd)}')

# print(ctypes.windll.user32.GetActiveWindow())
# print(repr(windowsStrings.encode(encoding='ascii', errors="ignore").decode())[1:-1])

# def getAllWindows():
#     """Returns a list of Window objects for all visible windows.
#     """
#     windowObjs = []
#     def foreach_window(hWnd, lParam):
#         if ctypes.windll.user32.IsWindowVisible(hWnd) != 0:
#             windowObjs.append((hWnd, lParam))
#         return True
#     enumWindows(enumWindowsProc(foreach_window), 0)

#     return windowObjs

# print(getAllWindows())