"""
Program Perhitungan Listrik Rumah Tangga
Menggunakan modul Biaya untuk menghitung total energi dan biaya listrik bulanan.
"""

from biaya import hitung_biaya

# Input data dari pengguna
energi_bulanan = float(input("Masukkan total konsumsi energi bulanan (kWh): "))

# Hitung biaya listrik
biaya = hitung_biaya(energi_bulanan)

def input_data():
    # Mengambil input perangkat elektronik dari pengguna.
    perangkat = []
    jumlah = int(input("Berapa jumlah alat elektronik? "))

    for i in range(jumlah):
        print(f"\nData alat ke-{i+1}:")
        nama = input("Nama perangkat : ")
        daya = float(input("Daya (watt): "))
        durasi = float(input("Durasi pemakaian per hari (jam): "))

        perangkat.append((nama, daya, durasi))
    
    return perangkat


def hitung_energi(perangkat):
    """
    Menghitung total kWh harian dan bulanan dari seluruh perangkat.
    """
    total_kwh_harian = 0

    for nama, daya, durasi in perangkat:
        energi = (daya / 1000) * durasi  
        total_kwh_harian += energi
    
    total_kwh_bulanan = total_kwh_harian * 30
    return total_kwh_harian, total_kwh_bulanan


def tampilkan_hasil(kwh_harian, kwh_bulanan):
    """
    Menampilkan hasil lengkap konsumsi energi dan biaya listrik.
    """
    biaya = hitung_biaya(kwh_bulanan)

    print("\n=== HASIL PERHITUNGAN ===")
    print(f"Total konsumsi energi harian : {kwh_harian:.2f} kWh")
    print(f"Total konsumsi energi bulanan: {kwh_bulanan:.2f} kWh")
    print(f"Estimasi biaya listrik bulanan: Rp {biaya:,.0f}")


def main():
    perangkat = input_data()
    kwh_harian, kwh_bulanan = hitung_energi(perangkat)
    tampilkan_hasil(kwh_harian, kwh_bulanan)

if __name__ == "__main__":
    main()
