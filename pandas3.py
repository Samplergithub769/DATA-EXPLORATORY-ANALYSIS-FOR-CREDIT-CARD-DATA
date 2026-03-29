import numpy as np
import pandas as pd

exam_data = {'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
'Jonas'],'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]}
df=pd.DataFrame(exam_data)
print(df)

df_reset=df.reset_index()
print(df_reset)

result=df_reset.to_string(index=False)
print(result)

# It converts the index into a normal column and resets the index to default (0, 1, 2, …).
# reset_index() → index ko normal column bana deta hai
# to_string(index=False) → display me index hide kar deta hai
#to_string->it is used only for formatted display of DataFrame.