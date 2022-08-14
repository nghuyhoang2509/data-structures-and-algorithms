# kỹ thuật nhánh cận dành cho bài toán du lịch


def Attempt(i):
    global bestconfig
    global result
    if (bestconfig < t[i-2]):
        return
    for index in range(2, n+1, 1):
        if (mark[index-1]) and (c[d[i-2]-1][index-1] != maxc):
            mark[index-1] = False
            d.append(index)
            t.append(t[i-2]+c[d[i-2]-1][index-1])
            if (i == n):
                if (c[index-1][0] != maxc):
                    if (bestconfig> t[i-1]):
                        bestconfig=t[i-1]
                        result=d.copy()
                else:
                    break  
            Attempt(i+1)
            d.remove(index)
            t.pop(i-1)
            mark[index-1] = True


# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1. Bài toán liệt kê/p_1_04_1/input.txt') as f:
    input = f.readlines()
    f.close()


# init
n = int(input[0].split()[0])
m = int(input[0].split()[1])
c = []
t = [0]
mark = []
d = [1]
result=[]
maxc = 100*100001
bestconfig = maxc
for i in range(0, n, 1):
    mark.append(True)
    c.append([])
    for j in range(0, n, 1):
        c[i].append(maxc)
for i in range(1, m+1, 1):
    a = input[i].split()
    c[int(a[0])-1][int(a[1])-1] = int(a[2])
    c[int(a[1])-1][int(a[0])-1] = int(a[2])


Attempt(2)
result.append(1)
print(result)
print('cost: ',bestconfig)
