# Tính giá trị biểu thức RPN


def setup():
    global RPN
    while (RPN.find("  ") >= 0):
        RPN = RPN.replace("  ", " ")
    i = 0
    while (i != len(RPN)):
        i += 1
        if (RPN[i-1] in "0123456789") and (RPN[i] in "0123456789"):
            continue
        if (RPN[i-1] != " "):
            RPN = RPN[:i] + " " + RPN[i:]
    while (RPN.find("  ") >= 0):
        RPN = RPN.replace("  ", " ")


# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P2. Cấu trúc dữ liệu và giải thuật/p_2_07_1/input.txt') as f:
    input = f.readline()
    f.close()

stack = []
RPN = input
temp = ""
setup()


for i in range(0, len(RPN), 1):
    if (RPN[i] in "0123456789"):
        temp += RPN[i]
        continue
    if (RPN[i] == " ") and (temp != ""):
        stack.append(temp)
        temp = ""
        continue
    if (RPN[i] != " "):
        x = stack.pop(len(stack)-1)
        y = stack.pop(len(stack)-1)
        z = RPN[i]
        if (z == '+'):
            stack.append(int(x)+int(y))
        elif (z == '-'):
            stack.append(int(y)-int(x))
        elif (z == '*'):
            stack.append(int(x)*int(y))
        else:
            stack.append(int(y)/int(x))

print(stack)