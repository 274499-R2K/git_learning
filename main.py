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
#print(c.dropna())
d=a.add(b,fill_value=0)

# print(d.sum())
# print(d.prod())
# print(d.max())
# print(d.argmax())
# print(d.var())
# print(d.mean())
# print(d.median())
# print(d.std())

#print(d.describe()) # summarizing stats table
D = pd.DataFrame(
    {'Name': ['Stefano',
              'Marco',
              'Franco'],
     'Surname': ['Mariani',
                 'Mamei',
                 'Zambonelli']
     })

#print(D)
# col = list(D.columns)
# print(col)
# ind = list(D.index)
# print(ind)
# print(D.index)
# print(D.head(1)) #??
# # print(D.tail(1))
# print(D.info())
# print(D.describe())
# print(D.shape)


C = pd.DataFrame({'A':a,'B':b})
E = C.fillna(0)
# print(E, "\n")
# print(E.loc[['C']],"\n")
# print(E[1:3], "\n")

planets_1 = pd.DataFrame({
    "Planet": ["Earth", "Mars", "Jupiter"],
    "Gravity": [9.8, 3.7, 23.1],
    "Mass": [100,80,400]
})
planets_2 = pd.DataFrame({
    "Planet": ["Mars", "Jupiter", "Neptune"],
    "MeanTemperature": [-65, -110, -200],
    "Mass": [80,400,200]
})
merged = pd.merge(planets_1, planets_2, on='Planet')
print(merged)












