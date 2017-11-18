def help_menu():

	option = ''

	print("\n  --------------- Help ------------\n")
		
	with open('help.txt', 'r') as fin:
		print (fin.read())
	while option != 'exit':
	#{
		option = input('>> ')
	#}