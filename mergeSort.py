#FUNCIONAAAA
def merge(iz, de, arr):
	n_iz = len(iz)
	n_de = len(de)
	i,j,k = 0,0,0	
	while(i < n_iz and j < n_de):
		if(iz[i] <= de[j]):
			arr[k] = iz[i]
			k += 1
			i += 1
		else:
			arr[k] = de[j]
			j += 1
			k +=1
	while(i < n_iz):
		arr[k] = iz[i]
		i += 1
		k += 1
	while(j < n_de):
		arr[k] = de[j]
		j += 1
		k += 1

def merge_sort(arr):
	n = len(arr)
	if(n < 2):
		return  
	mitad = n // 2
	iz = [0] * mitad
	de = [0] * (n - mitad)	

	i = 0
	for i in range(0, mitad):		
		iz[i] = arr[i]
	for i in range (mitad, n):
		de[i-mitad] = arr[i]
	
	merge_sort(iz)
	merge_sort(de)
	merge(iz, de, arr)

arr = [0 ,-2020, 7, -125, 6 , 2]
merge_sort(arr)
print(arr)