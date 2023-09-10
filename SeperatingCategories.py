import pandas as pd

data = pd.read_csv('SeperatingCategories.csv')
print(data.head())
categories = data.season.unique()
#print(categories)

for I in categories:
    df2 = data.loc[data['season'] == I]
    #print(df2)
    filename = "output//" + I + ".csv"
    #print(filename)
    df2.to_csv(filename, index=False)
