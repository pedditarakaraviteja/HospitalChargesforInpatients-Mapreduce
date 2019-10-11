#  open the file mapperoutput.txt and read the file into rinput.
rinput = open("./avage_medicare/map.txt","r")
# open the file routput and write the file into redoupt
routput = open("./avage_medicare/ouput.txt", "w")
thisKey = ""
thisValue = 0.0
# Reads the each line in rinput and seperated by tab space
for line in rinput:
  data = line.strip().split('\t')
  City, Averagemedicarepayments = data
  #remove the $ and , from Averagemedicarepayments to make sure the str can be change to float
  Averagemedicarepayments = Averagemedicarepayments.replace("$","")
  Averagemedicarepayments = Averagemedicarepayments.replace(",","")
if City != thisKey: 
    if thisKey:
      # output the last key value pair result
      routput.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = City
    thisValue = 0.0
  
  # apply the aggregation function for calculating totalmedicarepayments.

    thisValue += float(Averagemedicarepayments)
# output the final entry into the routput file
routput.write(thisKey + '\t' + str(thisValue)+'\n')
# close rinput and routput file
rinput.close()
routput.close()