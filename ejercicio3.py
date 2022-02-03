# importamos el conector
import mysql.connector as db

##### PARTE 3: AGREGAR DATOS EN LAS TABLAS #####

# creamos una nueva conexión con la base de datos creada. LLENAR CON LOS DATOS DE SU MYSQL
mydb = db.connect(
 host = 'localhost',
 user = 'root',
 passwd = 'piriro',
 database = 'taller2'
)
# usando la conexión creamos un cursor
my_cursor = mydb.cursor()

# cargamos en una variable la sentencia SQL para agregar varias filas en tabla Editoriales
sqlSentence = 'INSERT INTO editoriales(nombre, pais, ciudad, telefono) VALUES (%s, %s, %s, %s)'

# cargamos en una variable las tuplas a agregar
filas = [
 ('Editorial1', 'chile', 'santiago', 11111111),
 ('Editorial2', 'argentina', 'buenos aires', 22222222)
]
#ejecutamos la sentencia que agrega las filas (hay que usar executemany al agregar más de 1 fila)
my_cursor.executemany(sqlSentence, filas)

# Se guardan las filas creadas en la base de datos
mydb.commit()

# cargamos en una variable la sentencia SQL para agregar varias filas en tabla Libros
sqlSentence = 'INSERT INTO libros(titulo, autor, año, paginas, editorial_id) VALUES (%s, %s, %s, %s, %s)'

# preparamos un arreglo de las tuplas a agregar
filas = [
 ('Libro1', 'Jaime Navon', 2000, 600, 1),
 ('Libro2', 'Sebastian Leon', 2015, 300, 2),
 ('Libro3', 'Fabian Estelle', 2021, 100, 1)
]
# ejecutamos la sentencia que inserta las filas (notar el executemany)
my_cursor.executemany(sqlSentence, filas)

#Se guardan los cambios hechos en la base de datos
mydb.commit()

#### PARTE EXTRA: REVISAR LAS TABLAS #####

# Revisemos que se hizo el proceso bien, imprimiendo las filas de cada tabla

# creamos una nueva conexión con la base de datos creada. LLENAR CON LOS DATOS DE SU MYSQL
mydb = db.connect(
 host = 'localhost',
 user = 'root',
 passwd = 'piriro',
 database = 'taller2'
)
# usando la conexión creamos un cursor
my_cursor = mydb.cursor()

# Creamos una consulta para extraer todas las filas de la tabla libros
sqlSentence = 'SELECT * FROM libros;'

#ejecutamos la sentencia
my_cursor.execute(sqlSentence)

# Se extrae el resultado, convirtiéndolo en un objeto de python
rows = my_cursor.fetchall()
# Se imprimen todas las filas de la tabla de libros
print('Filas en tabla Libros:')
for row in rows:
    print(row)

# Se repite el proceso para la tabla de editoriales
# Creamos una consulta para extraer todas las filas de la tabla libros
sqlSentence = 'SELECT * FROM editoriales;'

#ejecutamos la sentencia
my_cursor.execute(sqlSentence)

# Se extrae el resultado, convirtiéndolo en un objeto de python
rows = my_cursor.fetchall()
# Se imprimen todas las filas de la tabla de libros
print('Filas en tabla Editoriales:')
for row in rows:
    print(row)