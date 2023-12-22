print('Tugas Praktikum 4'.center(35))
nama = 'Nur Ayu Khalifah'
nim  = '231031058'
prodi= 'Sistem Informasi B'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''


print()
str1 = 'duFort Frankel Von Neumann'
a = 'duFort'
b = 'Frankel'
c = 'Von'
d = 'Neumann'
ndfv = d+' '+a+' '+b+' '+c
e = ndfv.upper()
print(e)
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
a = str2.lower() 
a = a.replace('dufort frankel von','dfv')
print(a)
#output: dfv neumann

str3 = 'duFort Frankel Von Neumann'
a = str3.upper ()
a = a.replace('FRANKEL VON NEUMANN','F V N')
print(a)
#output: DUFORT F V N

str4 = 'duFOrt Frankel Von Neumann'
a = str4.lower()
b = 'dufort'
c = 'frankel'
d = 'von'
e = 'neumann'
e = e.replace ('neumann','N')
b = b.replace ('dufort','duFort')
c = c.replace ('frankel','f')
d = d.replace ('von','v')
ndfv = e+' '+b+' '+c+' '+d
print(ndfv)
#output: N duFort f v

str5 = 'DuFort Frankel Von Neumann'
a = 'Neumann'
a = a.upper()
b = str5.replace ( 'DuFort Frankel Von',' d f v')
b = 'd f v'
ndfv = a+' '+b
print(ndfv)
#output: NEUMANN d f v

str6 = 'duFort Frankel Von Neumann'
a = str6.upper ()
b = 'NEUMANN'
c = 'DUFORT FRANKEL VON'
c = c.replace ('DUFORT FRANKEL VON','DFV')
ndfv = b+' '+c
print(ndfv)
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
a = str7.strip("@$") 
b = a.strip("Neumann")
c = str7.replace(str7,"Neumann") 
d = c.upper()
dfvn =b+''+d
print(dfvn)
#output: duFort Frankel Von NEUMANN

str8 = '#duFort@Frankel@Von@Neumann$'
a = str8.replace('@',' ')
print(a.strip('#$'))
#output: duFort Frankel Von Neumann

str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
a = str9.strip("@$") 
b = a.replace("@#^", " ")
c = b.replace("*#(", " ") 
d = c.replace("(#(", " ") 
print(d) 
#output: duFort Frankel Von Neumann

str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann'
a = str10.strip("@^") 
b = a.replace("@!^"," ") 
c = b.replace("!1("," ") 
d = c.replace("(!("," ") 
e = d.title()            
f = e.replace("D","d")   
g = f.replace("f","F")   
print(g)
#output: duFort Frankel Von Neumann
