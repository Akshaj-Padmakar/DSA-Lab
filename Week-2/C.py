# Python program for implementation of MergeSort
def mergeSort(arr):
    ans = 0
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        a1 = mergeSort(L)

        # Sorting the second half
        a2 = mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                ans+=1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        ans += a1 + a2
    return ans


# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [28999, 1600, 1100, 1400, 800, 1200, 2300, 669, 3600, 1, 186, 299, 25, 3300, 2599, 1008, 900, 169, 607, 1280]

    print("Given array is", end="\n")
    printList(arr)
    a = mergeSort(arr)
    a-=2
    print(a)
    print("Sorted array is: ", end="\n")
    printList(arr)

# This code is contributed by Mayank Khanna
