import numpy as np
#b=np.array([[1.0,3.0],[7.1,8.9]])
#a=np.array([1,2,3],dtype='int16')
#print(a.ndim)
#print(a.shape)
#print(a.dtype)
#print(a.itemsize)
#print(b.itemsize)
#print(a.size)
#print(b.size)
#print(b.dtype)
#print(b.ndim)      2
#print(b.shape)   (2,2) 
#print(b[0,1])  3.0
#print(b[1,0])  7.1
#print(a[0,2]) error
#print(b[:,0])   1st column
#print(b[0,:])   1st row
#print(0,   startindex:last index:step)  like slicing first row
#b[0,1]=5  mutable
#k=np.zeros((2,2))
#print(k)
#ap=np.full((3,2),99,dtype='int16')
#print(ap)
#an=np.random.rand(9,8)
#print(an)
#full_like  wherer you pass a.shape,number
#random.random_sample   passs a.shape
#random.randint(4,7,size=(5,4))
#np.identity(5)
#ar=np.array([[1,2]])
#t=np.repeat(ar,3,axis=0)
#print(t)
##z=np.zeros((3,3))
#z[1,1]=9
#a[1:4,1:4]=z.copy
#print(a)
#be carful when copying arrays (b=a) both a and b will change simultaneously 
#b=a.copy()  to prevent it
#linear algebra
# for matrix multiplication number of columns = number of rows
#a=np.ones((2,3))
#b=np.full((3,2),2) 
#at=np.matmul(a,b)
#print(at)
#c=np.identity(3)
#k=np.full((3,3),4)
#kc=np.matmul(k,c)
#print(np.linalg.det(c))
# k1=k2.reshape((2,3))   just total number of elements should be same
#a=np.vstack((v1,v2,v3,v1))   vertical stack or horizontal stack hstack
#filedata=np.genfromtxt('data.txt',delimiter=',')
#filedata=filedata.astype('int32')
fil=np.array([[1,2,3,4,5,6,7,8,9,10],[1,4,5,6,7,8,9,0,1,2]])
#print(filedata[fil>5])   gives the elements where value greater than 50
#print(fil[[1,2,3]])   give the value at the given index
#print(np.any(fil>5))    np.any or np.all   axis=0 checks all elements columns
#print(fil[[0,1],[0,1]])     prints element at 0,0 and 1,1
# print(fil[0:2,[0,1]])         prints all permutations 00 01 10 11
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show() 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000), kind="kde")

plt.show()