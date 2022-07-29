# thuật toán sinh liệt kê các dãy nhị phân độ dài n


# read file input

with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1/p_1_02_1/input.txt') as f:
    input = f.read()
    f.close()

test = False
input = int(input)

# create string n char
numberStr = ""
for i in range(input):
    numberStr += "0"


index = input-1
while index>=0 :
    print(numberStr)
    index = input-1
    while (index >= 0) and (numberStr[index] == "1"):
        index -= 1
    if (index >= 0):
        if (index< input-1):
            numberStr = numberStr[:index] + "1" + numberStr[index:]
        else:
            numberStr = numberStr[:index] + "1" 
        numberNew = ""
        if (index< input-1):
            for i in range(input-1-index):
                numberNew+="0"
        numberStr= numberStr[:index+1] + numberNew
