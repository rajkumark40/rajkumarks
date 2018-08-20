import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
from numpy.random import seed
from numpy.random import randint
from numpy.random import rand
from numpy.random import uniform
import random as r
from sklearn.cluster import KMeans
count_0,count_1,count_2=0,0,0

from numpy.random import seed
from numpy.random import randint
for i in range(9):
    seed(i)
    x=randint(0,21,100)
    y=uniform(low=0.0,high=3.0,size=(100,))
    q=[]
    for i in range(100):
        c=[x[i],y[i]]
        q=np.append(q,c)
    a=q.reshape(100,2)
    
    kmeans=KMeans(n_clusters=3)
    kmeans.fit(a)
    print('centers',kmeans.cluster_centers_)
    print('labels:',kmeans.labels_)
    for i in range(len(kmeans.labels_)):
        if(kmeans.labels_[i]==0):
            count_0+=1

        if (kmeans.labels_[i]==1):
            count_1+=1

        if(kmeans.labels_[i]==2):
            count_2+=1
    print('per map_0',count_0)
    print('per map_1',count_1)
    print('per map_2',count_2)
    plt.scatter(a[:,0],a[:,1],c=kmeans.labels_)
    plt.xlabel('AGE')
    plt.ylabel('DRUGS')
    plt.show()
count_00=(int)(count_0/9)
count_01=(int)(count_1/9)
count_02=(int)(count_2/9)
print('using random it is found that:\n people using heroin is',count_00,'\npeople using prescribed drugs is ',count_01,'\npeople using cocain is',count_02)
if(count_00>count_01 & count_00>count_02):
    print('people using heroin is greatest')
elif((count_01>count_02)==1):
    print('people using prescribed drug is greatest')
else:
    print('people using cocain is greatest')