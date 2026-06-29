def merge_sort(arr, adim=[1]):
    if len(arr) > 1:
        mid = len(arr) // 2
        sol_yari = arr[:mid]
        sag_yari = arr[mid:]

        merge_sort(sol_yari, adim)
        merge_sort(sag_yari, adim)

        i = j = k = 0

        while i < len(sol_yari) and j < len(sag_yari):
            if sol_yari[i] < sag_yari[j]:
                arr[k] = sol_yari[i]
                i += 1
            else:
                arr[k] = sag_yari[j]
                j += 1
            k += 1

        while i < len(sol_yari):
            arr[k] = sol_yari[i]
            i += 1
            k += 1

        while j < len(sag_yari):
            arr[k] = sag_yari[j]
            j += 1
            k += 1
        
        print(f"{adim[0]}. Birleştirme Adımı: {arr}")
        adim[0] += 1

ornek_dizi = [16, 21, 11, 8, 12, 22]
print(f"İlk Hali: {ornek_dizi}")
print("-" * 45)
merge_sort(ornek_dizi)