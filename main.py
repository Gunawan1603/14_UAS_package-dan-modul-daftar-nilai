from Model.daftar_nilai import tambahkan, ubah, hapus, cari
from View.input_nilai import tambahdata
from View.view_nilai import tampil, caridata

while True:
    print('\nPilih salah satu menu di bawah ini:')
    print('=====================================')
    print('\n1.Tambah \n2.Tampil \n3.Hapus \n4.Ubah \n5.Cari \n6.Keluar dari program')
    x = input('\nMasukkan Pilihan Menu anda\t: ')
    if x.lower() == "1":
        tambahkan()
        tambahdata()
    elif x.lower() == "2":
        tampil()
    elif x.lower() == "3":
        hapus()
    elif x.lower() == "4":
        ubah()
    elif x.lower() == "5":
        cari()
        caridata()
    elif x.lower() == "6":
        print('Anda sudah keluar dari program')
        break

    else:
        print('Pilih menu yang tersedia di atas')
