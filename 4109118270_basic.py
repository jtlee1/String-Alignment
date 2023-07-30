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
def main():
    #AG,CT=48 AT=94 AC,GT=110 CG=118
    skip = 30
    tex = sys.argv[1]
    t1 = read(tex)
    t2 = create_string(t1)
    list1 = []
    list2 = []
    rip1 = len(t2[0])
    rip2 = len(t2[1])
    for x in range(rip1):
        for y in range(rip2):
            list1.append(x)
        list2.append(list1)
        list1 = []
    #t2 = ["TATTATTT","AGAA"]
    #t2 = ["AGA","AA"]
    arr = np.full((len(t2[0])+1,len(t2[1])+1),0)
    #ar = [1] * (100000)
    t2[0] = '@'+t2[0]
    t2[1] = '@'+t2[1]
    
    for x in range(len(t2[0])):
        arr[x][0] = 30*x
    for x in range(len(t2[1])):
        arr[0][x] = 30*x
    
    for x in range(len(t2[0])-1):
        for y in range(len(t2[1])-1):
            #if x==0 and y==0:
            #arr[x+1][y+1] = 0
            #else:
                c1 = cost(t2[0][x+1],t2[1][y+1])
                arr[x+1][y+1] = min(arr[x][y]+c1,arr[x][y+1]+skip,arr[x+1][y]+skip)
                    #if x==1 and y==1:
                    #print(c1)
    t = max(len(t2[0]),len(t2[1]))
    f = 0
    s = 0
    
    str1 = ""
    str2 = ""
    while f!=len(t2[0])-1 or s!=len(t2[1])-1:
        if f==len(t2[0])-1:
            #str1 += '_'
            str2 += t2[1][-s-1]
            str1 += '_'
            s += 1
        elif s==len(t2[1])-1:
            #str1 += 'I'
            str1 += t2[0][-f-1]
            str2 += '_'
            f += 1
        else:
            v = arr[-2-f][-1-s]
            h = arr[-1-f][-2-s]
            d = arr[-2-f][-2-s]
            if t2[0][-f-1] == t2[1][-s-1]:
                
                str1 += t2[0][-f-1]
                str2 += t2[1][-s-1]
                f += 1
                s += 1
            elif d<=v and d<=h and cost(t2[0][-1-f],t2[1][-1-s]) == arr[-1-f][-1-s]-arr[-2-f][-2-s]:
                str1 += t2[0][-f-1]
                str2 += t2[1][-s-1]
                f += 1
                s += 1
            elif arr[-1-f][-1-s] == arr[-1-f][-2-s] + skip:
                #str1 += '-'
                str2 += t2[1][-s-1]
                str1 += '_'
                s += 1
            elif arr[-1-f][-1-s] == arr[-2-f][-1-s] + skip:
                #print(str(h)+','+str(v)+','+str(d))
                #str1 += '|'
                str1 += t2[0][-f-1]
                str2 += '_'
                f += 1
            else:
                print("ERROR")
                print(d)
                print(cost(t2[0][-1-f],t2[1][-1-s]))
                print(h)
                print(v)
                print(arr[-1-f][-1-s])
       
    #finals = max(len(t2[0])-1,len(t2[1])-1)
    
    txt1 = str1[::-1]
    txt2 = str2[::-1]
    
    
        
    
        
   
    s1 = txt1[:50]+' '+txt1[-50:]
    s2 = txt2[:50]+' '+txt2[-50:]
    #globres = arr[-1][-1]
    return(arr[-1][-1],s1,s2)


#main()
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



