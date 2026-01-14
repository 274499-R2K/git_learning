import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=np.ones(100)
# print(a,"\n","---------------------------")
# print(f"{a.ndim=}")
# print(f"{a.shape=}")
# print(f"{a.dtype=}")

a2=np.ones((5,5))
# print(a2)

# r=np.arange(10,100,2)
# print(r)
rnd=np.random.normal(0,1,1000)
plt.scatter(np.arange(0,1000), rnd)
# plt.show()

# RESHAPING
# b=a.reshape(10,10)
# print(b)
# c=b.ravel()
# print(c)


# PD DataFrame to NP TENSOR
D = pd.DataFrame(
    {'Name': ['Stefano',
              'Marco',
              'Franco'],
     'Surname': ['Mariani',
                 'Mamei',
                 'Zambonelli']
     })
# print(D,"\n", '---------------------------------------')
# h=np.array(D.columns) #need to store column indexes (keys) in np array
# hl=list(D.columns) # or store in a python list
#
# print(h,"\n", '--------------------------------------')
#
# T=pd.DataFrame.to_numpy(D)
# print(T ,"\n")

#OPERATION SPREADING

a=np.arange(0,20)
b=np.arange(0,20)
A=a.reshape(4,5)
B=b.reshape(4,5)
# print(A,"\n")
# print(B,"\n")

C=A+B
print(C,"\n")

D=A*B
print(D,"\n")

E=A@B.T
print(E,"\n")

dE=np.linalg.det(E)
print(dE,"\n")

# Einv=np.linalg.inv(E)
# print(Einv,"\n")
