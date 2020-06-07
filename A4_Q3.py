import numpy as np
import matplotlib.pyplot as plt
import time

start1=time.time()

a  = 18871222
x0 = 19311015
c  = 19091030
m  = 19940814

n=100000
x=np.zeros(n)
k=np.linspace(0,n,n)
for i in range(n-1):
    x[0]=x0
    x[i+1]=(a*x[i]+c)%m

x=x/m
print(x)
end1=time.time()

start2=time.time()
x2=np.random.rand(n)
end2=time.time()

print('execution time for linear congruential random number generator is\n',end1-start1,'seconds\n')
print('execution time for numpy library function is',end2-start2,'seconds\n')
print('library code is',(end1-start1)/(end2-start2),'times faster\n')

