"""
Modul Hitung Biaya
Berisi fungsi pendukung untuk menghitung biaya listrik berdasarkan energi bulanan.
"""
def hitung_biaya(energi_bulanan, tarif=1500):
    """
    Menghitung biaya listrik bulanan.
    energi_bulanan : total kWh per bulan
    tarif : harga per kWh (default: 1500)
    """
    return energi_bulanan * tarif
