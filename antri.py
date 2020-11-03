n,t = map(int,input().split())
inputAntri = list(input())
antrian = []
for x in range(n):
    # print(inputAntri[x])
    if inputAntri[x] == "L" or inputAntri[x] == "l":
        if inputAntri[t-1] == "P":
            antrian.insert(x+1,inputAntri[x])
        else:
            antrian.insert(t,inputAntri[x])
            
    else:
        antrian.insert(x-1,inputAntri[x])
for x in antrian:
    print(x,end="")
print()