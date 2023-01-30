#reads EmployeePay.csv file & prints out details of each employee
import csv 

#open csv file in read mode 
employees = open('EmployeePay.csv', 'r')

#create csv object 
employee_file=csv.reader(employees, delimiter=',')

#skip first line in csv file 
next(employees)

#use for loop to step through file 
for record in employee_file:
    print('ID:', record[0],'Name:',record[1],record[2],'Salary:',record[3],'Bonus:',record[4])
    