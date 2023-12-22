#variabel untuk password benar
pw_instagram_benar ='malmwoL11'

#variabel kesempatan
kesempatan = 3

#variabel untuk status login
login_berhasil = False

#loop while untuk proses login
while kesempatan > 0 and not login_berhasil:
    #meminta user memasukkan password
    input_password = input('Masukkan password: ')
    #memeriksa password
    if input_password == pw_instagram_benar:
        print('Login berhasil')
        login_berhasil = True
    else:
        kesempatan -= 1
        if kesempatan > 0:
            print(f'Passwprd yang anda masukkan salah. Kesempatan login tersisa: {kesempatan}')
        else:
            print('Anda telah melebihi batas login')


