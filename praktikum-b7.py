import os
os.system('cls')

a = True

while a:
    jawab = input('Apakah ingin lanjutkan? (y/n)')
    if jawab == 'y':

        os.system('cls')
        print('Selamat Datang Lagi')
        a = True

    elif jawab == 'n':

        print('Sampai Ketemu Lagi :D')
        a = False

    else:

        os.system('cls')
        print('Jangan aneh-aneh deh ToT')
        a = True
