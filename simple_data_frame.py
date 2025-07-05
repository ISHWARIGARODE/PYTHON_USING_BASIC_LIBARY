import pandas as pd
#create a simple dataframe

data = { 
    'Name': ['Alice', 'Bob', 'Charlie', 'Shrusti', 'Harsha'],
    'Age': [25,30,35,20,40],
    'City': ['New York', 'Paris', 'London', 'Turkey', 'Bangalore'],
    'College': ['COEP', 'JDIET', 'VJT', 'DYPATIL', 'YCC']
}
df = pd.DataFrame(data)

#display the dataframe
print(df)

#access a column
print(df['Name'])

#basic statistics
print(df['Age'].mean()) #average age

#filter row
print(df[df['Age']>28])


print(df['College'])