import pandas as pd
# should have replaced the " as well to avoid confliction
data = pd.read_csv('data.txt', sep=',')
data = data.replace(to_replace='"',
                    value=" ")
data.to_excel('final_data.xlsx', index=False)
