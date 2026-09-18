def hitung_total_panen(jumlah_panen, harga_per_kg):
    total = jumlah_panen * harga_per_kg
    return total


def hitung_diskon(total, persen_diskon):
    diskon = total * persen_diskon / 100
    total_setelah_diskon = total - diskon
    return total_setelah_diskon


jumlah_panen = 100
harga_per_kg = 5000
persen_diskon = 10

total = hitung_total_panen(jumlah_panen, harga_per_kg)
total_akhir = hitung_diskon(total, persen_diskon)

print("Jumlah panen:", jumlah_panen, "kg")
print("Harga per kg: Rp", harga_per_kg)
print("Total nilai panen: Rp", total)
print("Diskon:", persen_diskon, "%")
print("Total setelah diskon: Rp", total_akhir)