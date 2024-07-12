import mysql.connector

# Koneksi ke database
dbq = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud"
)

mycursor = dbq.cursor()

# CREATE - Menambahkan data baru ke dalam tabel
def create_data(id, nama_produk, jumlah_produk, harga_produk):
    sql = "INSERT INTO produk (id, nama_produk, jumlah_produk, harga_produk) VALUES (%s, %s, %s, %s)"
    nilai = (id, nama_produk, jumlah_produk, harga_produk)
    mycursor.execute(sql, nilai)
    dbq.commit()
    print(mycursor.rowcount, "record inserted.")

# READ - Membaca data dari tabel
def read_data():
    sql = "SELECT * FROM produk"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# UPDATE - Memperbarui data yang ada dalam tabel
def update_data(id, nama_produk, jumlah_produk, harga_produk):
    sql = "UPDATE produk SET nama_produk = %s, jumlah_produk = %s, harga_produk = %s WHERE id = %s"
    nilai = (nama_produk, jumlah_produk, harga_produk, id)
    mycursor.execute(sql, nilai)
    dbq.commit()
    print(mycursor.rowcount, "record(s) affected.")

# DELETE - Menghapus data dari tabel
def delete_data(id):
    sql = "DELETE FROM produk WHERE id = %s"
    nilai = (id,)
    mycursor.execute(sql, nilai)
    dbq.commit()
    print(mycursor.rowcount, "record(s) deleted.")

# Menutup cursor dan koneksi
mycursor.close()
dbq.close()
