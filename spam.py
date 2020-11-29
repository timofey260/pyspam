'''
Made by Timofey
Discord: TiMoFey#5066
Github: https://github.com/timofey260/pyspam
site: https://timofey26s.tilda.ws
Errors:
	1. FileError: file not found!
	2. NumError: {num} not a number!
	3. IndexError: index out of range!
	4. TypeError: {str} is not 1,2 or 3!
	5. ErrorError: Error not found! correct def error()

'''
import pyautogui
from time import sleep # sleep block on load{wait...}
from colorama import Fore, init # for colored text
from os import system # system use for clear messages
init(Fore) # colorama init
uns = ''  #unuse str. uses for def error()
b = ('_____   +                     \n'
     '  |           /\\      /\\    \n'
     '  |     |    /  \\    /  \\   \n'
     '  |     |   /    \\  /    \\  \n'
     '  |     |  /      \\/      \\ \n'
     '========spam_programm=======  \n')        # menu
print(Fore.RED + b)
def error(num, result): # errors: easy moding
	if num == 1:
		print('FileError: file not found!')
		input()
	elif num == 2:
		print('NumError: %1s not a number!' %(result))
		input()
	elif num == 3:
		print('IndexError: index out of range!')
		input()
	elif num == 4:
		print('TypeError: %1s is not 1,2 or 3!' %(result))
		input()
	else:
		print('ErrorError: Error not found! correct def error()')
		input()
	exit()


print(Fore.YELLOW + "[" + Fore.CYAN + "1" + Fore.YELLOW + "]file")    		#menu buttons
print(Fore.YELLOW + "[" + Fore.CYAN + "2" + Fore.YELLOW + "]message")
print(Fore.YELLOW + "[" + Fore.CYAN + "3" + Fore.YELLOW + "]exit")
name = input('>>> ') # name: 1, 2 or 3(int)
st = 0
if name == '1':
	f = input("file name: ") #f - filename(str)
	print(Fore.GREEN + 'num of messages(you can use"all"): ' + Fore.RED)
	
	sta = input() # sta - num of messages(int or str('all'))
	if sta == 'all':
		num = 0 # num - index of file(int)
		fil = f + ".txt" # file.txt
		try: # errorfind
			file = open(fil, 'r', encoding = 'utf-8').readlines() # open file for 'all'
		except:
			error(1, uns)
		filew = file
	elif sta != 'all':
		
		try: # errorfind
			sta = int(sta) # sta - num of messages(int or str('all'))
		except:
			error(2, sta)
		num = 0
		fil = f + ".txt"
		try: # errorfind
			file = open(fil, 'r', encoding = 'utf-8').readlines() #open file for 'slice'
			
		except:
			error(1, uns)
		if sta > len(file):
			error(3, uns)
		filew = file[:sta] #slice of file
	
	sleep(4)     # wait...
	system('cls||clear') # cls

	print(Fore.YELLOW + b +"\nwait.  ")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + b +"\nwait.. ")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + b +"\nwait...")
	system('cls||clear')
	for a in filew:							   # spam messages in file
			print(Fore.GREEN + '%1d message send!' %(num + 1)) # print messages in screen
			pyautogui.write(a)									
			num = num + 1

	print('=====process=====')
	print(b, '\ntimes: %1s' %(len(filew)))
	pyautogui.alert('succefuly send %2d messages!' %(len(filew))) # result
elif name == '2':
	print(Fore.RED + b)
	print(Fore.GREEN + 'text: ' + Fore.RED)
	g = input()
	print(Fore.GREEN + 'num of messages: ' + Fore.RED)

	try: # errorfind
		n = int(input())
	except:
		error(2, n)
	sleep(4)    # wait...
	f = range(n)
	system('cls||clear') # cls

	print(Fore.YELLOW + b +"\nwait.  ")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + b +"\nwait.. ")
	sleep(0.5)
	system('cls||clear')

	print(Fore.YELLOW + b +"\nwait...")
	system('cls||clear')

	print('=====process=====')
	print(b, '\nmessage: %1s\ntimes: %1s' %(g, n))
	for i in f:												# spam messages
	    print(Fore.GREEN + '%1d message send!' %(i + 1)) # print messages in screen
	    pyautogui.write(g)
	    pyautogui.press('enter')

	pyautogui.alert('succefuly send %2d messages!' %(n)) # result
elif name == '3':
	exit()
else:
	error(4, name)
