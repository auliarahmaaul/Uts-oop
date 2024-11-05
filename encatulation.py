class Produk:
    def __init__(self, nama, harga):
        self.nama = nama               # Atribut publik
        self.__harga = harga           # Atribut privat (enkapsulasi)

    # Getter untuk mendapatkan harga
    def get_harga(self):
        return self.__harga

    # Setter untuk mengubah harga, hanya jika harga baru lebih besar dari 0
    def set_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
            print(f"Harga berhasil diubah menjadi {self.__harga}")
        else:
            print("Harga harus lebih besar dari 0.")

    # Metode untuk menampilkan informasi produk
    def tampilkan_info(self):
        print(f"Nama Produk: {self.nama}")
        print(f"Harga: {self.get_harga()}")

# Membuat objek Produk
produk = Produk("Laptop", 10000000)

# Mengakses dan menampilkan informasi produk
produk.tampilkan_info()
# Output:
# Nama Produk: Laptop
# Harga: 10000000

# Mengubah harga menggunakan setter
produk.set_harga(12000000)  # Output: Harga berhasil diubah menjadi 12000000

# Menampilkan harga setelah perubahan
print(f"Harga setelah perubahan: {produk.get_harga()}")  # Output: Harga setelah perubahan: 12000000

# Mencoba memberikan harga negatif
produk.set_harga(-5000)  # Output: Harga harus lebih besar dari 0.

# Mencoba mengakses harga secara langsung (akan gagal karena __harga adalah privat)
# print(produk.__harga)  # Akan menghasilkan error jika di-uncomment
