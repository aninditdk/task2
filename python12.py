#program to get sample 75% of the diamonds DataFrame's rows without replacement and store the remaining 25% of the rows in another DataFrame

import pandas as pd
df= pd.read_csv("C:\\Users\\user\\Desktop\\spectrum\\diamonds.csv")
g=df.head(int(len(df)*(0.75)))
f=df.tail(int(len(df)*(0.25)))
print(g)
print(f)
