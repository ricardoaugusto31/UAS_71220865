print("*"*6, "Kredit Keaktifan Mahasiswa", "*"*6)
print("(Student Activities Credit)")
print("1. Menambahkan Kegiatan")
print("2. Menampilkan Jumlah Poin")
print("3. Keluar")
print("-"*27)
pilihan = int(input("Silahkan masukan pilihan Anda: "))
pPrestasi = "30"
pOrganisasi = "10"
pKepanitiaan = "5"
pRekognisi = "2"


if pilihan == 1:
    nk = input("Nama Kegiatan: ")
    tgl = input("Tanggal Kegiatan: ")
    print("Pilihan Kategori Kegiatan: ")
    print("- Prestasi")
    print("- Organisasi")
    print("- Kepanitiaan")
    print("- Rekognisi")
    pk = input("Masukan Kategori Kegiatan: ")
    Prestasi = "Prestasi"
    Organisasi = "Organisasi"
    Kepanitiaan = "Kepanitiaan"
    Rekognisi = "Rekognisi"
    print("Kegiatan berhasil ditambahkan.")
elif pilihan == 2:
    print("Nama Kegiatan", "Tanggal",  "Kategori",  "Poin")
    print("HMTI 2022", "tahun 2022-2023", "Organsisasi", pOrganisasi)
    

else:
    print("Sistem berhenti...")

    
   














