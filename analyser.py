import pandas as pd

file = pd.read_csv('testpricedatashort_csv.csv', nrows=300)
data = pd.DataFrame(file)

sample = (data.head(250))
price = sample['Price']

sectionsTemp =  sample.index.size / 10
sections = int(sectionsTemp)
print("sections", sections)
splitSections = {}
list = []

length = len(sample.index)
print(type(length))
print("length", length)
firstDayTemp = sample['Time (local)'].iloc[1]
firstDay = firstDayTemp[0:10]
print("Test", firstDay)
day = []
nextDay = "text"
dayDict = {}

for x in range(length):
    """ This function will pick every row that matches the firstDay variable and
     add it to a list """
    # thisTime below is the date specificially from each row, with time chopped
    # off, then checked against a specific date.
    thisTime = sample['Time (local)'].loc[x][0:10]
    if thisTime == firstDay:
        thisDayTemp = sample.loc[x]
        thisDay = pd.DataFrame(thisDayTemp)
        day.append(thisDay)
        dayDict[x] = thisDay
    else:
        nextDate = thisTime
        print("TEST", nextDate)
        break
print("End of first day")
#print("FUll days dict", dayDict)
#print("Days List", day)
print("Day from dict", dayDict[12])
print("Day from list", day[12])
    

""" Below is random stuff which is useful for now but will probably be deleted """

"""
for x in range(sections):
This function takes the number of desired sections and creates a dataframe
    for each one, adding each dataframe to a list
    if x != 0:
        end = x*10
        piece = sample.loc[end-10: end]
        splitSections[x] = piece
        pd.DataFrame(piece)
        list.append(piece)


for x in range(sections):
    This function takes the number of desired sections and creates a dataframe
    for each one, adding each dataframe to a list
    if x != 0:
        end = x*10
        piece = sample.loc[end-10: end]
        splitSections[x] = piece
        pd.DataFrame(piece)
        list.append(piece)

else: 
    print("pass")
    pass

#print("working?", splitSections)
#print("SOME", list)
#print("DFAD", splitSections[2])
#print("Another", splitSections[3])

    for x in splitSections:
    frame = splitSections[x]
    frameMax = frame["Price"].max()
    frameMin = frame["Price"].min()
    priceRange = frameMax - frameMin
    price = ["Price"]
    print("This frames max", frameMax)
    print("This frames min", frameMin)
    print("This frames range", priceRange) """