# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="spekhp"  # Ganti dengan nama database yang telah Anda buat

)

# Buat objek cursor

db_cursor = db_connection.cursor()

# Definisikan struktur tabel 'handphone'

create_table_query = """

CREATE TABLE handphone (

    id INT AUTO_INCREMENT PRIMARY KEY,

    merek VARCHAR(100),

    memory VARCHAR(50),

    processor VARCHAR(50),

    kamera VARCHAR(50)

)

"""

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

# Komit perubahan ke database

db_connection.commit()

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()