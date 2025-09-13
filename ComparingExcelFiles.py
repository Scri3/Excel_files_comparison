import pandas as pd

File1 = 'File1.xlsx'
File2 = 'File2.xlsx'

# Excel files:
files = [File1, File2]

# Empty dictionary
data = {}

# Read data from each file and store in the dictionary
for file in files:

    df = pd.read_excel(file)

    data[file] = df

# Calculate data resemblance rate for each column
for col in data[files[0]].columns:

    resemblance_rate = sum(data[files[0]][col] == data[files[1]][col]) / len(data[files[0]])

    print(f'Resemblance Rate for Column {col}: {100*resemblance_rate:.2f}%\n')

   