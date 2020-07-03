# konstruksi dasar python
# sequential : eksekusi berurutan

print('halo dunia')
print('by : Muhammad Yasa')
print('tanggal 20 desember 2020')
print('---'*10)

# percabangan : eksekusi terpilih

aku_ingin_cepat = True

if aku_ingin_cepat:
    print('jalan lurus terus')
else:
    print('jalan memutar saja')


# perulangan
jumalah_anak = 4
# print('halo anak #1')
# print('halo anak #2')
# print('halo anak #3')
# print('halo anak #4')

for index_anak in range(1,jumalah_anak+1): # jumlah perulangan, jumlah anak - 1 = 4
    print(f'halo anak {index_anak}')

