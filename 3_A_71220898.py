a = int(input("Masukkan pembatas: "))
b = int(input("Masukkan Angka Yang dilarang: "))
for i in range(a):
    if i == b:
        continue
    print (i, end=' ')