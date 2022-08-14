# kỹ thuật nhánh cận dãy ABC
import math

def test(i):
    for long in range(1,math.ceil(i/2)+1,1):
        str1=""
        str2=""
        for index in range(i,i-long,-1):
            str1+=result[index]
            str2+=result[index-long]
        if (str1==str2): return False
    return True

 

def Attempt(i):
    global resultBest
    global countBest
    global count
    if (count> countBest):
        return
    for char in charArr:
        result.append(char)
        if (char=="C"): count+=1
        if test(i):
            if (i==n-1):
                if (count<countBest):
                    resultBest= result.copy()
                    countBest=count
            else:
                Attempt(i+1)
        if (char=="C"): count-=1
        result.pop(i)

# read file input
with open('C:/Users/nghuy/OneDrive/Desktop/học thuật toán/P1. Bài toán liệt kê/p_1_04_2/input.txt') as f:
    input = f.readline()
    f.close()


# init
charArr= ["A","B","C"]
result=[]
resultBest=[]
count=0
n = int(input)
countBest = n

Attempt(0)
print(resultBest)