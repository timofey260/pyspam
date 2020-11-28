import pyautogui
from time import sleep
from colorama import Fore, init
from os import system
init(Fore)
b = ('_____   +                     \n'
     '  |           /\\      /\\    \n'
     '  |     |    /  \\    /  \\   \n'
     '  |     |   /    \\  /    \\  \n'
     '  |     |  /      \\/      \\ \n'
     '========spam_programm=======  \n')

name = input("file[f] or message[m]")
st = 0
if name == 'f':
	f = input("file name: ")
	print(Fore.GREEN + 'num of messages(you can use"all"): ' + Fore.RED)
	
	sta = input()
	if sta == 'all':
		num = 0
		fil = f + ".txt"
		try:
			file = open(fil, 'r', encoding = 'utf-8').readlines()
		except:
			print('Error: file not found!')
			input()
		filew = file
	elif sta != 'all':
		
		try:
			sta = int(sta)
		except:
			print('error: %1s not a number!' %(sta))
			input()
		num = 0
		fil = f + ".txt"
		try:
			file = open(fil, 'r', encoding = 'utf-8').readlines()
			
		except:
			print('Error: file not found!')
			input()
			pass
		if sta > len(file):
			print('Error: index out of range!')
			input()
			exit()
		filew = file[:sta]
	
	
	
	print(b)
	sleep(4)
	system('cls||clear')

	print(Fore.YELLOW + "wait.")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + "wait..")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + "wait...")
	system('cls||clear')
	for a in filew:
			print(Fore.GREEN + '%1d message send!' %(num + 1))
			pyautogui.write(a)
			num = num + 1

	print('=====process=====')
	print(b, '\ntimes: %1s' %(sta))
	pyautogui.alert('succefuly send %2d messages!' %(sta))
elif name == 'm':
	print(Fore.RED + b)
	print(Fore.GREEN + 'text: ' + Fore.RED)
	g = input()
	print(Fore.GREEN + 'num of messages: ' + Fore.RED)

	try:
		n = int(input())
	except:
		print('error: %1s not a number!' %(n))
		input()
	print(b)
	sleep(4)
	f = range(n)
	system('cls||clear')

	print(Fore.YELLOW + "wait.")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + "wait..")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + "wait...")
	system('cls||clear')

	print('=====process=====')
	print(b, '\nmessage: %1s\ntimes: %1s' %(g, n))
	for i in f:
	    print(Fore.GREEN + '%1d message send!' %(i + 1))
	    pyautogui.write(g)
	    pyautogui.press('enter')

	pyautogui.alert('succefuly send %2d messages!' %(n))

else:
	print('ErrorType: %1s is not f or m!' %(name))
	input()
	pass
