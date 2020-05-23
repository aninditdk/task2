#program to count the duplicate rows of diamonds DataFrame
import pandas as pd
df= pd.read_csv("C:\\Users\\user\\Desktop\\spectrum\\diamonds.csv")
df1=df.duplicated().sum()
print(df1)
