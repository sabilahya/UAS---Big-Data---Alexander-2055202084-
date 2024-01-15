import mysql.connector

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="spekhp"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan data handphone yang ingin dimasukkan

handphone_data = [

    ("Iphone 14 Pro Max", "256 GB", "Apple A16 Bionic", "48 MP"),

    ("Advan NASA Pro", "32 GB", "UNISOC SC9832E", "13 MP"),

    ("OPPO Find N3", "512 GB", "Qualcomm Snapdragon 8 Gen 2", "64 MP"),

    ("vivo V29e", "256 GB", "Snapdragon 695 5G", "64 MP")

]

 

# Perulangan untuk memasukkan data ke dalam tabel

for data in handphone_data:

    insert_query = "INSERT INTO handphone (merek, memory, processor, kamera) VALUES (%s, %s, %s, %s)"

    db_cursor.execute(insert_query, data)