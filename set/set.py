bulan1={'januari','februari','maret'}
bulan2={'April','May','June','July'}
bulan3={'July','August','September'}
bulan4=set()
print(type(bulan4))


bulan={'Januari','February','March'}
month={'April','May','June','July'}
tsuki={'July','August','September'}
bulan.add('April')
print(bulan)

if 'May' in bulan:
    print('yes')
else:
    print('no')

bulan |= month
print(bulan)

month &= tsuki
print(month)

tsuki.pop()
print(tsuki)
print(tsuki <= month)
print(month >= tsuki)



