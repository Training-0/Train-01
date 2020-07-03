# tipe data penting
print('tipe data skalar')
anak1 = 'yasa'
anak2 = 'muhammad'
anak3 = 'power'
anak4 = 'ranger'
anak5 = 'merah'

print(anak1)
print(anak2)
print(anak3)
print(anak4)
print(anak5)

print('\ntipe data list/daftar/array')

anak = ['dragon', 'zameckis', 'bagdemagus']
print(anak)
anak.append('bagus')
print(anak)

print('\nsapa anak ke 2')
print(f'hai anak {anak[1]}')

print('\nsapa semua anak')
for a in anak:
    print(f'hai {a}')

print('\nsapa semua anak cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}.hai {anak[a]}')

