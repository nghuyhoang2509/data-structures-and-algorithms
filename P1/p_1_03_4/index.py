# thuật toán quay lui liệt kê các cách phân tích số
def Attempt(i,sum,index):
    for x in range(index, n+1, 1):
        result.append(x)
        if (i != n-1) and (n-sum >= 2*x):
            Attempt(i+1,sum+x,x)
        if (n-sum == result[i]):
            for l in range(0,i+1,1):
                if l==0:
                    print(result[l],end="")
                else: print(' +',result[l],end="")
            print()
            result.pop(i)
            break
        result.pop(i)



# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1/p_1_03_4/input.txt') as f:
    input = f.readline()
    f.close()


n = int(input)

if not(n == 0):
    result = []
   
    Attempt(0,0,1)
