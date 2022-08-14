# thuật toán sinh liệt kê các tập con k phần tử


# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1. Bài toán liệt kê/p_1_02_2/input.txt') as f:
    input = f.readline().split()
    f.close()


n = int(input[0])
k = int(input[1])

result = []
for index in range(k):
    result.append(index+1)
index = k-1


while index >= 0:
    print(result)
    index = k-1
    while (index>=0) and (result[index]==n-k+1+index):
        index-=1
    if (index>=0):
        result[index]+=1
        for i in range(index+1,k,1):
            result[i]= result[i-1]+1
