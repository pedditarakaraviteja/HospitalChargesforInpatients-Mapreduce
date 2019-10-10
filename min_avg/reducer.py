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