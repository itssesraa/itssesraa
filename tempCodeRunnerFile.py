import pandas as pd

df = pd.read_excel("C:/Users/anwar salman/OneDrive/Desktop/12/E-commerce project - Copy (4) - Copy.xlsx")
print(df.head())

df.info()
df.describe()
clean_data =df.duplicated()
clean_data.sum()