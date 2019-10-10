# mapin is a variable which reads input file mapoutputs.txt.
mapin = open("./min_avg/mapoutputs.txt","r")
# mapout is a vriable which writes output to r.txt file.
mapout = open("./min_avg/r.txt","w")
thisKey = ""
# thisValue = 0.0
fullList = []
for line in mapin:
  rowList = []
  data = line.split('\t')
  City = data[0]
  Averagecoveredcharges = data[1]
  # rowList is an array which is appended with city names.
  rowList.append(City)
  # rowList is then appended Averagecoveredcharges.
  rowList.append(Averagecoveredcharges)
  # now we append the rowList to fullList.
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
  #This is a logic to find out the city with minimum Averagecoveredcharges.