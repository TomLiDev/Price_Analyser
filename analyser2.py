import pandas as pd

sampleSize = 100
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

print("TEST3", startLowPrice, startHighPrice)
print("TEST4", file['Price'].max())
print(file)

firstDayTemp = file['Time (local)'].iloc[0]
firstDay = firstDayTemp[0:10]
print("TEST5", firstDay)

#This little for loop creates a dictionary 
for index, row in file.iterrows():
    if row['Time (local)'][0:10] == firstDay:
        dayDict[index] = row
        dayList.append(row)

#print("outside", dayDict)

oneDay = pd.DataFrame.from_dict(dayDict)
oneDayList = pd.DataFrame(dayList)
#print("yep", oneDay)
print("YET", oneDayList)
print("max in df", oneDayList['Price'].max())


""" def lowPoint():
    for ind in file.index:
        if file['Price'][ind] < startLowPrice:
            newLow = file['Price'][ind]
            print("test in function", newLow)

lowPoint() """