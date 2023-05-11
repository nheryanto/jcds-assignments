if __name__ == '__main__':
    hari = 485

    # konversi hari ke tahun
    tahun = hari // 360
    # menghitung sisa hari
    sisa_hari = hari % 360

    # konversi sisa hari ke bulan
    bulan = sisa_hari // 30
    # menghitung sisa hari
    sisa_hari %= 30

    # konversi sisa hari ke minggu
    minggu = sisa_hari // 7
    # menghitung sisa hari
    sisa_hari %= 7
    
    print(f"{hari} hari = {tahun} tahun {bulan} bulan {minggu} minggu {sisa_hari} hari")

    # pengecekan
    #total_hari = tahun*360 + bulan*30 + minggu*7 + sisa_hari
    #flag = str(hari == total_hari).upper()
    #print('Jumlah hari sama ' + flag)
