import numpy as np
import matplotlib.pyplot as plt
import time

t=time.time()
print(t)
x=np.random.rand(10000)
t2=time.time()

plt.subplots()
plt.plot(x,'o')
plt.hist(x,density='True')
plt.subplots()
plt.hist(x,density='True')
plt.show()

