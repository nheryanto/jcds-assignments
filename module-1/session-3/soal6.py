if __name__ == '__main__':
    jumlah_apel = int(input("Masukkan Jumlah Apel: "))
    jumlah_jeruk = int(input("Masukkan Jumlah Jeruk: "))
    jumlah_anggur = int(input("Masukkan Jumlah Anggur: "))

    harga_apel = 10000
    harga_jeruk = 15000
    harga_anggur = 20000

    total_apel =jumlah_apel * harga_apel
    total_jeruk = jumlah_jeruk * harga_jeruk
    total_anggur = jumlah_anggur * harga_anggur
    total_belanja = total_apel + total_jeruk + total_anggur

    print("Detail Belanja")
    print(f"Apel : {jumlah_apel} x {harga_apel} = {total_apel}")
    print(f"Jeruk : {jumlah_jeruk} x {harga_jeruk} = {total_jeruk}")
    print(f"Anggur : {jumlah_anggur} x {harga_anggur} = {total_anggur}")
    print(f"Total : {total_belanja}")
