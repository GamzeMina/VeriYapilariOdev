def insertion_sort(arr):
    n = len(arr)
    print(f"İlk Hali: {arr}")
    print("-" * 45)
    
    for i in range(1, n):
        anahtar = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > anahtar:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anahtar
        print(f"{i}. Adım (Seçilen Sayı: {anahtar:2d}): {arr}")

ornek_dizi = [22, 27, 16, 2, 18, 6]
insertion_sort(ornek_dizi)