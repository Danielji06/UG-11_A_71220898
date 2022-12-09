Nama = input("Masukkan nama: ")
muncul = 0
for i in range(len(Nama)):
    muncul +=1
    print(Nama[:muncul])
for i in range(len(Nama)):
    muncul -=1
    print(Nama[:muncul])