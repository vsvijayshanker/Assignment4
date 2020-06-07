import numpy as np
import matplotlib.pyplot as plt
import scipy
import time

a  = 18871222
x0 = 19311015
c  = 19091030
m  = 19940814

n=10000
x=np.zeros(n)
k=np.linspace(0,n,n)
for i in range(n-1):
    x[0]=x0
    x[i+1]=(a*x[i]+c)%m

x=x/m
print(x)


plt.subplots()
plt.scatter(k,x,marker='o',s=0.1,color='red',label='random number 0-1')
plt.subplots()
plt.hist(x,density='True')
#plt.legend()
plt.show()
