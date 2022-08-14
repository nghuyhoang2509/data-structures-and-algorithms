# Tính giá trị biểu thức RPN

def get(char):
    if (char in '('):
        return 0
    if (char in '+-'):
        return 1
    if (char in '*/'):
        return 2
    return 4


def push(ele):
    global stack
    if (get(ele) < get(stack[len(stack)-1])):
        elePrint = stack.pop()
        if (elePrint != "("):
            print(elePrint, end=" ")
    stack.append(ele)


# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P2. Cấu trúc dữ liệu và giải thuật/p_2_07_2/input.txt') as f:
    input = f.readline()
    f.close()

stack = []
exp = input
number = ""

while exp.find(" ") >= 0:
    exp = exp.replace(" ", "")

for i in range(0, len(exp), 1):
    if (exp[i] in "0123456789"):
        number += exp[i]
        continue
    if (exp[i]=='('): 
        stack.append(exp[i])
        continue
    if (exp[i] == ")"):
        if (number!=""):
            print(number,end=" ")
            number=""
        for j in range(len(stack)-1,-1,-1):
            if not(stack[j] in "()"):
                print(stack[j],end=" ")
        stack = []
        continue
    if (number == ""):
        if (stack==[]):
            stack.append(exp[i])
        else:
            push(exp[i])
        continue
    print(number, end=" ")
    push(exp[i])
    number = ""


