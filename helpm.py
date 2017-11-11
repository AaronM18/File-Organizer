def help_menu():

	option = ''

	print("\n  --------------- Help ------------\n")
		
	with open('README.txt', 'r') as fin:
		print (fin.read())
	while option != 'exit':
	#{
		option = input('>> ')
	#}