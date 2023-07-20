import psycopg2
import requests
import os
import base64

def download_files_from_database():
    # Informasi koneksi ke database PostgreSQL
    db_host = 'localhost'
    db_name = 'sister_db'
    db_user = 'postgres'
    db_password = '4dm1n'

    # Membuat koneksi ke database
    conn = psycopg2.connect(
        host=db_host,
        dbname=db_name,
        user=db_user,
        password=db_password
    )

    # Membuat cursor
    cursor = conn.cursor()

    try:
        # Query untuk mendapatkan data file dari tabel 'dokumen'
        cursor.execute("SELECT id_dok, file_name, media_type, file_dok FROM dok.dokumen")
        rows = cursor.fetchall()

        # Loop melalui hasil query dan mendownload file
        for row in rows:
            doc_id, nama_file, tipe_file, data_file = row

            if data_file is not None:  # Cek apakah data_file berisi data yang valid
                # Konversi data BYTEA menjadi bentuk bytes yang benar
                data_file_bytes = base64.b64decode(data_file)

                # Tentukan direktori penyimpanan untuk file
                save_dir = 'downloads'
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                # Tentukan nama file yang akan disimpan
                save_path = os.path.join(save_dir, nama_file)

                # Mendownload file dari URL dan menyimpannya di direktori yang telah ditentukan
                with open(save_path, 'wb') as f:
                    f.write(data_file_bytes)

                print(f"File '{nama_file}' (ID: {doc_id}) berhasil diunduh.")
            else:
                print(f"File '{nama_file}' (ID: {doc_id}) tidak dapat diunduh karena data kosong.")

    except Exception as e:
        print("Terjadi kesalahan saat mengunduh file:", e)

    finally:
        # Tutup cursor dan koneksi
        cursor.close()
        conn.close()

if __name__ == "__main__":
    download_files_from_database()
