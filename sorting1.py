def bubbleSortStopIfNoSwap(listData):
    print('Data yang akan diurutkan : ', listData)
    count = 0
    n = len(listData)
    swapped = True  # Penanda apakah ada pertukaran data yang dilakukan
    while swapped:
        swapped = False
        count += 1
        print('Iterasi ke-', count,':')
        for i in range(n-1):
            if listData[i] > listData[i+1]:
                listData[i], listData[i+1] = listData[i+1], listData[i]
                swapped = True
        if not swapped:
            break  # Hentikan iterasi jika tidak ada pertukaran data yang dilakukan
        print(listData)
    print('Data urut-', listData)

# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
bubbleSortStopIfNoSwap(data)
