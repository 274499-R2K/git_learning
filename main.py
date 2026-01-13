import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# S = pd.Series(['a','b','c','d','e','f','g','h'])
# #print(S)
# V = {'0':1, '1':2, '2':3, '3':4, '4':5, '5':6}
# Vs = pd.Series(V)
# #print(Vs)
# Vx = Vs > 4
# print(Vx)
# print(Vs[Vx])
# print(Vs[Vs>5])
a=pd.Series({'A':2 , 'B':3 , 'C':4})
b=pd.Series({'B':5 , 'D':7 , 'E':2})
c=a+b
#print(c)
print(c.dropna())
print(a.add(b,fill_value=0))














