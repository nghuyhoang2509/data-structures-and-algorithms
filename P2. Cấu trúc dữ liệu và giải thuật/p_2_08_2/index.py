# Các thuật toán sắp xếp


# SelectionSort
def SelectionSort(arr, n):
    for i in range(0, n-1, 1):
        imin = i
        for j in range(i+1, n, 1):
            if arr[j] < arr[imin]:
                imin = j
        temp = arr[i]
        arr[i] = arr[imin]
        arr[imin] = temp
    return arr


# BubbleSort
def BubbleSort(arr, n):
    for i in range(0, n-2, 1):
        for j in range(n-1, i, -1):
            if (arr[j] < arr[j-1]):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    return arr


# InsertionSortwithBinarySearching
def InsertionSortwithBinarySearching(arr, n):
    for i in range(1, n, 1):
        before = 0
        end = i
        while before <= end:
            medium = (before + end)//2
            if (arr[medium] < arr[i]):
                before = before + 1
            else:
                end = end - 1
        arr.insert(before, arr.pop(i))
    return arr


# ShellSort
def ShellSort(arr, n):
    distance = n // 2
    while distance != 0:
        for i in range(distance, n, 1):
            j = i-distance
            temp = arr[i]
            while j >= 0 and temp < arr[j]:
                arr[i] = arr[j]
                arr[j] = temp
                j -= distance
        distance = distance // 2
    return arr


# QuickSort
def QuickSort(arr, n):
    def partition(s, e):
        if s >= e:
            return
        arrPivot = [arr[s], arr[e], arr[(s+e)//2]]
        arrPivot.sort()
        pivot = arrPivot[1]
        i = s
        j = e
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                if i < j:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                i += 1
                j -= 1
        partition(s, j)
        partition(i, e)
    partition(0, n-1)
    return(arr)


# HeapSort
def HeapSort(arr, n):
    def Adjust(r, e):
        if (2*r+2<=e):
            if (arr[2*r+1] > arr[2*r+2]):
                if (arr[r] < arr[2*r+1]):
                    temp = arr[2*r+1]
                    arr[2*r+1] = arr[r]
                    arr[r] = temp
                    Adjust(2*r+1,e)
            else:
                if (arr[r] < arr[2*r+2]):
                    temp = arr[2*r+2]
                    arr[2*r+2] = arr[r]
                    arr[r] = temp
                    Adjust(2*r+2,e)
        elif (2*r+1<=e):
            if (arr[2*r+1]>arr[r]):
                temp = arr[r]
                arr[r] = arr[2*r+1]
                arr[2*r+1] = temp

    for r in range(n // 2 - 1, -1, -1):
        Adjust(r, n-1)
    for i in range(n-1, -1, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        Adjust(0, i-1)
    return arr


# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P2. Cấu trúc dữ liệu và giải thuật/p_2_08_2/input.txt') as f:
    input = f.readline()
    input = input.split()
    f.close()

n = int(input[0])
arr = input[1:].copy()
print(HeapSort(arr, n))
