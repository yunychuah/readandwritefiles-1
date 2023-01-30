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

for record in csvfile:
    if record[0] == str(customer_ID):
        line_total = float(record[3])+ float(record[4]) + float(record[5])
        customer_total += line_total
    else:
        customer_ID += 1
        line_total = 0
        line_total = float(record[3])+ float(record[4]) + float(record[5])
        customer_total += line_total
        
    outfile.write(str(customer_total)+'\n')    
outfile.close()

#current customer id equal to previous cust id
#set customer id 