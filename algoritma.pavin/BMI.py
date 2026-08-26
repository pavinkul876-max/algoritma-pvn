berat = float(input("Masukkan berat badan (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan (cm): "))

# Konversi tinggi dari cm ke meter ya bu kalo gada ini eror
tinggi_m = tinggi_cm / 100

# Hitung BMI
bmi = berat / (tinggi_m**2)

# Penentuan kategori dan keterangan berdasarkan nilai BMI ya bu ya
if bmi < 18.5:
    kategori = "Kurus (Underweight)"
    keterangan = "Perlu tambah berat badan"
elif 18.5 <= bmi <= 24.9:
    kategori = "Normal (Ideal)"
    keterangan = "Pertahankan gaya hidup sehat"
elif 25 <= bmi <= 29.9:
    kategori = "Gemuk (Overweight)"
    keterangan = "Perlu olahraga lebih"
else:
    kategori = "Obesitas"
    keterangan = "Konsultasi dokter"

# hasilnya ibukuhh
print(f"\nNilai BMI  : {bmi:.2f}")
print(f"Kategori   : {kategori}")
print(f"Keterangan : {keterangan}")