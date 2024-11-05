# Kelas Induk
class Kendaraan:
    def __init__(self, nama, kecepatan):
        self.nama = nama
        self.kecepatan = kecepatan

    def info(self):
        print(f"Nama Kendaraan: {self.nama}")
        print(f"Kecepatan: {self.kecepatan} km/jam")

# Kelas Anak 1 (inheritance dari Kendaraan)
class Mobil(Kendaraan):
    def __init__(self, nama, kecepatan, jumlah_pintu):
        super().__init__(nama, kecepatan)  # Memanggil konstruktor kelas induk
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        super().info()  # Memanggil metode info dari kelas induk
        print(f"Jumlah Pintu: {self.jumlah_pintu}")

# Kelas Anak 2 (inheritance dari Kendaraan)
class Motor(Kendaraan):
    def __init__(self, nama, kecepatan, tipe_motor):
        super().__init__(nama, kecepatan)  # Memanggil konstruktor kelas induk
        self.tipe_motor = tipe_motor

    def info(self):
        super().info()  # Memanggil metode info dari kelas induk
        print(f"Tipe Motor: {self.tipe_motor}")

# Membuat objek dari kelas Mobil
mobil = Mobil("Toyota Avanza", 120, 4)
mobil.info()
# Output:
# Nama Kendaraan: Toyota Avanza
# Kecepatan: 120 km/jam
# Jumlah Pintu: 4

print()  # Untuk pemisah output

# Membuat objek dari kelas Motor
motor = Motor("Yamaha NMAX", 100, "Skuter")
motor.info()
# Output:
# Nama Kendaraan: Yamaha NMAX
# Kecepatan: 100 km/jam
# Tipe Motor: Skuter
