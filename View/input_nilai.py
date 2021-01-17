from Model.daftar_nilai import data_mahasiswa


def tambahdata():
    nama = input('\nMasukkan Nama Mahasiswa\t\t\t: ')
    nim = int(input('Masukkan NIM Mahasiswa\t\t\t: '))
    tugas = int(input('Masukkan Nilai Tugas Mahasiswa\t: '))
    uts = int(input('Masukkan Nilai UTS Mahasiswa\t: '))
    uas = int(input('Masukkan Nilai UAS Mahasiswa\t: '))
    hasil = (tugas*0.3) + (uts*0.35) + (uas*0.35)
    data_mahasiswa[nama] = nim, tugas, uts, uas, hasil