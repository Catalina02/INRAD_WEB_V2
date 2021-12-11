#DURANTE EL DESARROLLO
##1
###Iniciar el entorno virtual

./mivir/Scripts/Activate.ps1

##2
###Ejecutar las Migraciones

python manage.py makemigrations 
\textcolor{gray}{si no sirve, ocupar}
\textcolor{gray}{python manage.py migrate --run-syncdb 
}
python manage.py migrate
# INRAD_WEB_V2
