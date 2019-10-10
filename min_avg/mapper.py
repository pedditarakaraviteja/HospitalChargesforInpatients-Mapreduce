# mapinput open the inpatientcharges and the text 
mapinputs = open("./data/inpatientCharges.txt","r")
# write results in output.txt
mapoutput = open("mapoutputs.txt", "w")
for line in mapinputs:
  # separate each column using space
  data = line.strip().split('	')
  # if the number of columns in dataset is 12 then separate city and average covered charges columns in datasource and write them in mapoutput.txt
  if (len(data) == 12):
   Definition, Id, Name, StreetAddress, City, State, Zipcode, Refferalregion, Totaldischarges, Averagecoveredcharges,  Averagetotalpayements, Averagemedicarepayments   = data
   mapoutput.write(City + "\t" + Averagecoveredcharges + "\n")