import os
from shutil import copy

#------------------------------  Load Lists  -------------------------------
def load_list_from_dir(path, dir_list):
	# Load_list_from_dir carga una lista a partir de un archivo
	try:	
		with open(path, "r") as f:	# abre el archivo que recive
		    dir_list = [line.rstrip('\n') for line in f]	# crea una lista por por cada linea del .cfg

		f.close()

		return dir_list

	except:		# si el archivo no existe se crea uno nuevo en es adireccion, se regresa una lista vacia
		print("\n ERROR: Source/Destiny file can't be found at: ", path)
		print('\n A Source file was generated...')
		f = open(path,'w+')
		f.close()

		return dir_list	

def load_sc(sc_list):

	#print("\n Loading SC...")

	path = os.path.dirname(os.path.abspath(__file__)) # obtiene la direccion del .py
	path = path + '\data\sc.cfg'

	return load_list_from_dir(path, sc_list)

def load_ds(ds_list):

	#print('\n Loading DS...')

	path = os.path.dirname(os.path.abspath(__file__)) # obtiene la direccion del .py
	path = path + '\data\ds.cfg'
	
	return load_list_from_dir(path, ds_list)

#-------------------------------  Find-Copy  -------------------------------
def check_file(file, ds_list):

	# Check_file revisa que el nombre del archivo tenga una palabra clave

	for destiny in ds_list:	# recorre la lista de direcciones destino
		aux = destiny.split('||')	# Separa la direccion de la lista de palabras           # aux[0] = direccion     aux[1] = lista de palabras clave
		keywords = aux[1].split(',')	# crea la lsita de palabras clave

		for kw in keywords:			# recorre la lsita de palabras clave
			if kw in file:				# si la el archivo contiene la plabra clave regresa la direccion aux[0]
				return [aux[0]] 

	return []	# si no se encontraron coincidencias se regresa una lista vacia

def search_files(sc_list, ds_list):

	# Search_files recorre la lista de direcciones, de donde saca una lista de archivos por cada direccion
	# Recorre la lista de archivos por direccion y si tiene una palabra clave mueve el archivo
	# Para mover el archivo lo copia a la direccion destino y borra el del directorio origen
	
	for src in sc_list:	#saca una direccion de la lista

		try:
			file_list = os.listdir(src)	# crea una lista de los archivos en esa direccion
			
			for file in file_list:	# selecciona un archivo de la lista de archivos
				if os.path.isfile(src + '/' +file):	# revisa que file sea un archivo y no una carpeta
					dst = check_file(file, ds_list)	# revisa que el archivo contenga una palabra clave

					try:
						if dst != []:	# si la lista dst esta vacia no hubo coincidencia y el archivo no se mueve
							try:	
								if os.path.isdir(dst[0]):	# revisa que la direcion destino sea valida
									abs_src = src + '/' + file  # la direccion source tiene que ser la direccion absoluta de la archivo (C:\docs + \+ file.txt)
									copy(abs_src, dst[0])		# se copia a la direcion de destino
									os.remove(abs_src)			# se borra el archivo en la carpeta origen
							except:
								print("\n ERROR: Invalid Destiny folder: ", dst[0])

					except:
						print("\n The following file wasn't moved: ", file)
				else:
					pass
		except:
			print("\n ERROR: Invalid Source folder: ", src)

#-----------------------------  Display SRC List  -------------------------------
def display_scList(sc_list):
	i = 1

	print('\n  Lista de rutas origen:')

	for rute in sc_list:
		print('\n\t' + str(i) + '. ' + rute)
		i+=1

	return

#-----------------------------  Display DST List  -------------------------------
def display_dsList(ds_list):
	i = 1

	print('\n  Lista de rutas destino:')

	for line in ds_list:
		rute_kw = line.split('||')

		print('\n\t' + str(i) + '. ' + rute_kw[0])
		print('\t  Palabras clave: ' + rute_kw[1])

		i+=1

	return


#-----------------------------  Update Files  ----------------------------------
def update_file(list, file_name):
	path = os.path.dirname(os.path.abspath(__file__)) # obtiene la direccion del .py
	path = path + '/Data' + file_name
	
	try:
		open()
	except:
		print('')
#-----------------------------  ADD SRC  -----------------------------------
def add_src(sc_list):

	new_path = input('\n Introduce la nueva ruta:')

	sc_list.append(new_path)

	return

#-----------------------------  ADD DS  -----------------------------------
def add_ds(ds_list):

	rute = input('\n Introduce la nueva ruta:')

	words = input('\n Introduce las palabras clave')

	new_path = rute + '||' + words

	ds_list.append(new_path)

	return

#-----------------------------  Main -------------------------------
def main():
	# Sc_list = source list
	# ds_ list = destiny list
	sc_list = []
	ds_list = []

	# carga los archivos .cfg de donde saca las listas de direcciones
	sc_list = load_sc(sc_list)	
	ds_list = load_ds(ds_list)

	# llamada  afunciones
	#display_scList(sc_list)
	#display_dsList(ds_list)
	#search_files(sc_list, ds_list)
#---------------------------------

main()