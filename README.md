# PASOS PARA DESPLEGAR EL PROYECTO

En la terminal con el proyecto abierto, crear el entorno virtual con el siguiente comando (Windows):

py -m venv env

Este demorara unos segundos, una vez hecho activar el entorno virtual con el siguiente comando (Windows):

env\Scripts\activate

Si este paso salio bien, a la izquierda de la raiz del proyecto deberia aparecer el siguiente mensaje: (env)
Este indica que esta activado el entorno virtual

Ahora tenemos que instalar los frameworks que se usan en el proyecto, estos se encuentran en el archivo "requirements.txt" y se instala todo con un comando(Funcionan de igual manera en Linux y Windows):

pip install -r requirements.txt

Como paso final para ejecutar el proyecto, correr la aplicacion con el comando:

py ./main.py

Este le dara una direccion IP, la cual tendra que copiar y buscar en algun navegador web, donde se vera el proyecto funcionando.