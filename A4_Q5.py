import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(2/np.pi)*np.exp(-(x**2)/2)

n=500
x=np.random.rand(n)

y=f(x)

plt.subplots()
plt.plot(x,y,'o')
#plt.hist(y,density='True',color='red')

plt.show()
print(y)
