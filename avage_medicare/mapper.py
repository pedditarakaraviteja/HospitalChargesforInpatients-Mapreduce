# input open the inpatientcharges and the text 
input = open("./data/inpatientCharges.txt","r")
# write results in output.txt
output = open("./avage_medicare/map.txt", "w")
# open everyline in inpatientCharges.txt
for line in input:
  # separate each column using space
  data = line.strip().split('	')