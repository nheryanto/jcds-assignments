if __name__ == '__main__':
    '''
    A dan B berjarak 120km dan sama-sama berangkat jam 9 WIB.
    Kecepatan A 60km/jam dari timur dan kecepatan B 40km/jam dari barat.
    Asumsi posisi mula B adalah titik 0, maka posisi A dan B setelah waktu berjalan selama t jam:
    posisi_A = 40*t         (1)
    posisi_B = 120 - 60*t   (2)
    A dan B akan bertemu ketika mereka berada di posisi yang sama atau (1) = (2)
    60*t = 120-40*t
    100*t = 120
    dimana t adalah waktu yang diperlukan sampai A dan B bertemu.
    '''
    
    # menghitung waktu sampai bertemu dalam menit
    t = 120/100 * 60
    # konversi menit ke jam
    hours = int(t//60)
    # menghitung sisa menit
    mins = int(t % 60)

    # jam berangkat
    start_time = 9

    print(f"A dan B bertemu pukul {start_time+hours} lewat {mins} menit WIB")
