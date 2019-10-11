# input open the inpatientcharges and the text 
input = open("./data/inpatientCharges.txt","r")
# write results in output.txt
output = open("./avage_medicare/map.txt", "w")
# open everyline in inpatientCharges.txt
for line in input:
  # separate each column using space
  data = line.strip().split('	')
  # if number of columns in dataset is 12 then separate state and total discharges columns in datasource and write them in output.txt
  if (len(data) == 12):
   Definition, Id, Name, StreetAddress, City, State, Zipcode, Refferalregion, Totaldischarges, Averagecoveredcharges,  Averagetotalpayements, Averagemedicarepayments   = data
   output.write(City + "\t" + Averagemedicarepayments + "\n")
# close input and output.txt
input.close()
output.close()