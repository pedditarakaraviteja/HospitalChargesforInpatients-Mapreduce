mapin = open("./min_avg/mapoutputs.txt","r")
mapout = open("r.txt","w")
thisKey = ""
# thisValue = 0.0
fullList = []
for line in mapin:
  rowList = []
  data = line.split('\t')
  City = data[0]
  Averagecoveredcharges = data[1]
  rowList.append(City)
  rowList.append(Averagecoveredcharges)
  fullList.append(rowList)
#fullList.sort()
minValue = 0.0
finalObject = {}
list1 = []
for row in fullList:
  
  if row[0] != thisKey:
    thisKey = row[0]
    thisValue = 0.0
    minValue = 0.0

  thisKey = row[0]
  row[1] = row[1].replace(",","")
  thisValue = float(row[1])
  if thisValue > minValue:
    minValue = thisValue
  finalObject[thisKey] =minValue
for keyValue in finalObject:
  # print(keyValue + " " + str(finalObject[keyValue])+"\n")
  mapout.write(keyValue + " " + str(finalObject[keyValue]) +"\n")

# close redinput and redouput file
mapin.close()
mapout.close()