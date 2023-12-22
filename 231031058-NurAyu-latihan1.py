nilai = 70
batas_lulus = 65
nilai = float(input('Masukkan Nilai = '))

if nilai >= batas_lulus :
    print ('Selamat, kamu lulus!')
elif nilai <= batas_lulus :
    print ('Maaf, kamu tidak lulus!')

# Menerima input dari pengguna dan mengonversinya ke dalam integer
nilai = int(input('Masukkan nilai (0-100): '))
batas_lulus = 65

# Memeriksa apakah nilai lebih besar dari batas_lulus
if nilai > batas_lulus:
    print('Selamat, kamu lulus!')
elif nilai <= batas_lulus :
    print ('Maaf, kamu tidak lulus!')
