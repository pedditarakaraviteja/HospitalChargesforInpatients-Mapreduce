## Hospital Charges For Inpatient

We are functioning on this project for Bigdata course. Our project number is 08. 


 #### List of developers  
 
 
 
 
    
* Taraka Ravi Teja Peddi  
* Sai Manikanta Durga Prasad   
* Yaswanth Yarram  
* Hongyang Wang  
### Links  

https://github.com/pedditarakaraviteja/HospitalChargesforInpatients-Mapreduce  
https://github.com/pedditarakaraviteja/HospitalChargesforInpatients-Mapreduce/issues  
### Introduction
This project is hand-me-down to implement map reduce functionality on our bigdata source Hospital Charges for Inpatients. The reason why we choose Hospital Charges for Inpatients as our data source is because there is a good amount of data and also there are many  rows and columns which gave us multiple options to map reduce.

### Datasource  


Our datasource provides variation of hospital charges in the various hospitals in the US for the top 100 diagnoses.Datasource provides 3 years of data.The datasource is  well structured in excel sheet.    

### Link to datasource  
https://www.kaggle.com/speedoheck/inpatient-hospital-charges/  
### The Challenge
#### What makes it a big data problem?

* Volume: There is 26MB of data in this dataset and 163,066 records.3 years of hospital charges data is available in this source.    
* Variety: This dataset is structured and it is in excel format.  
* Velocity: Data will be generated based on when the hospital charges in different areas.  
* Veracity: Data is very clear. There are no redundant columns and the records was collected from USA Health department dataset https://data.cms.gov/Medicare-Inpatient/Inpatient-Prospective-Payment-System-IPPS-Provider/97k6-zzx3 and it seems to be reliable.  
* Value: Using this data source we can evaluate  years of hospital charges for patients  data including their providerid, state,their amount of discharge, average medicare payments,average total payments all the other information.  
### Big Data Questions
* For each state, calculate the total number of discharges.(Peddi Taraka Raviteja).  
* For each state, calculate the maximum number of Average total payments(Sai Manikanta Durga Prasad,Vinukonda)  

### Big data solutions
One solution per developer.
- #### Taraka Raviteja Peddi
* Mapper input: One line data that mapper will read:
   * 039 - EXTRACRANIAL PROCEDURES W/O CC/MCC	10001	SOUTHEAST ALABAMA MEDICAL CENTER	1108 ROSS CLARK CIRCLE	DOTHAN	AL	36301	AL - Dothan	91	$32,963.07 	$5,777.24 	$4,763.73  
   
*  Mapper Output/reducer input:Example of an intermediate key, value pair output by your mapper:  
    Al 879  
    AK 23  
    AZ 606  
    *  Reduced Output:  
     city = AL(Albama) total number of discharges = 879  
    * Language :  
     Language used for map reducing python  
    * What kind of chart will you use to display your results?  
     I will use pie chat to display results.  
     
     
 - #### Sai Manikanta Durga Prasad Vinukonda  
 * Mapper input: One line data that mapper will read.  
    * 039 - EXTRACRANIAL PROCEDURES W/O CC/MCC	10001	SOUTHEAST ALABAMA MEDICAL CENTER	1108 ROSS CLARK CIRCLE	DOTHAN	AL	36301	AL - Dothan	91	$32,963.07 	$5,777.24 	$4,763.73   
    * Mapper Output/reducer input:Example of an intermediate key, value pair output by your mapper:  
     Az- 166748.44  
     Al- 140505.02  
     Ar-97901.26  
     Ak- 7768   
   *  Reduced Output:  
     city = AZ(Arizona) maximun number of totalpayments = 166748.44    
    * Language :    
     Language used for map reducing is  python    
    *  What kind of chart will you use to display your results?    
     I will use bar chat to display results.    
     
     

  
