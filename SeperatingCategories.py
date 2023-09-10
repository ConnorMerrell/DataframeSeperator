import pandas as pd

categoryName = "season"

data = pd.read_csv('SeperatingCategories.csv')
print(data.head())
categories = data[categoryName].unique()
#print(categories)

for I in categories:
    df2 = data.loc[data[categoryName] == I]
    #print(df2)
    filename = "output//" + I + ".csv"
    #print(filename)
    df2.to_csv(filename, index=False)
