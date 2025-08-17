import pandas as pd

data = {
    "Name": ["Sachin", "Raj", "Simran"],
    "Age": [25, 22, 24]
}
df = pd.DataFrame(data)

# Convert single column
name_list = df["Name"].tolist()
print(name_list)  # ['Sachin', 'Raj', 'Simran']

values_list = df.values.tolist()
print(values_list)
# [['Sachin', 25], ['Raj', 22], ['Simran', 24]]

row_list = df.values.tolist()
for row in row_list:
    print(row)
# ['Sachin', 25]
# ['Raj', 22]
# ['Simran', 24]

for ro