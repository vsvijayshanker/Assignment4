
import numpy as np
import scipy.stats

n=144
score=np.array((2,3,4,5,6,7,8,9,10,11,12))
px=np.array((1,2,3,4,5,6,5,4,3,2,1))/36
count1=np.array((4,10,10,13,20,18,18,11,13,14,13))
count2=np.array((3,7,11,15,19,24,21,17,13,9,5))
print(px)
#Test1
for i in range(np.size(score)-1):
    count1[i+1]=count1[i]+count1[i+1]
    count2[i+1]=count2[i]+count2[i+1]
    px[i+1]=px[i]+px[i+1]


V1=0
V2=0
for i in range(np.size(score)):
    V1=V1+((count1[i]-px[i]*n)**2)/(n*px[i])
    V2=V2+((count2[i]-px[i]*n)**2)/(n*px[i])

V1=1-scipy.stats.chi2.cdf(V1,10)
V2=1-scipy.stats.chi2.cdf(V2,10)
print('values are',V1,V2)
if 0<V1<0.01 or 0.99<V1<1.00:
    print('count1 is not sufficiently rnadom')
if 0.01<V1<0.05 or 0.95<V1<0.99:
    print('count1 is suspect')
if 0.05<V1<0.10 or 0.90<V1<0.95:
    print('count1 is almost suspect')
if 0.10<V1<0.90:
    print('count1 is sufficiently random')

if 0<V2<0.01 or 0.99<V2<1.00:
    print('count2 is not sufficiently rnadom')
if 0.01<V2<0.05 or 0.95<V2<0.99:
    print('count2 is suspect')
if 0.05<V2<0.10 or 0.90<V2<0.95:
    print('count2 is almost suspect')
if 0.10<V2<0.90:
    print('count2 is sufficiently random')
