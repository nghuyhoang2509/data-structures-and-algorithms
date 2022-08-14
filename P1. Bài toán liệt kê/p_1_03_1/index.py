# thuật toán quay lui liệt kê các dãy nhị phân độ dài n 

def Attempt(i):
    for x in arrAvailable:
        result[i]=x
        if not(i==n):
            Attempt(i+1)
        else:
            print(result)


# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1. Bài toán liệt kê/p_1_03_1/input.txt') as f:
    input = f.read()
    f.close()


n = int(input)-1

if not(n==-1):
    arrAvailable=[0,1]
    result=[]
    for i in range(n+1):
        result.append("")
    Attempt(0)



