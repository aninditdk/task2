#program to calculate count, minimum, maximum price for each cut of diamonds DataFrame

import pandas as pd
df= pd.read_csv("C:\\Users\\user\\Desktop\\spectrum\\diamonds.csv")
g=df.groupby("cut")
g1=g.max()
g1.reset_index(inplace=True)
g2=g.min()
g2.reset_index(inplace=True)
print(g.count())
print(g1[["cut","price"]])
print(g2[["cut","price"]])
