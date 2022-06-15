#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

arr=input().split(' ')
n=int(arr[0])
m=int(arr[1])

list=[]
for i in range(0,n):
    arr=input().split(' ')
    list.append(arr)

a=numpy.array(list)
a=a.astype(numpy.float)

print(numpy.mean(a, axis = 1))
print(numpy.var(a,axis=0))
print(round(numpy.std(a),11))
