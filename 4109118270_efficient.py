import numpy as np
import time
import os
import psutil
import memory_profiler as mp
import sys





def read(x):
    with open(x) as f:
        line = f.readlines()
    for y in range(len(line)):
        line[y] = line[y].strip('\n')
    return line

def insert(s,p):
    return s[:p]+s+s[p:]

def create_string(x):
    arr = ['','']
    flag = 0
    for y in x:
        if y.isnumeric():
            arr[flag-1] = insert(arr[flag-1],int(y)+1)
        else:
            arr[flag] = y
            flag = flag+1
    return arr

def myfunc(): 
    x = 1
    if x == 1:
        print("x is 1.")

def cost(y,z):
    x = y+z;
    #AG,CT=48 AT=94 AC,GT=110 CG=118
    arr = [0,48,94,110,118]
    if y=="@" or z=="@":
        return np.inf
    elif x=="AG" or x=="CT" or x=="GA" or x=="TC":
        return 48
    elif x=="AT" or x=="TA":
        return 94
    elif x=="AC" or x=="GT" or x=="CA" or x=="TG":
        return 110
    elif x=="CG" or x=="GC":
        return 118
    else:
        return 0

#profile(precision=80)
def getali(x,y):
    t2 = [[0],[0]]
    t2[0] = x
    t2[1] = y
    #AG,CT=48 AT=94 AC,GT=110 CG=118
    skip = 30
    #t1 = read('input2.txt')
    #t2 = create_string(t1)
    #t2 = ["TATTAT","AAA"]
    #t2 = ["AAA","AAG"]
    #arr = np.full((len(t2[0])+1,len(t2[1])+1),0)
    arr = np.full((2,len(t2[1])+1),0)
    #ar = [1] * (100000)
    t2[0] = '@'+t2[0]
    t2[1] = '@'+t2[1]
    
    '''for x in range(len(t2[0])):
        arr[x][0] = 30*x'''
    for x in range(len(t2[1])):
        arr[0][x] = 30*x
    
    for x in range(len(t2[0])-1):
        arr[1][0] = (x+1)*30
        for y in range(len(t2[1])-1):
            #if x==0 and y==0:
            #arr[x+1][y+1] = 0
            #else:
            c1 = cost(t2[0][x+1],t2[1][y+1])
            arr[1][y+1] = min(arr[0][y]+c1,arr[1][y]+skip,arr[0][y+1]+skip)
                    #if x==1 and y==1:
                    #print(c1)
        #print("before")
        #print(arr)
        arr[[0,1]] = arr[[1,0]]
    #print(arr)
    #print(arr[0][-1])
    #print(arr[0])
    return(arr[0])
    
def dac(x,y):
    skip = 30
    str = ["",""]
    if len(x) == 0:
        #print("A")
        for i in range(len(y)):
            str[0] += '_'
            str[1] += y[i]
    elif len(y) == 0:
        #print("B")
        for i in range(len(x)):
            str[1] += '_'
            str[0] += x[i]
    elif len(x) == 1:
        #print("C")
        flag = 0
        cos = np.inf
        idx = 0
        for i in range(len(y)):
            temp = min(cost(x[0],y[i]),cos,2*skip)
            if temp!=cos:
                idx = i
            cos = temp
        if cos == 2*skip:
            str[0] += x[0]
            str[1] += '_'
            for i in range(len(y)):
                str[0] += '_'
                str[1] += y[i]
        else:
            for i in range(len(y)):
                if i == idx:
                    str[0] += x[0]
                    str[1] += y[i]
                else:
                    str[0] += '_'
                    str[1] += y[i]
    elif len(y) == 1:
        #print("D")
        flag = 0
        cos = np.inf
        idx = 0
        for i in range(len(x)):
            temp = min(cost(x[i],y[0]),cos,2*skip)
            if temp!=cos:
                idx = i
            cos = temp
        if cos == 2*skip:
            str[0] += '_'
            str[1] += y[0]
            for i in range(len(x)):
                str[0] += x[i]
                str[1] += '_'
        else:
            for i in range(len(x)):
                if i == idx:
                    str[0] += x[i]
                    str[1] += y[0]
                else:
                    str[0] += x[i]
                    str[1] += '_'
    else:
        fx = x[:len(x)//2]
        xmid = int(len(x)/2)
        lx = x[len(x)//2:]
        rlx = lx[::-1]
        ry = y[::-1]
        L = getali(fx,y)
        R = getali(rlx,ry)
        rR = R[::-1]
        ymid = np.argmin(L+rR)
        #print("XXXX")
        #print(ymid)
        te1 = dac(x[:xmid],y[:ymid])
        te2 = dac(x[xmid:],y[ymid:])
        str[0] = te1[0]+te2[0]
        str[1] = te1[1]+te2[1]
    return str


def main():
    tex = sys.argv[1]
    t1 = read(tex)
    t2 = create_string(t1)
    
    list1 = []
    list2 = []
    rip1 = len(t2[0])
    rip2 = 2
    for x in range(rip1):
        for y in range(rip2):
            list1.append(x)
        list2.append(list1)
        list1 = []
    #t2 = ["GGGG","AAAAAAAA"]
    #t2[0] = t2[0][::-1]
    #t2[1] = t2[1][::-1]
    #t2[0] = t2[0][:len(t2[0])//2] #str
    #t2[0] = t2[0][len(t2[0])//2:] #ing
    c = getali(t2[0],t2[1])
    
    str1 = dac(t2[0],t2[1])
    #str1 = ["AAA","AGA"]
    s1 = str1[0][:50]+' '+str1[0][-50:]
    s2 = str1[1][:50]+' '+str1[1][-50:]
    #print("before1: " + str1[0][:50])
    #print("after1: " + str1[0][-50:])
    #print("len1: " + str(len(t2[0]))+ " , "+ str(len(str[0])))
    #print("before2: " + str(c[-1]))
    #print("after2: " + str[1])
    #print("len2: " + str(len(t2[1]))+ " , "+ str(len(str[1])))
    return str(c[-1]),s1,s2

def getmem():
    start_mem = mp.memory_usage(max_usage=True)
    res = mp.memory_usage(proc=(main, ), max_usage=True, retval=True)
    return start_mem,res

    
def gettime():
    start = time.process_time()
    c,s1,s2 = main()
    t = time.process_time() - start
    return t,c,s1,s2

t,c,s1,s2 = gettime()
start_mem,res = getmem()


with open('output.txt', 'w') as f:
    f.write(s1)
    f.write("\n")
    f.write(s2)
    f.write("\n")
    f.write(str(c))
    f.write("\n")
    f.write(str((res[0]-start_mem)*1048.576))
    f.write("\n")
    f.write(str(t))



#print('start mem', start_mem)
#print('max mem', res[0])
#print('used mem', res[0]-start_mem)
#
#print('return', res[1])
