# importamos el conector
import mysql.connector as db

##### PARTE 1: CREAR UNA BASE DE DATOS LLAMADA TALLER2 #####

# creamos una conexión con el motor MySQL. AQUI DEBEN PONER LOS DATOS DE SU MYSQL
mydb = db.connect(
 host = 'localhost',
 user = 'root',
 passwd = 'piriro',
 database = ''
)
# usando la conexión creamos un cursor
my_cursor = mydb.cursor()

# cargamos en una variable la sentencia SQL para crear la nueva base de datos
sqlsentence = 'CREATE DATABASE Taller2'

# ejecutamos la sentencia que crea la base de datos
my_cursor.execute(sqlsentence)