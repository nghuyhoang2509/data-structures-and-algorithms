# thuật toán sinh liệt kê hoán vị

# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1. Bài toán liệt kê/p_1_02_3/input.txt') as f:
    input = f.readline()
    f.close()


n = int(input)


result = []
for index in range(n):
    result.append(index+1)

index=n-1

while index>=0:
    print(result)
    index= n-1
    if (index==n-1):
        index-=1
    while (index>=0) and (result[index]> result[index+1]):
        index-=1
    if (index>=0):
        c=result[index]

        # sort arr
        arrTempStart=result[:(index)]
        arrTempEnd=result[index:]
        arrTempEnd.sort()
        arrTempStart.extend(arrTempEnd)
        result= arrTempStart.copy()

        #swap
        i=result.index(c,index)
        d=result[i+1]
        result.pop(i+1)
        result.insert(index,d)
        
        





