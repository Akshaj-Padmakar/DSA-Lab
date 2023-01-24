#Selection Sort

Arr = [28999, 1600, 1100, 1400, 800, 1200, 2300, 669, 3600, 1, 186, 299, 25, 3300, 2599, 1008, 900, 169, 607, 1280]

count = 0

for i in range(len(Arr)):
	
	min_index = i
	for j in range(i+1, len(Arr)):
		if Arr[min_index] > Arr[j]:
			min_index = j
			
	if(i != min_index):		
	    Arr[i], Arr[min_index] = Arr[min_index], Arr[i]
	    count += 1

print ("Sorted array")
for i in range(len(Arr)):
	print("%d" %Arr[i],end=" ")
	
print("\n")
print("The number of iterations are " + str(count))
