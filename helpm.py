def help_menu():

	option = ''

	print("\n  --------------- Help ------------\n")
		
	with open('help.txt', 'r') as fin:
		print (fin.read())

	while option != 'b':
	#{
		print("\n\tTo go back type 'b'")
		option = input('>> ')
		option = option.lower()
	#}