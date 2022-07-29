# thuật toán quay lui giải bài toán xếp hậu


def Attempt(x):
    for y in range(1, n+1, 1):
        if (cross1[x+y]) and (cross2[x-y+5]) and (col[y]):
            row[x] = y
            if (x == n):
                for index in range(1,n+1,1):
                    print('(',index,',',row[index],'); ',end="")
                print()
            else:
                cross1[x+y] = False
                cross2[x-y+5] = False
                col[y] = False
                Attempt(x+1)
                cross1[x+y] = True
                cross2[x-y+5] = True
                col[y] = True


# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1/p_1_03_5/input.txt') as f:
    input = f.readline()
    f.close()


n = int(input)
cross1 = []
cross2 = []
col = []
row = []
result = []
for i in range(0, 2*n+2, 1):
    row.append(True)
    col.append(True)
    cross1.append(True)
    cross2.append(True)

Attempt(1)
