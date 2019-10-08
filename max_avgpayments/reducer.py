# This file has given a read access
mapin = open("./max_avgpayments/mapoutputs.txt","r")
# This file has given an write access 
mapout = open("./max_avgpayments/r.txt","w")
thisKey = ""
thisValue = 0.0
fullList = []

# Hence in every part of the mapin take the row list as a array and append the value of the state and average total payments and row list 
for line in mapin:
  rowList = []
  data = line.split(' ')
  #Storing the data in first array.
  State = data[0]
  Averagetotalpayements = data[1]
  rowList.append(State)
  rowList.append(Averagetotalpayements)
  fullList.append(rowList)
  # print(fullList)
# This sort the entire list
#fullList.sort()
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
  # This is the aggregrate function to calculate the maximum 
  if thisValue > maxValue:
    maxValue = thisValue
  finalObject[thisKey] = maxValue
for keyValue in finalObject:
  # print(keyValue + " " + str(finalObject[keyValue])+"\n")
  mapout.write(keyValue + " " + str(finalObject[keyValue]) +"\n")

# close redinput file 
mapin.close()
# close the out file 
mapout.close()

