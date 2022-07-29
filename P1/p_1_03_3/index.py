# thuật toán quay lui liệt kê chỉnh hợp không lặp chập k
def Attempt(i):
    for x in arrAva:
        if not(x in set):
            result[i]=x
            set.add(x)
            if (i==k-1):
                print(result)
            else:
                Attempt(i+1)
            set.remove(x)

# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1/p_1_03_3/input.txt') as f:
    input = f.readline().split()
    f.close()


n = int(input[0])
k = int(input[1])

if not(k==0):
    set=set()
    result=[]
    arrAva=[]
    for i in range(1,n+1,1):
        arrAva.append(i)
    for i in range(0,k,1):
        result.append(0)
    Attempt(0)



