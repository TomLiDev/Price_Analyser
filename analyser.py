import pandas as pd

file = pd.read_csv('testpricedatashort_csv.csv', nrows=300)
data = pd.DataFrame(file)

sample = (data.head(50))
price = sample['Price']

sectionsTemp =  sample.index.size / 10
sections = int(sectionsTemp)
print("sections", sections)

splitSections = {}
list = []

for x in range(sections):
    """ This function takes the number of desired sections and creates a dataframe
    for each one, adding each dataframe to a list """
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
print("DFAD", splitSections[2])
print("Another", splitSections[3])

#for x in splitSections:
    #print("new", splitSections[x])