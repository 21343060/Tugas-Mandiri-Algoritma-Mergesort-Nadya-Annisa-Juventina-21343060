def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
    #fungsi pertama digunakan untuk  mwnghitung panjang dari dua buat sub array

	# selanjutnya membuat dua array sementara yang digunakan untuk menampung elemen dari dua subarray itu
	L = [0] * (n1)
	R = [0] * (n2)

    # kemudian menyalin elemen dari dua subarray ke dalam array sementara yaitu L dan R 
    # serta kembali ke arr array asli, dalam urutan yang diurutkan
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# tahap penggabungan kembali[l..r]
	i = 0	 # Ini meruapakan index pertama dari subarray 
	j = 0	 # Ini merupakan index kedua dari subarray
	k = l	 # Ini merupakan index ketiga dari subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
			k += 1
    # pada bagian ini akan menjalankan sebuah algoritma yang menyalin elemen-elemen yang tersisa dari sub-array kiri(L) ke array asli
    #Loop ini akan terus berjalan hingga semua elemen dari kedua sub-array telah diproses dan disalin ke dalam array asli secara terurut
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

    # pada bagian ini, algoritma menyalin elemen - elemen yang tersisa dari sub-array kanan(R) ke array asli
    #Loop ini akan terus berjalan hingga semua elemen dari kedua sub-array telah diproses dan disalin ke dalam array asli secara terurut
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# L digunakan untuk indeks kiri dan r untuk indeks kanan
#sub-array dari arr yang akan diurutkan serta m merupakan indeks  tengah dari array

def mergeSort(arr, l, r):
	if l < r:

		m = l+(r-l)//2

		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# pada langkah dibawah ini dilakukannya sebauh pengujian untuk meenghasilkan array yang terurut
arr = [27, 3, 8, 21, 53, 1, 15, 6]
n = len(arr)
print("Data Sebelum Diurutkan")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nData Sesudah Diurutkan")
for i in range(n):
	print("%d" % arr[i],end=" ")

