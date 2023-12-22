nim = [2,3,1,0,3,1,0,5,8]
nim1 = ['2','3','1','0','3','1','0','5','8']
print(nim)
# akses item
print('item indeks 0: ',nim[0])
print('item indeks 0: ',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
# akses indeks negatif
print('item indeks terakhir:',nim[-1])
print('item indeks terakhir:',nim[-len(nim)])
print('item indeks 3: [-6]',nim[-6])
print('item indeks 5: [-4]',nim[-4])
print('item indeks -7: [2]',nim[2])
print('item indeks 2: [-7]',nim[-7])
# akses indeks batas
print(f'item indeks 1,2.....: {nim[1:]}')
print(f'item indeks 3,4.....: {nim[3:]}')
print(f'item indeks 0,1,2,3 : {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8] : {nim[:-1]}')
print(f'item indeks [:4] : {nim[:-5]}')
# pengirisan
print(f'item indeks 1,2,: {nim[1:3]}')
print(f'item indeks []  : {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
# nested list
kelas = [('Kalkulus',2),
         ('Pancsila',3)]
kelas.append(('Programming',2))
kelas.append(("Sainster",3))
kelas.append(("Bahasa",2))
# tambahkan matkul 4 dan 5 dan sksnya

# Mata kuliah 1: Matkul1 dengan 2 sks
# Mata kuliah 2: Matkul2 dengan 3 sks
# Mata kuliah 3: Matkul3 dengan 2 sks
# Mata kuliah 4: Matkul4 dengan 3 sks
# Mata kuliah 5: Matkul5 dengan 2 sks

print()
print(f'Mata kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks')
print(f'Mata kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks')
print(f'Mata kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks')
print(f'Mata kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks')
print(f'Mata kuliah 5: {kelas[4][0]} dengan {kelas[4][1]} sks')
print()


data = [('Nur Ayu Khalifah',2023,'Aktif'),
        (98,99,99,97,98),
        (2,3,2,3,2),
        ('SI-Reguler','Sistem Informasi B','Ganjil')]

print()
print(f'Nama mahasiswa: {data[0][0]}')
print(f'Inisial {data[0][0]}: {data[0][0][0]}{data[0][0][4]}{data[0][0][8]}')
ubah = int(''.join(map(str,nim))) 
print(f'NIM {data[0][0]}: {ubah}')
print(f'Program {data[0][0]}: {data[-1][0]} {data[-1][1]}')
print(f'Angkatan {data[0][0]}: {data[-1][-1]}-{data[0][1]}')
print(f'Total sks {data[0][0]} adalah: {sum(data[2])}')
print(f'Jumlah Nilai {data[0][0]}: {len(data[2])}')
print(f'Nilai tertinggi {data[0][0]}: {max(data[1])}')
print(f'Nilai terendah {data[0][0]}: {min(data[1])}')
print(f'Rata-rata nilai {data[0][0]}: {sum(data[1])/len(data[1])}')


#Nama mahasiswa: Nur Ayu Khalifah
#Inisial Nur Ayu Khalifah: NAK
#NIM Nur Ayu Khalifah: 231031058
#Program Nur Ayu Khalifah: SI-Reguler Sistem Informasi B
#Angkatan Nur Ayu Khalifah: Ganjil-2023
#Total sks Nur Ayu Khalifah adalah: 12
#Jumlah Nilai Nur Ayu Khalifah: 5
#Nilai tertinggi Nur Ayu Khalifah: 99
#Nilai terendah Nur Ayu Khalifah: 97
#Rata-rata nilai Nur Ayu Khalifah: 98.2














