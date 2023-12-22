nama = str (input('Nama karyawan: '))
pendapatan = float(input("Masukkan pendapatan karyawan: "))
status_berhak = 1000
if pendapatan >= 1000:
    print('Status: Berhak')
else:
    print('Status: Tidak Berhak')
