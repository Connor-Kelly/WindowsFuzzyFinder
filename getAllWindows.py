import pyautogui
import os
import subprocess

# def getAllWindows():
windows = pyautogui.getAllWindows()
windowsList = list(filter(lambda s: s != "", map(lambda w: w.title, windows)))
windowsStrings = '\n'.join(windowsList)
# print(repr(windowsStrings))
# print(windowsStrings)
print(repr(windowsStrings.encode(encoding='ascii', errors="ignore").decode())[1:-1])


# print('---')

# print('attempting fzf')
# out = os.system('fzf')
# out = subprocess.check_output(['echo', windowsStrings, '|', 'less'],
                            #   stdin=subprocess.PIPE)
# child = subprocess.Popen(['fzf'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# child = subprocess.Popen(['cat', 'testWindows', '|', 'fzf'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# out = child.stdout.read()
# print(f'Selected: ${out}')
# print(out[0:3])
# print(repr(out))
# for x in windows:  
#     print(repr(x.title))

