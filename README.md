############ Instalacion

Python 3.5.6

verificr tener instalacion 

Donde vas a guardar tu proyecto, guarda la carpeta python, y dentro de ella ejecuta python virtualenv venv
Entrar a la carpeta (venv) y buscar la subcarpeta /Scripts/activate.bat (Ejecutar el activate.bat)
Luego volvemos a la carpeta Python y ejecutamos el comando
pip install -r requirements.txt
Cuando termine de instalar las librerias, vamos al archivo servicio.py de la carpeta Python y lo ejecutamos
Escucha por el puerto 5000 y la URL es localhost (http://localhost:5000)

Abre el proyecto SOAP UI Y EJECUTA el metodo Create

###### URL

http://127.0.0.1:5000/create

###### POST

{
	"data":
	[
		{"value":"70,84,85"},
		{"value":"70,84,78,80"},
		{"value":"70,84,78,76"},
		{"value":"70,49,54,51"},
		{"value":"70,49,37,40"},
		{"value":"70,49,37,22"}
	]
}

###### Headers

Content-Type : application/json

###### Response

{
	"5Arbol"
}


###### URL

http://127.0.0.1:5000/ancestro

##### GET

?arbol=5Arbol&abs1=40&abs2=78

###### Headers

Content-Type : application/json


###### RESPONSE

{
	"70"
}


EN la raiz de ls carpeta hay dos carpetas

#
/files guarda el arbol del create

ejemplo /files/5arbol

/graphs guarda el arbol ya con conexiones

ejemplo. /graphs/5Arbol

el ancestro solo lo devuelve el calculo del servicio
