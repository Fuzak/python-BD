# importamos el conector
import mysql.connector as db

##### PARTE 2: CREAR TABLAS LIBROS Y EDITORIALES #####

# creamos una nueva conexión con la base de datos creada. LLENAR CON LOS DATOS DE SU MYSQL
mydb = db.connect(
 host = 'localhost',
 user = 'root',
 passwd = 'piriro',
 database = 'taller2'
)
# usando la conexión creamos un cursor
my_cursor = mydb.cursor()

# cargamos en una variable la sentencia SQL para crear la la tabla editoriales
sqlSentence = 'CREATE TABLE editoriales(id INT PRIMARY KEY AUTO_INCREMENT, \
                                           nombre VARCHAR(50), \
                                           pais VARCHAR(30), \
                                           ciudad varchar(100), \
                                           telefono INT);'

# ejecutamos la sentencia que crea la tabla editoriales
my_cursor .execute(sqlSentence)


# cargamos en una variable la sentencia SQL para crear la la tabla libros,
# notar que se agrega una llave foranea a la columna editorial_id
sqlSentence = 'CREATE TABLE Libros(id INT PRIMARY KEY AUTO_INCREMENT , \
                                   titulo VARCHAR(100), \
                                   autor VARCHAR(100), \
                                   año INT,  \
                                   paginas INT, \
                                   editorial_id INT references EDITORIALES(ID));'

# ejecutamos la sentencia que crea la tabla libros
my_cursor .execute(sqlSentence)
