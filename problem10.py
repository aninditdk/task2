#program to check the number of rows and columns and drop those row if 'any' values are missing in a row of diamonds DataFrame

import pandas as pd
df= pd.read_csv("C:\\Users\\user\\Desktop\\spectrum\\diamonds.csv")
rows,columns=df.shape
print("rows = ",rows)
print("columns = ",columns)
df=df.dropna(inplace=True)

