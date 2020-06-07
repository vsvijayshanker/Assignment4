import numpy as np
import matplotlib.pyplot as plt

n=10000
x=np.random.random(n)
y=np.random.random(n)
a=4/n   #area of single spot

def f(x,y):
    return x**2+y**2

x=2*x-1     #x has range -1 to +1 for unit radius
y=2*y-1     #y has range -1 to +1 for unit radius

l=f(x,y)    
print(l)
A=0
for i in range(n):
    if l[i]<1:      #condition for counting the spot
        A=A+1       #total no of spots under the circle


A=A*a #total are inside the circle
print(A)
plt.subplots()
plt.scatter(x,y,color='red')
plt.show()
