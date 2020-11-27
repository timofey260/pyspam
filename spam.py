import pyautogui
import time
from banner import b
from colorama import Fore, init
init(Fore)

print(Fore.RED + b)
print(Fore.GREEN + 'text: ' + Fore.RED)
b = input()
print(Fore.GREEN + 'num of messages: ' + Fore.RED)
n = int(input())
time.sleep(3)
f = range(0, n)
print(Fore.YELLOW + "wait.")
time.sleep(0.5)
print(Fore.YELLOW + "wait..")
time.sleep(0.5)
print(Fore.YELLOW + "wait...")
for i in f:
    print(Fore.GREEN + '%1d message send!' %(i + 1))
    pyautogui.write(b)
    pyautogui.press('enter')

pyautogui.alert('succefuly send %2d messages!' % n)
