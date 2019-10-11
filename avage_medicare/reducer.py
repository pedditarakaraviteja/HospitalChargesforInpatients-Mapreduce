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