	

------------------------------------------   FILE ORGANIZER  ------------------------------------------


Funcionamiento General:
	
	En la carpeta data se pueden encontrar 2 archivos .cfg:

	-> sc.cfg:	guarda las rutas donde el programa va a revisar los archivos contenidos

		EJEMPLO:
			C:\Users\Usser\Descargas

	-> ds.cfg:	guarda las rutas donde el programa va a mover los archivos a partir de palabras clave 
				especificas por ruta
				Por linea debe haber una ruta con una separacion '||' entre las palabras clave separadas 
				por una coma ','

		EJEMPLO:
			C:\Users\juan\Documents\||juan,clave2,clave3
			C:\Users\pedro\Documents\||pedro,claveA,claveB
			C:\Users\oscar\Documents\||oscar,clave0,clave9

					ruta||palabra1,palabra2,palabra3


Agregar:

	->SC: se introduce una nueva ruta de donde se van a mover archivos

		EJEMPLO: 
			>> C:\Users\Usser\Descargas
	
	->DS: se introduce una nueva ruta de donde se van a mover archivos, despues se pide enlistar las
		palabras clave

		EJEMPLO:
			>> C:\Users\Usser\Descargas
			>> clave1,calve2,clave3

