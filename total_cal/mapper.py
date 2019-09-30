# mapinput open the inpatientcharges and the read text 
mapinput = open("inpatientCharges.txt","r")
# write results in output.txt
mapoutput = open("mapperoutput.txt", "w")
# open everyline in inpatientCharges.txt
for line in mapinput:
  # separate each column using space
  data = line.strip().split('	')
  # if number of columns in dataset is 12 then separate state and total discharges columns in datasource and write them in mapoutput.txt
  if (len(data) == 12):
   Definition, Id, Name, StreetAddress, City, State, Zipcode, Refferalregion, Totaldischarges, Averagecoveredcharges,  Averagetotalpayements, Averagemedicarepayments   = data
   mapoutput.write(State + "\t" + Totaldischarges + "\n")
# close mapinput and mapoutput.txt
mapinput.close()
mapoutput.close()
