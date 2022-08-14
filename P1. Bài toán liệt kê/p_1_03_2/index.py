# thuật toán quay lui liệt kê các tập con k phần tử
def Attempt(i):
    if (i==0):
        index=1
    else:
        index=result[i-1]+1
    for x in range(index,n+1,1):
        result[i]=x
        if (i==k-1):
            print(result)
        else:
            Attempt(i+1)



# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1. Bài toán liệt kê/p_1_03_2/input.txt') as f:
    input = f.readline().split()
    f.close()


n = int(input[0])
k = int(input[1])

result = []

if not(k==0):
    for index in range(k):
        result.append(0)
    Attempt(0)
