Download file images or pdf Postgresql
Dibuat untuk kebutuhan mendownload file berjenis BYTEA pada postgresql

Beberapa hal yg harus dipastikan
# Informasi koneksi ke database PostgreSQL
    db_host = 'localhost'
    db_name = 'nama_database'
    db_user = 'postgres'
    db_password = 'postgres_password'
# Edit keperluan ini untuk disesuaikan
    cursor.execute("SELECT id_dok, file_name, media_type, file_dok FROM dok.dokumen")
    id_dok = baris primary key
    file_name = baris variable name
    media_type = baris untuk jenis media
    file_dok = baris pada tabel untuk file yang ingin di download
    dok.dokumen = Terdapat pada skema dok pada tabel dokumen
    ![image](https://github.com/deffan10/Download-File-From-Postgresql/assets/49578199/3b71f049-6f27-4751-9d2d-40046735ed45)
