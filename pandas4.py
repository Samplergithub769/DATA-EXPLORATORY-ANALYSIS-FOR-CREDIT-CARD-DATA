import numpy as np
import pandas as pd

exam_data = {'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
'Jonas'],'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]}
df=pd.DataFrame(exam_data)
print(df)


df.loc[8,'score']=10.2
print(df)




total_nans=df[['score','name']].isna().sum()
print(total_nans)

# .sum() → counts the number of True values per column.

total_nans=df[['score','name']].isna().sum().sum() # it returns a single value
print(total_nans)

