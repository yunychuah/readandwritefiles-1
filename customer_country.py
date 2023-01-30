#reads customers.csv file and produces new file containing customer name and country 
import csv 

#open csv file in read mode
infile = open('customers.csv', 'r')

#create csv object
csvfile = csv.reader(infile)

#skip first line in csv file
next(infile)

#use for loop to step through file
counter = 0 

outfile = open('customer_country.csv', 'w')

for record in csvfile:
    outfile.write(record[1] + ' ' + record[2] + ',' + record[4] + '\n')

    counter += 1

outfile.write(str(counter))

outfile.close()
