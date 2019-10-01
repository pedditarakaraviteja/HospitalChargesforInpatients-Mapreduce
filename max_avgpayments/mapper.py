# mapinput open the inpatientcharges and given the read access 
mapinputs = open("./data/inpatientCharges.txt","r")
# write results in output.txt.given the write access 
mapoutput = open("./max_avgpayments/mapoutputs.txt", "w")
# open everyline in inpatientCharges.txt
for line in mapinputs:
  # separate each column usi
  data = line.strip().split('	')
  # if number of columns in dataset is 12 then separate state and total discharges columns in datasource and write them in mapoutput.txt
  if (len(data) == 12):
    Definition, Id, Name, StreetAddress, City, State, Zipcode, Refferalregion, Totaldischarges, Averagecoveredcharges,  Averagetotalpayements, Averagemedicarepayments   = data
    mapoutput.write(State + "\t" + Averagetotalpayements + "\n")
# close the mapinputs file
mapinputs.close()
# close the mapoutput file 
mapoutput.close()


