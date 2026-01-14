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


# C = pd.DataFrame({'s1':a,'s2':b})
# E = C.fillna(0)
# print(E, "\n")
# print(E.loc[['B']],"\n")
# print(E[1:3], "\n")




#
planets_1 = pd.DataFrame({
    "Planet": ["Earth", "Mars", "Jupiter", "Saturn"],
    "Gravity": [9.8, 3.7, 23.1, 24.2],
    "Mass": [100,80,400,300]
})

planets_2 = pd.DataFrame({
    "Planet": ["Mars", "Jupiter", "Neptune", "Venus"],
    "MeanTemperature": [-65, -110, -200, 120],
    "Mass": [80,400,200,150]
})

planets_3 = pd.DataFrame({
    "Planet": ["Mercury", "Cerere", "Pluton", "Moon"],
    "MeanTemperature": [250, -110, -500, -10],
    "Mass": [130,100,50,20]
})

planets_4 = pd.DataFrame({
    "Planet": ["Io", "Uran"],
    "MeanTemperature": [-65, -110],
    "Gravity": [9.8, 3.7],
})
# merged = pd.merge(planets_1, planets_2, on='Planet')
# print(merged)
merged=planets_1
p_list=[planets_2,planets_3,planets_4]
# print(p_list)
for p in p_list:
    merged = pd.merge(merged,p, on='Planet', suffixes=('_p1', '_p2'), how="outer")
    merged['Mass_p1'] = merged['Mass_p1'].combine_first(merged['Mass_p2'])
    merged['Gravity_p1'] = merged['Gravity_p1'].combine_first(merged['Gravity_p2'])
    merged['MeanTemperature_p1'] = merged['MeanTemperature_p1'].combine_first(merged['MeanTemperature_p2'])
    merged = merged.drop(columns=['Mass_p1','Mass_p2','Gravity_p1', 'Gravity_p2',
                                  'MeanTemperature_p1', 'MeanTemperature_p2'])
merged = merged.rename(columns={'Mass_p1': 'Mass', 'Gravity_p1': 'Gravity', 'MeanTemperature_p1': 'MeanTemperature'})
print(merged, "\n")
#
# # Puoi fare N merge in un ciclo (ad esempio con una lista di DataFrame)
# # e unire due DataFrame alla volta.
# # L’importante è che dopo ogni merge tu normalizzi subito la colonna Mass,
# # altrimenti dopo N merge potresti ritrovarti con molte colonne Mass_p1, Mass_p2,





# # print (merged['Mass'])
# # print (merged.loc[2])
# M=merged
# #print(M, "\n")
# M['Type'] = ['Rocky', 'Gas', 'Rocky', 'Gas', 'Gas', 'Rocky']
# print(M, "\n")
#
# t_group=M.groupby('Type')
# for t in t_group:
#     print("index = ",t[0], "\n")
#     print("data: ","\n", t[1], "\n")
#
# # g_mean=t_group.aggregate('mean')
# # g_std=t_group.aggregate('std')
# #not working beacuse mix of string and number
#
# print("\n","\n","------------------------")
# g_mean = t_group.mean(numeric_only=True)
# g_std = t_group.std(numeric_only=True)
# print("MEAN VALUES:","\n", g_mean, "\n","\n", "STD VALUES:","\n",g_std, "\n")
#
#
#
#







