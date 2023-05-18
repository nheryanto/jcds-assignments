if __name__ == '__main__':
    '''
    a_now: usia Andi saat ini
    b_now: usia Budi saat ini
    a_next: usia Andi 2 tahun lagi
    b_next: usia Budi 2 tahun lagi

    a_now + b_now = 49  (1)
    a_now = 0.4*b_now   (2)
    
    substitusi (2) ke (1)
    0.4*b_now + b_now = 49
    1.4*b_now = 49
    '''
    # menghitung usia Andi dan Budi saat ini
    b_now = 49/1.4
    a_now = 0.4*b_now

    # menghitung usia Andi dan Budi 2 tahun lagi
    a_next = a_now + 2
    b_next = b_now + 2
    print(f"Dua tahun lagi, usia Andi = {a_next} tahun dan usia Budi = {b_next} tahun")