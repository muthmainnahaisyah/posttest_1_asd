# NAMA = MUTHMAINNAH AISYAH
# NIM = 2209116001
# KELAS = SI-A

import os
os.system("cls")

variabel = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

# MERGE SORT

def flatten(variabel):
    if isinstance(variabel, list):
        listkosong = []
        for i in variabel:
            listkosong.extend(flatten(i))
        return listkosong
    else:
        return [variabel]

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

print("List belum terurut:")
print(variabel)
print("List sudah terurut:")
list_baru = flatten(variabel)
hasil = mergeSort(list_baru)
print(hasil)