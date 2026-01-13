import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a=np.ones(100)
print(a,"\n","---------------------------")
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

b=a.reshape(10,10)
print(b)

