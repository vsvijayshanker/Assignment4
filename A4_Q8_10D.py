#volume of 10-D unit sphere
import numpy as np
import matplotlib.pyplot as plt

n=1000000
d=10
a=(2**d)/n #area of single spot

A=0
x=np.zeros((d,n))   #array of 10 dimensions
l=np.zeros(n)       #array for testing the distance from origin is less than 1

for i in range(d):
    x[i]=np.random.random(n) #creates 10 array of random numbers
    l=l+x[i]**2             #sum of xi**2 i is dimension
l=np.sqrt(l)                #array of distance from origin


for j in range(n):
    if l[j]<1:      #testing criteria counts if distance from origin is less than 1
        A=A+1


A=A*a   #total area of sphere of d no of dimensions


print('\nVolume of ',d, 'dimensional unit sphere is approximately',A)
