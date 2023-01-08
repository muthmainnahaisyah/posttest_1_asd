# NAMA = MUTHMAINNAH AISYAH
# NIM = 2209116001
# KELAS = SI-A

import os
os.system("cls")

variabel = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

# QUICK SORT

def flatten(variabel):
    if isinstance(variabel, list):
        listkosong = []
        for i in variabel:
            listkosong.extend(flatten(i))
        return listkosong
    else:
        return [variabel]

def partition(l, bwh, atas):
    pivot = l[bwh]
    pos_batas = bwh+1
    for j in range(bwh+1,atas):
        if l[j] < pivot:
            l[pos_batas],l[j]=l[j],l[pos_batas]
            pos_batas += 1
    l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
    return pos_batas

def quicksort(l, bwh, atas):
    if atas <= bwh:
        return
    q = partition(l, bwh, atas)
    quicksort(l, bwh, q-1)
    quicksort(l, q, atas)
    return l

print("Sebelum diurutkan =")
print(variabel)
print("Setelah diurutkan =")
list_baru = flatten(variabel)
akhir = quicksort(list_baru, 0, len(list_baru)-1)
print(akhir)
