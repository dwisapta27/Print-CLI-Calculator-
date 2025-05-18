w = 800
hp = 350

print('=====JASA PRINT=====')
print('Hitam Putih = 350')
print('Warna = 800')
print('')

halaman = str(input('Banyaknya halaman = '))
hitamputih = int(input('Banyaknya kertas Hitam Putih = '))
warna = int(input('Banyaknya kertas Warna = '))

print('=',(hitamputih*hp)+(warna*w))
a = (hitamputih*hp)+(warna*w)
rgkp = int(input('Jumlah rangkap = '))
rangkap = rgkp*a

print('Total = ',rangkap)
print('')

lthp = int(input('Banyaknya tambahan kertas Hitam putih = '))
ltw = int(input('Banyaknya tambahan kertas Warna = '))   

print('total lembar tambahan = ',(lthp*hp)+(ltw*w))
b = (lthp*hp)+(ltw*w)

total = rangkap+b
print('')
print('Total yang harus dibayar',total)

print('Terima kasih ;)')