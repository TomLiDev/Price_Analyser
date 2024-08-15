import pandas as pd

sampleSize = 200
file = pd.read_csv('testpricedatashort_csv.csv', nrows=sampleSize)

print("TEST", file.index)
print("TEST2", file['Price'].iloc[0])

# The below 2 lines take the first price from the first row and use this to
# define the startLowPrice and startHighPrice to be fed into the function
# below 
startLowPrice = file['Price'].iloc[0]
startHighPrice = file['Price'].iloc[0]

dayList = []
dayDict = {}
firstDayTemp = file['Time (local)'].iloc[0]
firstDay = firstDayTemp[0:10]

nextDayList = []
nextDayDict = {}

def createNewDay(newDay, newStart):
    for index, row in file.iloc[newStart:].iterrows():
        if row['Time (local)'][0:10] == newDay:
            nextDayDict[index] = row
            nextDayList.append(row)
        else:
            newDay = row['Time (local)'][0:10]
            newStart = index
            createNewDay(newDay, newStart)


#This little for loop creates a dictionary of all rows which equal the first
# day, the index where the next day starts is taken as a variable
for index, row in file.iterrows():
    if row['Time (local)'][0:10] == firstDay:
        dayDict[index] = row
        dayList.append(row)
    else:
        print("Not 1 day", row['Time (local)'][0:10])
        newDay = row['Time (local)'][0:10]
        print("test inside", type(newDay))
        newStart = index
        print("HGHGHGHGHG", newStart)
        createNewDay(newDay, newStart)
        break

# The below are dataframes made from the list and dictionary created above
# The 2 variable are the high and low prices from the list-derived df
oneDay = pd.DataFrame.from_dict(dayDict)
oneDayList = pd.DataFrame(dayList)
currentLow = oneDayList['Price'].min()
currentHigh = oneDayList['Price'].max()

subset = file.loc[file['Time (local)'].str.contains(newDay)]
print("Yep", subset)
print("yep2", subset['Price'].min())

print("down here", nextDayDict)