def bidirectionalBubbleSort(listData):
    print('Data yang akan diurutkan : ', listData)
    count = 0
    n = len(listData)
    left = 0
    right = n - 1
    while left < right:
        count += 1
        print('Iterasi ke-', count,':')
        for i in range(left, right):  # Pointer bergerak dari kiri ke kanan
            if listData[i] > listData[i+1]:
                listData[i], listData[i+1] = listData[i+1], listData[i]
        right -= 1  # Data terbesar sudah berada di indeks terakhir, kurangi panjang rentang
        for i in range(right, left, -1):  # Pointer bergerak dari kanan ke kiri
            if listData[i] < listData[i-1]:
                listData[i], listData[i-1] = listData[i-1], listData[i]
        left += 1  # Data terkecil sudah berada di indeks pertama, tambahkan panjang rentang
        print(listData)
    print('Data urut-', listData)

# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
bidirectionalBubbleSort(data)
