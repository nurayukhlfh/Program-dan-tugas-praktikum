biodata = {'Nama'    : 'Nur Ayu Khalifah',
         'Panggilan' : 'Ayu',
         'Nim'       : '231031058',
         'TTL'       : 'Parepare, 22 Februari 2005',
         'Agama'     : 'Islam',
         'Alamat'    : 'Jl.Kijang',
         'RT/RW'     : '002/008',
         'Hobi'      : 'Melukis'
           }


biodata['Panggilan'] = 'Ayu'
print('Nama Lengkap saya adalah {} biasa dipanggil {} '.format(
  biodata.get('Nama'),
  biodata.get('Panggilan')
))

biodata['nim'] = ''
print('Nim saya{} adalah {}'.format(
  biodata.get('nim'),
  biodata.get('Nim')
))

biodata['TTl'] = ''
print('Tempat Tanggal Lahir saya{} {}'.format(
  biodata.get('TTl'),
  biodata.get('TTL')
))

biodata['agama'] = ''
print('Agama saya adalah{} agama {}'.format(
  biodata.get('agama'),
  biodata.get('Agama')
))

biodata ['RT'] = '002'
biodata ['RW'] = '008'
print('Alamat saya di {} RT {} RW {}'.format(
  biodata.get('Alamat'),
  biodata.get('RT'),
  biodata.get('RW')
))

biodata['Hobi'] = 'Melukis'
print('Hobi dari saya adalah {}'.format(
  biodata.get('Hobi')
))

