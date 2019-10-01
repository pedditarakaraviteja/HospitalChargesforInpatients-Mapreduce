#  open the file mapperoutput.txt and read the file into redinput.
redinput = open("./total_cal/mapperoutput.txt","r")
# open the file redoutput and write the file into redoupt
redouput = open("./total_cal/redouput.txt", "w")

thisKey = ""
thisValue = 0.0
# Reads the each line in redinput and seperated by tab space
for line in redinput:
  data = line.strip().split('\t')
  State, Totaldischarges = data

  if State != thisKey:
    if thisKey:
      # output the last key value pair result
      redouput.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = State 
    thisValue = 0.0
  
  # apply the aggregation function for calculating totaldischarges.
  thisValue += float(Totaldischarges)

# output the final entry into the redouput file
redouput.write(thisKey + '\t' + str(thisValue)+'\n')
# close redinput and redouput file
redinput.close()
redouput.close()