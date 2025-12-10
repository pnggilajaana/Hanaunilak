"""
Modul Manajemen Listrik Rumah Tangga
Berisi fungsi-fungsi untuk menghitung konsumsi energi, biaya listrik, efisiensi peralatan,
dan analisis penggunaan listrik bulanan.
"""

# =============================
# 1. Perhitungan Konsumsi Energi
# =============================

def konsumsi_harian(daya_watt, jam_pemakaian):
    """
    Menghitung konsumsi energi harian suatu peralatan.

    Args:
        daya_watt (float/int): Daya perangkat dalam watt
        jam_pemakaian (float): Lama penggunaan per hari

    Returns:
        float: Konsumsi energi harian dalam kWh
    """
    return (daya_watt * jam_pemakaian) / 1000


def konsumsi_bulanan(daya_watt, jam_pemakaian, hari=30):
    """
    Menghitung konsumsi energi bulanan suatu peralatan.

    Args:
        daya_watt (float/int): Daya perangkat dalam watt
        jam_pemakaian (float): Lama penggunaan per hari
        hari (int): Jumlah hari dalam sebulan (default: 30)

    Returns:
        float: Konsumsi energi bulanan dalam kWh
    """
    return konsumsi_harian(daya_watt, jam_pemakaian) * hari

# =============================
# 2. Perhitungan Biaya
# =============================

def hitung_biaya(energi_kwh, tarif=1500):
    """
    Menghitung biaya listrik berdasarkan konsumsi energi.

    Args:
        energi_kwh (float): Total energi yang digunakan dalam kWh
        tarif (int/float): Harga per kWh (default: 1500)

    Returns:
        float: Total biaya listrik
    """
    return energi_kwh * tarif

# =============================
# 3. Analisis Peralatan
# =============================

def estimasi_biaya_peralatan(daya_watt, jam_pemakaian, tarif=1500, hari=30):
    """
Mengestimasi biaya bulanan penggunaan suatu perangkat listrik rumah tangga.

    Args:
        daya_watt (float/int)
        jam_pemakaian (float)
        tarif (int/float)
        hari (int)

    Returns:
        float: Estimasi biaya bulanan
    """
    energi = konsumsi_bulanan(daya_watt, jam_pemakaian, hari)
    return hitung_biaya(energi, tarif)


def perbandingan_peralatan(daftar_peralatan):
    """
    Membandingkan konsumsi energi beberapa peralatan.

    Args:
        daftar_peralatan (list of dict):
            Format contoh:
            [
                {"nama": "AC", "daya": 350, "jam": 8},
                {"nama": "Kulkas", "daya": 150, "jam": 24}
            ]

    Returns:
        list: Daftar hasil analisis energi
    """
    hasil = []
    for p in daftar_peralatan:
        energi = konsumsi_bulanan(p["daya"], p["jam"])
        hasil.append({
            "nama": p["nama"],
            "konsumsi_kwh": energi,
            "biaya": hitung_biaya(energi)
        })
    return hasil

# =============================
# 4. Main Demo
# =============================

if __name__ == "__main__":
    print("Testing Modul Manajemen Listrik Rumah Tangga")

    # Contoh 1: Hitung konsumsi harian & bulanan
    print("Konsumsi Harian Lampu 10W selama 5 jam =", konsumsi_harian(10, 5), "kWh")
    print("Konsumsi Bulanan Lampu =", konsumsi_bulanan(10, 5), "kWh")

    # Contoh 2: Estimasi biaya
    biaya = estimasi_biaya_peralatan(350, 8)  # AC 350W, dipakai 8 jam per hari
    print("Estimasi biaya AC per bulan = Rp", biaya)

    # Contoh 3: Analisis beberapa peralatan
    peralatan = [
        {"nama": "AC", "daya": 350, "jam": 8},
        {"nama": "Kulkas", "daya": 150, "jam": 24},
        {"nama": "TV", "daya": 80, "jam": 4}
    ]

    analisis = perbandingan_peralatan(peralatan)
    print("Analisis Peralatan:")
    for a in analisis:
        print(f"{a['nama']} - {a['konsumsi_kwh']} kWh - Rp {a['biaya']}")
    