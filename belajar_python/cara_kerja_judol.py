kasih_menang = 3
persentase = 1
i = 0

while i < kasih_menang :
    print("Anda Menang")
    i += 1

for i in range(kasih_menang + 1):
    persentase = persentase - 0.25
    print("Persentase kemenangan Anda adalah", persentase, "%")
    i -= 1

