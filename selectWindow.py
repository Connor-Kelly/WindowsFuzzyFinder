import pyautogui
import sys
import ctypes
import os
args = sys.argv[1:]
print(f'args: {args}')

SW_MINIMIZE = 6
SW_MAXIMIZE = 3
SW_HIDE = 0
SW_SHOW = 5
SW_RESTORE = 9

def getWindowWithTitle(title):
    windows = pyautogui.getAllWindows()
    for w in windows:
        if w.title.encode(encoding='ascii', errors="ignore").decode() == title:
            return w
    return None
    

currentWindow = pyautogui.getActiveWindow()
print(f'current window: title: {currentWindow.title} | hWnd: {currentWindow._hWnd}')
print(f'currentPID: {os.getpid()}')
# GetConsoleWindow()
curHwnd = ctypes.windll.kernel32.GetConsoleWindow()
print(f'currentHwnd: {curHwnd}')

if len(args) > 0: 
    w = getWindowWithTitle(args[0])
    if w != None:
        restoreVal = ctypes.windll.user32.ShowWindow(curHwnd, SW_RESTORE)
        print(f'restoreVal: {restoreVal}')
        showVal = ctypes.windll.user32.ShowWindow(curHwnd, SW_SHOW)
        print(f'showVal: {showVal}')
        setFGVal =  ctypes.windll.user32.SetForegroundWindow(curHwnd)
        print(f'setFGVal: {setFGVal}')
        allowFGSet =  ctypes.windll.user32.AllowSetForegroundWindow(curHwnd)
        print(f'allowFGSet: {allowFGSet}')
        print('---')
        print(f'window title: {w.title} | _hWnd: {w._hWnd}')
        restoreVal = ctypes.windll.user32.ShowWindow(w._hWnd, SW_RESTORE)
        print(f'restoreVal: {restoreVal}')
        showVal = ctypes.windll.user32.ShowWindow(w._hWnd, SW_SHOW)
        print(f'showVal: {showVal}')
        setFGVal =  ctypes.windll.user32.SetForegroundWindow(w._hWnd)
        print(f'setFGVal: {setFGVal}')


    # windows = pyautogui.getWindowsWithTitle(args[0])
    # # windows = pyautogui.getAllWindows()
    # print(windows)
    # if len(windows) > 0:
    #     w = windows[0]
    #     # try:
    #     # print(f'window title: {w.title} | _hWnd: {w._hWnd}')
    #     restoreVal = ctypes.windll.user32.ShowWindow(curHwnd, SW_RESTORE)
    #     print(f'restoreVal: {restoreVal}')
    #     showVal = ctypes.windll.user32.ShowWindow(curHwnd, SW_SHOW)
    #     print(f'showVal: {showVal}')
    #     setFGVal =  ctypes.windll.user32.SetForegroundWindow(curHwnd)
    #     print(f'setFGVal: {setFGVal}')
    #     allowFGSet =  ctypes.windll.user32.AllowSetForegroundWindow(curHwnd)
    #     print(f'allowFGSet: {allowFGSet}')
    #     print('---')
    #     print(f'window title: {w.title} | _hWnd: {w._hWnd}')
    #     restoreVal = ctypes.windll.user32.ShowWindow(w._hWnd, SW_RESTORE)
    #     print(f'restoreVal: {restoreVal}')
    #     showVal = ctypes.windll.user32.ShowWindow(w._hWnd, SW_SHOW)
    #     print(f'showVal: {showVal}')
    #     setFGVal =  ctypes.windll.user32.SetForegroundWindow(w._hWnd)
    #     print(f'setFGVal: {setFGVal}')
    #         # windows[0].restore()
            # windows[0].activate()
        # except:
        #     print("An exception occurred")

