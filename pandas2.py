import pandas as pd
df = pd.DataFrame({
    'col1': [1, 4, 3,4,5],
    'col2': [4, 5, 6,7,8],
    'col3': [7, 8, 9,8,1]
})
print(df)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
print(df)
#display.width sets the maximum width of the output line (in characters).
#display.max_columns sets the maximum number of columns that will be displayed in the output.

print(df.iloc[[2]])