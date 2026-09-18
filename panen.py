def hitung_total_panen(jumlah_panen, harga_per_kg):
    total = jumlah_panen * harga_per_kg
    return total


jumlah_panen = 100
harga_per_kg = 5000

total = hitung_total_panen(jumlah_panen, harga_per_kg)

print("Jumlah panen:", jumlah_panen, "kg")
print("Harga per kg: Rp", harga_per_kg)
print("Total nilai panen: Rp", total)