# 13_UAS_package dan modul daftar nilai

BAHASA PEMROGRAMAN

TEHNIK INFORMATIKA

UNIVERSITAS PELITA BANGSA

NAMA : GUNAWAN

NIM     : 312010191

KELAS   : TI.20.B1

DOSEN   : Agung Nugroho,S.Kom.,M.Kom

SOAL UJIAN AKHIR SEMESTER (UAS)

**Buat package dan modul dengan struktur**

![14_UAS_package dan modul daftar nilai](Gambar/1_Tugas_UAS.jpg)

- Untuk membuat Package Modul kita buka aplikasi **PyCharm** :

![14_UAS_package dan modul daftar nilai](Gambar/2_New_project.jpg)

- Pilih `New Project` Lalu simpan project sesuai Location Directory dan beri nama folder :

![14_UAS_package dan modul daftar nilai](Gambar/3_New_project_Loc.jpg)

- Kemudian Pilih New > Python Package :

       " -> Kita buat Nama Model dan View "

![14_UAS_package dan modul daftar nilai](Gambar/5_New_pyton_pack.jpg)

- Tampilan Package folder Model dan View yang terdapat file_init_.py

![14_UAS_package dan modul daftar nilai](Gambar/6_New_pyton_pack_Model-View.jpg)

- Kemudian kita buat nama program Python dengan Klik Folder Model > pilih New >Python File dengan nama : daftar_nilai.py

![14_UAS_package dan modul daftar nilai](Gambar/7_New_pyton_pythfile.jpg)

- Lalu kita buat nama program Python dengan Klik Folder view > pilih New >Python File dengan nama : input_nilai.py dan view_nilai.py

![14_UAS_package dan modul daftar nilai](Gambar/8_New_pyton_View_pythfile.jpg)

- Nama program python sudah kita buat :

![14_UAS_package dan modul daftar nilai](Gambar/9_Direct_new_project.jpg)

# **Buat syntax program python**

**Membuat code program : `daftar_nilai.py`**

![14_UAS_package dan modul daftar nilai](Gambar/10_Program_daftar_nilai.jpg)
![14_UAS_package dan modul daftar nilai](Gambar/11_Program_daftar_nilai-2.jpg)

**Penjelasan :**
- Disini kita menggunakan dictionary ya untuk menyimpan inputan data mahasiswa<br>
- Def tambahkan : Dibagian ini kita gunakan print untuk penulisan bagian input data mahasiswa nanti agar terlihat rapih<br>
- Def hapus : <br>
- Disini kita buat inputan yang menginput nama<br>
    - Gunanya untuk menghapus data mahasiswa dari nama mahasiswa itu sendiri<br>
    - Kita gunakan del untuk fungsi menghapus datanya<br>
    - (If)Jika mahasiswa tersebut ada maka data mahasiswa tersebut akan terhapus<br>
    - (Else)Jika nama mahasiswa tersebut tidak ada maka datanya tidak akan ditemukan<br>
- Def ubah<br>
Penjelasan:<br>
    - Disini kita hampir sama dengan yang hapus, kita gunakan inputan nama untuk mengubah NIM, Nilai Tugas, Ujian Tengah Semester(UTS), ataupun Ujian Akhir Semester(UAS)<br>
    - Lalu setelah kita memasukkan nama maka dictionary akan mengeksekusi program menggunakan keys untuk mencari data dari nama mahasiswa tersebut<br>
    - (If)Jika nama mahasiswa tersebut ketemu atau ada didalam data maka program akan masuk ke inputan NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS yang baru<br>
    - (Else)Jika nama mahasiswa tersebut tidak ada didalam data maka program akan memunculkan tulisan atau perintah bahwa data mahasiswa tidak ada<br>
- Def cari<br>
Penjelasan:<br>
    - Fungsinya sama dengan Def tambahkan<br>    

**Membuat code program `input_nilai.py`**

![14_UAS_package dan modul daftar nilai](Gambar/12_Program_input_nilai.jpg)

Penjelasan:<br>
- From dan import<br>
Penjelasan:<br>
    - From digunakan untuk memanggil package sementara import untuk tujuan yang kita pilih yaitu modul daftar_nilai<br>
    - Lalu kita gunakan import data_mahasiswa itu gunanya agar saat kita menginputkan data atau setiap kali kita menambah data maka data mahasiswa secara otomatis akan masuk kedalam dictionary meskipun beda atau terpisah package dan juga modulnya<br>

  - Def tambah data<br>
Penjelasan:<br>
    - Disini kita buat inputan karena tadi kita sudah membuat kata - kata outputnya kali ini kita cukup membuat inputan data mahasiswanya saja<br>
    - Jangan lupa gunakan perkalian untuk menghitunghasil total atau rata- ratanya<br>
    
**Membuat code program `view_nilai.py`**

![14_UAS_package dan modul daftar nilai](Gambar/13_Program_view_nilai.jpg)
![14_UAS_package dan modul daftar nilai](Gambar/14_Program_view_nilai-2.jpg)

Penjelasan:<br>
- From dan import<br>
Penjelasan:<br>
    - Fungsinya sama saja dengan yang ada dibagian Input_Nilai<br>
 
  - Def tampil<br>
Penjelasan:<br>
    - Disini kita buat sebuah tabel untuk menampilkan data - data dan nama - nama mahasiswa didalam dictionary<br>
    - (If)Jika terdapat data maka data dan nama mahasiswa tersebut akan muncul<br>
    - Disini kita menggunakan for untuk melakukan perulangan nomor urut<br>
    - (Else)Jika kita belum menginputkan data sama sekali maka akan muncul tulisan "tidak ada data"<br>
    
  - Def cari data<br>
Penjelasan:<br>
    - Tadi kita sudah buat print sama seperti dibagian Input_Nilai<br>
    - Kita akan langsung membuat inputan dengan format nama untuk mencari data dari mahasiswa yang sedang kita cari<br>
    - (If)Jika data mahasiswa yang dicari ada didalam dictionary maka data baik Nama, NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS akan muncul<br>
    - (Else)Jika data mahasiswa yang dicari tidak ada didalam dictionary maka akan muncul tulisan "datanya tidak ada"<br>
    
**Membuat code program :  `main.py`**

![14_UAS_package dan modul daftar nilai](Gambar/15_Program_main.jpg)

- From dan import<br>
Penjelasan:<br>
    - Sama seperti sebelumnya hanya saja disini sedikit berbeda<br>
    - From disini kita tulis package.modulnya lalu import fungsi(def) tadi<br>
    - Karena dibagian main ini kita akan menggunakan atau membuat syntax pilihan menu<br>
   
  - While True<br>
Penjelasan:<br>
    - Kita gunakan print untuk membuat pilihan menunya<br>
    - Lalu kita buat inputan untuk memilih menu nanti ketika program dijalankan<br>
    - (If dan Elif)Kita gunakan karena kita akan membuat cabang pilihan yang banyak<br>
    - Lalu dibawahnya kita tambahkan  juga fungsi - fungsi yang sudah kita buat tadi<br>
    - Pada perintah ke 6 kita gunakan break untuk keluar dari program yang kita jalankan<br>
    - (Else)Jika kita tidak memilih salah satu menu tersebut maka akan muncul peringatan "pilih menu yang tersedia diatas"<br>
    
# **Menjalankan program python**

- Untuk menjalankan program kita klik : Run > `main.py`

* Pilih Menu Nomor : 1. Tambah

![14_UAS_package dan modul daftar nilai](Gambar/16_Tambah_data.jpg)

* Pilih Menu Nomor : 2. Tampil

![14_UAS_package dan modul daftar nilai](Gambar/17_Tampilkan_data.jpg)

* Untuk Menambah data lagi,pilih Menu Nomor : 1. Tambah

![14_UAS_package dan modul daftar nilai](Gambar/18_Tambah_data_lagi.jpg)

* Untuk menampilkan data yang kita tambah,Pilih Menu Nomor : 2. Tampil

![14_UAS_package dan modul daftar nilai](Gambar/19_Tampilkan_data_lagi.jpg)

* Pilih Menu Nomor : 3. Hapus

![14_UAS_package dan modul daftar nilai](Gambar/20_Hapus_data.jpg)

* Untuk menampilkan data yang kita hapus,Pilih Menu Nomor : 2. Tampil

![14_UAS_package dan modul daftar nilai](Gambar/21_Tampilakan_Hapus_data.jpg)

* Pilih Menu Nomor : 4. Ubah

![14_UAS_package dan modul daftar nilai](Gambar/22_Ubah_data.jpg)

* Untuk menampilkan data yang kita ubah,Pilih Menu Nomor : 2. Tampil

![14_UAS_package dan modul daftar nilai](Gambar/23_Tampilkan_Ubah_data.jpg)

* Pilih Menu Nomor : 5. Cari
* > Kemudian ketik Nama Mahasiswa

![14_UAS_package dan modul daftar nilai](Gambar/24_Tampilkan_cari_data.jpg)

* Pilih Menu Nomor : 6. Keluar dari program

![14_UAS_package dan modul daftar nilai](Gambar/25_Keluar_program.jpg)

- Untuk Melihat syntax - syntax program python yang sudah kita buat silahkan tekan ``Click Here``: 

1. Package modul(daftar_nilai) [Click Here](Model/daftar_nilai.py)
2. Package View(input_nilai) [Click Here](View/input_nilai.py) dan view(view_nilai) [Click Here](View/view_nilai.py)
3. modul main [Click Here](main.py)

Cukup Sekian Penjelasan dari saya.

   **TERIMAKASIH**
