import numpy as np
import pandas as pd
df=pd.DataFrame(np.random.randn(10,2))
print("Original dataframe:")
print(df)
part_70=df.sample(frac=0.7,random_state=10)
print("\n70%of the dataframe")
print(part_70)
part_30=df.drop(part_70.index)
print("\n30%of the dataframe")
print(part_30)


#Picks 70% of rows randomly.
#random_state=10 ensures you get the same 70% every time you run the code.

s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])
df=pd.concat([s1,s2],axis=1) # column-wise
print(df)