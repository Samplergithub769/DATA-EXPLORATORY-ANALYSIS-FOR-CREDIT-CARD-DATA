import numpy as np
import pandas as pd

exam_data = {'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
'Jonas'],'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]}
df=pd.DataFrame(exam_data)
print(df)

df=df.sample(frac=1)
print(df)

# df.sample(frac=1) → returns all rows (frac=1) in random order.