import numpy as np
import pandas as pd

exam_data = {'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin',
'Jonas'],'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data,labels)
print(df)

result=df.columns.tolist()
print(result)

df = pd.DataFrame({
    'col1': [1, 4, 3,4,5],
    'col2': [4, 5, 6,7,8],
    'col3': [7, 8, 9,8,1]
})
print(df)




df=pd.DataFrame({'city':['California','Georgia','Los Angeles','Georgia','California','California','California','Los Angeles','Los Angeles','Los Angeles'],'name':['A','B','C','D','E','F','G','H','I','J']})
result=df.groupby(['city'])['name'].count().reset_index(name='Number of people')
print(result)
