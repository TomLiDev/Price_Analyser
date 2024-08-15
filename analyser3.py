import pandas as pd

sampleSize = 200
file = pd.read_csv('testpricedatashort_csv.csv', nrows=sampleSize)

count = 0

def checkBuy(index, newPrice):
    for index, row in file.iloc[index:].iterrows():
        buyTarget = newPrice + 0.03
        print(buyTarget)


for index, row in file.iterrows():
    if row['Price'] < 0.887:
        count =+ 1
        print(count)
        print(row)
        newPrice = row['Price']
        print(newPrice)
        index = index
        checkBuy(index, newPrice)
        break


