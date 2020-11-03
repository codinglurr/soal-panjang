budi = 0
ani = 0

# print(f"Pertandingan Babak Pertama, Nilai Soal untuk Budi")
# babak1 = 1
# while babak1 <= 10:
#     validasi = int(input(f"Masukkan nilai ke-{babak1} Budi: "))
#     if validasi == 0 or validasi == 100:
#         budi += validasi
#         babak1 += 1
#     else:
#         pass


# print(f"Pertandingan Babak Kedua, Nilai Soal untuk Ani")
# babak2 = 1
# while babak2 <= 10:
#     validasi = int(input(f"Masukkan nilai ke-{babak2} Ani: "))
#     if validasi == 0 or validasi == 100:
#         ani += validasi
#         babak2 += 1
#     else:
#         pass


print("Pertandingan Babak Ketiga, Ketikkan Nama Penjawab Soal")
nama = ''
skor = 0
for babak3 in range(1,10):
    nama = input("Masukkan nama penjawab, jika tidak ada, ketik q: ").lower()
    while nama == "budi" or nama == "ani":
        if nama != "q":
            while (skor == 0 or skor == 100):
                skor = int(input(f"Masukkan nilai soal ke {babak3}: "))
            else:
                continue
                
        if nama == "budi":
            budi += skor
        elif nama == "ani":
            ani += skor
        else:
            continue
    
print("Skor Ani :",ani)
print("Skor Budi :",budi)
win = ''
if ani > budi:
    win = "ani"
elif ani < budi:
    win = "budi"
else:
    win = "budi dan ani"
print("Pemenangnya adalah", win) 