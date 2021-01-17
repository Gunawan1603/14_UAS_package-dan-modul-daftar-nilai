data_mahasiswa = {}


def tambahkan():
    print('||======<  Tambah Data Mahasiswa  >======||')
    print('||=======================================||')
    print('||======< Masukkan Data Mahasiswa >======||')


def hapus():
    print('||======< Hapus Data Mahasiswa >======||')
    print('||====================================||')
    nama = input('Masukkan Nama Mahasiswa\t\t:')
    if nama in data_mahasiswa.keys():
        del data_mahasiswa[nama]
        print('\n||=====< Data mahasiswa berhasil dihapus >=====||')
    else:
        print('\nData {0} Tidak Ditemukan'.format(nama))


def ubah():
    print('\nMengubah Data Mahasiswa')
    print('=======================')
    nama = input('Masukkan Nama Mahasiswa\t\t\t: ')
    if nama in data_mahasiswa.keys():
        nim = int(input('Masukkan NIM Baru Mahasiswa\t\t: '))
        tugas = int(input('Masukkan Nilai Tugas Terbaru\t: '))
        uts = int(input('Masukkan Nilai UTS Terbaru\t\t: '))
        uas = int(input('Masukkan Nilai UAS Terbaru\t\t: '))
        hasil = (tugas*0.3) + (uts*0.35) + (uas*0.35)
        data_mahasiswa[nama] = nim, tugas, uts, uas, hasil
        print('\n||=====< Data Mahasiswa berhasil diubah >=====||')
    else:
        print('\nData {0} Tidak Ditemukan'.format(nama))


def cari():
    print('||=====< Cari Data Mahasiswa >=====||')
    print('||=================================||')
    print('||===< Masukkan Data Mahasiswa >===||')