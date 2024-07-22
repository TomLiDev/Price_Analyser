import pandas as pd

file = pd.read_csv('testpricedatashort_csv.csv', nrows=300)
data = pd.DataFrame(file)

sample = (data.head(30))
price = sample['Price']

#print(sample.Price.rolling(10).min())

print("thing", sample.index.size)
sectionsTemp =  sample.index.size / 10
sections = int(sectionsTemp)
print("sections", sections)

#test = sample.iloc[1::10, :]
#print("test", test)

#print("Sample2", sample2)
#print("Test", sample.loc[4:5])

splitSections = []

#newDf = pd.DataFrame(data, 30)
#print("TEST", newDf)

for x in range(sections):
    if x != 0:
        end = x*10
        print("this is x", x*10)
        piece = sample.loc[end-10: end]
        pd.DataFrame(piece)
        splitSections.append(piece)
        print("Inside loop", piece)
else: 
    print("pass")
    pass

print("working?", splitSections)
    



#for index, row in sample2.iterrows():
    #print("inside function", row['Price'], row['Time (local)'])

#chopper()