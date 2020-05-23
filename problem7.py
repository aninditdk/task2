# Reading a csv file and printing the first 5 rows

import pandas as pd
df= pd.read_csv("C:\\Users\\user\\Desktop\\spectrum\\diamonds.csv")
print(df.head(5))
