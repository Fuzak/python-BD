# importar el conector
import mysql.connector as db

# crear una nueva conexión con la base de datos InfoAeropuertos
mydb = db.connect(
 host = 'localhost',
 user = 'root',
 passwd = 'piriro',
 database = 'infoaeropuertos'
)

# usando la conexión crear un cursor
my_cursor = mydb.cursor()

# cargar en una variable la sentencia SQL para agregar varias filas en tabla Aeropuertos
sqlSentence = 'INSERT INTO aeropuertos(id, ident, type, name, elevation_ft, municipality, iata_code, score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

# cargar en una variable las tuplas a agregar
filas = [
 ('39340', 'SHCC', 'heliport', 'Clinica Las Condes Heliport', '2461', 'Santiago','', '25'),
 ('39379', 'SHMA', 'heliport', 'Clinica Santa Maria Heliport', '2428', 'Santiago','', '25'),
 ('39390', 'SHPT', 'heliport', 'Portillo Heliport', '9000', 'Los Andes','', '25')
]

#ejecutar la sentencia que agrega las filas con executemany
my_cursor.executemany(sqlSentence, filas)

# Se guardan las filas creadas en la BD
mydb.commit()


