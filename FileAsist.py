
import os
from Algorithm import *
from helpm import *

def clsn():

	if os.name == 'posix':
		os.system('clear')

	if os.name == 'nt':
		os.system('cls')

	return

def run(sc_list, ds_list):
	
	search_files(sc_list, ds_list)

	return

def menu_CF(sc_list, ds_list):

	option = ''

	clsn()

	while option != 'exit':
	#{
		print("\n  --------------- Source Configuration ------------\n")
		
		print("\n  1. Display list")
		print("\n  2. Add")
		print("\n  3. Delete")
		print("\n\tChoose an option:")

		option = input('>> ')

		if option == '1':
			clsn()
			display_scList(sc_list)

		if option == '2':
			clsn()
			add_src(sc_list)

		if option == '3':
			clsn()
			display_scList(sc_list)
			del_sc(sc_list)

		#clsn()
	#}
	return

def menu_CD(sc_list, ds_list):

	option = ''

	clsn()

	while option != 'exit':
	#{
		print("\n  --------------- Destiny Configuration ------------\n")
	
		print("\n  1. Display list")
		print("\n  2. Add")
		print("\n  3. Delete")
		print("\n\tChoose an option:")

		option = input('>> ')

		if option == '1':
			clsn()
			display_dsList(ds_list)

		if option == '2':
			clsn()
			add_ds(ds_list)

		if option == '3':
			clsn()
			display_dsList(ds_list)
			del_ds(ds_list)

		#clsn()
	#}
	return

def menu_main(sc_list, ds_list):

	option = ''
	
	clsn()

	while option != 'exit':
	#{
		print("\n  //////// File Orginizer \\\\\\\\\\\\\\ \n")
		
		print("\n  1. Source Configuration")
		print("\n  2. Destiny Configuration")
		print("\n  3. Run")
		print("\n  To exit type 'exit', for help type 'help'")
		print("\n\tChoose an option:")

		option = input('>> ')

		if option == '1':
			menu_CF(sc_list, ds_list)

		if option == '2':
			menu_CD(sc_list, ds_list)

		if option == '3':
			run(sc_list, ds_list)

		if option == "help":
			help_menu()

		clsn()
	#}
	print("\n ------ Succes ----------\n")

	return
#--------------------------------------------------------		

def main():
	sc_list = []
	ds_list = []

	# carga los archivos .cfg de donde saca las listas de direcciones
	sc_list = load_sc(sc_list)	
	ds_list = load_ds(ds_list)

	menu_main(sc_list, ds_list)

#---------------
main()