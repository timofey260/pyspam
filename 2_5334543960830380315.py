import pyautogui
import time
b = input('text: ')
n = int(input('num of messages: '))
time.sleep(5)
f = range(0, n)

for i in f:
    print((i + 1), ' message send!')
    pyautogui.write(b)
    pyautogui.press('enter')
