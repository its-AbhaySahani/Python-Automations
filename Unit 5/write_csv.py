# writre sample data in csv file
import pandas as pd
data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
        'Age': [20, 21, 22, 23],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
df.to_csv('Unit 5\Sample_CSV.csv', index=False)
print('Data is written in csv file')
