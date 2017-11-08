
import os
from Algorithm import *

def clsn():

	if os.name == 'posix':
		os.system('clear')

	if os.name == 'nt':
		os.system('cls')

	return

def run():
	return

def menu_CF():

	option = ''

	#clsn()

	while option != 'exit':
	#{
		print("\n  --------------- Source Configuration ------------\n")
		
		print("\n  1. Display list")
		print("\n  2. Add")
		print("\n  3. Delete")
		print("\n\tChoose an option:")

		option = input('>> ')

		if option == '1':
			pass

		if option == '2':
			pass

		if option == '3':
			pass

		#clsn()
	#}
	return

def menu_CD():

	option = ''

	#clsn()

	while option != 'exit':
	#{
		print("\n  --------------- Destiny Configuration ------------\n")
	
		print("\n  1. Display list")
		print("\n  2. Add")
		print("\n  3. Delete")
		print("\n\tChoose an option:")

		option = input('>> ')

		if option == '1':
			pass

		if option == '2':
			pass

		if option == '3':
			pass

		#clsn()
	#}
	return

def menu_main():

	option = ''
	
	#clsn()

	while option != 'exit':
	#{
		print("\n  --------------- MENU ------------\n")
		
		print("\n  1. Source Configuration")
		print("\n  2. Destiny Configuration")
		print("\n  3. Run")
		print("\n\tChoose an option:")

		option = input('>> ')

		if option == '1':
			menu_CF()

		if option == '2':
			menu_CD()

		if option == '3':
			run()

		#clsn()
	#}
	print("\n ------ Succes ----------\n")

	return
#--------------------------------------------------------		
menu_main()