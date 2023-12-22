pwd_benar = 'si23b'
a = True
i = 0
limit = 3
while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        print('Password Salah, Coba Lagi!')
        if i == limit:
            a = False
            print('Anda kehabisan kesempatan')
        else:
            print(f'Kesempatan anda tersisa {limit-i} kali')


komputer memilih angka [1...5]
user tebak angka:
jika salah 1: Tebakan salah, anda memiliki 2 kesempatan lagi
jika salah 2: Tebakan salah, anda memiliki 2 kesempatan lagi
jika salah 3: Tebakan salah, belum berhasil
            Angka yang dicari adalah x
