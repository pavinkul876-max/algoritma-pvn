nama = input("Masukkan nama siswa (Kevin / Ardi / Ello): ").strip()
#strip menghapus semua jenis spasi
#elif fungsinya adalah untuk memberikan pilihan kedua, ketiga, dan seterusnya ya bu yh jika pilihan pertama (if) salah.
#lower mengubah semua huruf besar dalam teks menjadi huruf kecil seingat ku
if nama.lower() == "kevin":
    nilai_ujian = 90
    status_hadir = "hadir"
elif nama.lower() == "ardi":
    nilai_ujian = 75
    status_hadir = "hadir"
elif nama.lower() == "ello":
    nilai_ujian = 80
    status_hadir = "alfa"
else:
    # jika memasukkan nama selain 3 di atas, bisa diinput manual ya bu guru rizki cantik
    nilai_ujian =float(input("Masukkan nilai ujian (0-100): "))  #float sama ygbu rizki jelaskan lah ya
    status_hadir = input("Masukkan status kehadiran (hadir/alfa): ").lower()

lulus =(status_hadir == "hadir") and (nilai_ujian >= 65 )


beasiswa = (status_hadir == "hadir") and (nilai_ujian >= 85)

print("\n" + "="*35) #maaf ya bu ini aku tanya ai soalnya dah pusing 
print(f"Nama Siswa       : {nama}")    #f fungsinya buat masukin variabel itu pokonya maaf klo salah
print(f"Nilai Ujian      : {nilai_ujian}")
print(f"Status Kehadiran : {status_hadir}")
print("="*35)

if status_hadir == "alfa":
    print("Hasil Status     : TIDAK LULUS (Gagal karena kebanyakan Alfa)")
elif beasiswa:
    print("Hasil Status     : LULUS + DAPAT BEASISWA!")
elif lulus:
    print("Hasil Status     : LULUS")
else:
    print("Hasil Status     : TIDAK LULUS (Nilai tidak mencukupi)")
    #nilai 10000000 ya bu mks