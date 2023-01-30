#reads sales.csv file and creates new file w customer ID and calculated total(as shown in salesreport.csv)
import csv

#open sales csv file in read mode 
sales_file=open('sales.csv', 'r')

csvfile = csv.reader(sales_file)

next(sales_file)
 
outfile = open('salesreport.csv', 'w')

customer_ID = 250
customer_total = 0 
line_total = 0

outfile.write('Customer' + ',' 'Total' + '\n')

for record in csvfile:
    if record[0] == str(customer_ID):
        line_total = float(record[3])+ float(record[4]) + float(record[5])
        customer_total += line_total
         
    else:
        outfile.write(str(customer_ID) + ',' + str(customer_total) +'\n') 
        customer_ID = record[0] 
        line_total = 0
        customer_total = 0
        line_total = float(record[3])+ float(record[4]) + float(record[5])
        customer_total += line_total

outfile.write('261' + ',' + str(customer_total))           
outfile.close() 