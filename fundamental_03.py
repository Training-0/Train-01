"""
tipe data dictionary
KVP = Key Value Pair
dictionary = kamus
"""

kamus_indonesia_inggris = {}
kamus_indonesia_inggris['anak'] = 'child'
kamus_indonesia_inggris['istri'] = 'wife'
kamus_indonesia_inggris['ayah'] = 'father'
kamus_indonesia_inggris['ibu'] = 'mother'

# print(kamus_indonesia_inggris)
# print(kamus_indonesia_inggris['ayah'])
# print(kamus_indonesia_inggris['ibu'])


print('data ini di kirimkan oleh server gojek, untuk memberikan info dari drvier di sekitar pemakai aplikasi')

data_dari_server_gojek = {
    'tanggal' : '15-07-2020', # tanggal data di ambil
    'driver_list' : ['santoso', 'bagus', 'dian','wina'] # list pengemudi yg ada di tanggal pengambilan
}

print(data_dari_server_gojek)

print(f"Driver di sekitar sini{data_dari_server_gojek['driver_list']}")

print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")

# sekarang saya akan menambah kompelsitas lagi

data_dari_server_gojek_1 = {
    'tanggal' : '15-07-2020', # tanggal data di ambil
    'driver_list' : [{'nama':'santoso', 'jarak':10 }, {'nama':'bagus', 'jarak':30 }, {'nama':'dian', 'jarak':55 },{'nama':'wina', 'jarak':70 }] # list pengemudi yg ada di tanggal pengambilan
}

print(data_dari_server_gojek_1)

print(f"\nDriver di sekitar sini{data_dari_server_gojek_1['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek_1['driver_list'][0]}")
print(f"Driver terdekat {data_dari_server_gojek_1['driver_list'][0]['jarak']} meter")
