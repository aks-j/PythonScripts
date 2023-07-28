Create a sample solution to load data from csv file and display the employee details
1)	Create a sample csv file with column names EmployeeID, EmployeeName, DateofJoining, Department, EmailAddress.
2)	Let the file contain at least 25 rows of data (can be random data).
3)	Read the contents of this file and display the data

"""""
# Solution :-

#Import csv package
import csv
#Opens the file named Employee_Details.csv using 'open' funtion
with open(r"Employee_Details.csv") as file:
    # CSV reader object
    reader = csv.reader(file)
    # 'for' loop iterates over each row in 'reader' object
    for row in reader:
        # 'print(row)' used to display each row in the console
        print(row)
"""""

Output:-

['EmployeeID', 'EmployeeName', 'Department', 'Salary (In K)', 'Date of Joining', 'Email Address']
['1', 'Tom ', 'ETA', '10000', '1/1/2022', 'abc@gmail.com']
['2', 'Bob', 'ADM', '20000', '2/1/2022', 'xyz@gmail.com']
['3', 'Jack', 'ECS', '30000', '3/1/2022', 'efg@gmail.com']
['4', 'Harry', 'ETA', '40000', '4/1/2022', 'abc@gmail.com']
['5', 'Tom1 ', 'ADM', '50000', '5/1/2022', 'xyz@gmail.com']
['6', 'Bob2', 'ECS', '60000', '6/1/2022', 'efg@gmail.com']
['7', 'Jack3', 'ETA', '70000', '7/1/2022', 'abc@gmail.com']
['8', 'Harry4', 'ADM', '80000', '8/1/2022', 'xyz@gmail.com']
['9', 'Tom 5', 'ECS', '90000', '9/1/2022', 'efg@gmail.com']
['10', 'Bob6', 'ETA', '100000', '10/1/2022', 'abc@gmail.com']
['11', 'Jack7', 'ADM', '110000', '11/1/2022', 'xyz@gmail.com']
['12', 'Harry8', 'ECS', '120000', '12/1/2022', 'efg@gmail.com']
['13', 'Tom9', 'ETA', '130000', '1/1/2023', 'abc@gmail.com']
['14', 'Bob10', 'ADM', '140000', '2/1/2023', 'xyz@gmail.com']
['15', 'Jack11', 'ECS', '150000', '3/1/2023', 'efg@gmail.com']
['16', 'Harry12', 'ETA', '160000', '4/1/2023', 'abc@gmail.com']
['17', 'Tom13', 'ADM', '170000', '5/1/2023', 'xyz@gmail.com']
['18', 'Bob14', 'ECS', '180000', '6/1/2023', 'efg@gmail.com']
['19', 'Jack15', 'ETA', '190000', '7/1/2023', 'abc@gmail.com']
['20', 'Harry16', 'ADM', '200000', '8/1/2023', 'xyz@gmail.com']
['21', 'Tom17', 'ECS', '210000', '9/1/2023', 'efg@gmail.com']
['22', 'Bob18', 'ETA', '220000', '10/1/2023', 'abc@gmail.com']
['23', 'Jack19', 'ADM', '230000', '11/1/2023', 'xyz@gmail.com']
['24', 'Harry20', 'ECS', '240000', '12/1/2023', 'efg@gmail.com']
['25', 'Tom21', 'ETA', '250000', '1/1/2024', 'abc@gmail.com']


# *************--Thank You!!--:)**************
