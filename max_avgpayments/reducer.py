mapin = open("./max_avgpayments/mapoutputs.txt","r")
mapout = open("r.txt","w")
thisKey = ""
thisValue = 0.0
fullList = []
for line in mapin:
  rowList = []
  data = line.split(' ')
  State = data[0]
  Averagetotalpayements = data[1]
  rowList.append(State)
  rowList.append(Averagetotalpayements)
  fullList.append(rowList)
  # print(fullList)

fullList.sort()
maxValue = 0.0
finalObject = {}
for row in fullList:
  
  if row[0] != thisKey:
    thisKey = row[0]
    thisValue = 0.0
    maxValue = 0.0

  thisKey = row[0]
  row[1] = row[1].replace(",","")
  thisValue = float(row[1])
  if thisValue > maxValue:
    maxValue = thisValue
  finalObject[thisKey] = maxValue
for keyValue in finalObject:
  # print(keyValue + " " + str(finalObject[keyValue])+"\n")
  mapout.write(keyValue + " " + str(finalObject[keyValue]) +"\n")

# close redinput and redouput file
mapin.close()
mapout.close()