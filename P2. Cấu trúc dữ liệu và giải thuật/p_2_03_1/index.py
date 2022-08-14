# Đệ quy giải tháp hà nội


def move(n,x,y,z):
    if n==1:
        print('transfer plate',n,'from col',x,'to col',y)
        return
    move(n-1,x,z,y)
    print('transfer plate',n,'from col',x,'to col',y)
    move(n-1,z,y,x)



# read file input

with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P2. Cấu trúc dữ liệu và giải thuật/p_2_03_1/input.txt') as f:
    input = f.read()
    f.close()

n = int(input)

move(n,'a','c','b')
