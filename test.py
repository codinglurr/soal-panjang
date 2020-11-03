arr = {'g':0, 'm':1, 's':2}
hasilAkhirAni = 0
hasilAkhirBudi = 0
#Lengkapi ... di bawah dengan sintaks yang sesuai
for i in range(1, 4):
    sesi = int(input(f"Input jumlah sesi untuk putaran ke-{i} :"))
    print("\n")
    skorAni = 0
    skorBudi = 0
    for j in range(1, sesi+1):
        inputAni = input()
        inputBudi = input()
        print("\n")
        if inputAni != inputBudi:
            result = (arr[inputAni]-arr[inputBudi]+5)%3
        if result == 1:
 #ani menang
            skorAni += 1
        elif result == 0:
 #budi menang
            skorBudi +=1
    if skorAni > skorBudi:
        win = "Ani"
        hasilAkhirAni += 1
    elif skorAni < skorBudi:
        win = "Budi"
        hasilAkhirBudi += 1
    else:
        win = "Tidak Ada, Hasil Seri"
    print(f"Sesi ke-{i} dimenangkan oleh :", win)
    print("\n")
if hasilAkhirAni > hasilAkhirBudi:
    win = "Ani"
elif hasilAkhirAni < hasilAkhirBudi:
    win = "Budi"
else:
     win = "Tidak Ada, Hasil Seri"
print(win)