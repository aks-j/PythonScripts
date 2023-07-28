# PythonScripts
1.Function to Get Middle Characters from a String
Code:

def printMiddleCharacter(input_str, num_chars):
    middle_index = len(input_str) // 2
    first_char = middle_index - num_chars // 2
    last_char = first_char + num_chars

    if num_chars >= 1:
        middle_chars = input_str[first_char:last_char]
        print(f'Middle {num_chars} characters are: {middle_chars}')
    else:
        print(f'Invalid number of middle characters: {num_chars}')

input_str = "pythonscripts"
num_chars = 5
printMiddleCharacter(input_str, num_chars)

# Example Usage:
2. Merge List with Given Conditions
def mergeLists(list1, list2):
    divisible_by_5 = [num for num in list1 if num % 5 == 0]
    divisible_by_2 = [num for num in list2 if num % 2 == 0]
    merged_list = divisible_by_5 + divisible_by_2
    return merged_list

def mergeListDescendingOrder(merged_list):
    merged_list.sort(reverse=True)
    return merged_list

list1 = [10, 50, 21, 46, 35]
list2 = [58, 88, 76, 100, 65]

merged_list = mergeLists(list1, list2)
print("Merged_List:", merged_list)

merged_list_desc = mergeListDescendingOrder(merged_list)
print("Merged_List_Desc:", merged_list_desc)

# Example Usage:
3.Python Class to Display Employee Details

Code:
class Person:
    def __init__(self, first_name, middle_name, last_name, gender):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender

    def display_person(self):
        return f'First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\nGender: {self.gender}'


person1 = Person("Jaffer", "Tom", "Scott", "Male")
person2 = Person("Janny", "Doe", "Marek", "Female")

print("Person1 attributes:")
print(person1.display_person())

print("Person2 attributes:")
print(person2.display_person())

# Example Usage:
4.Load Data from CSV File and Display Employee Details

import csv

def display_employee_details():
    with open("Employee_Details.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
display_employee_details()


# Example Usage:

5.Function to Retrieve JSON Key Values

import json

def retrieve_key_values(json_input, key_name):
    values = []
    for item in json_input:
        if key_name in item:
            values.append(item[key_name])
    return values
json_input = [{"ProductID": "1", "ProductName": "Car"},
              {"ProductID": "2", "ProductName": "Bus"}]

key_name_1 = "ProductID"
key_values_1 = retrieve_key_values(json_input, key_name_1)
print(f"{key_name_1} values:", key_values_1)

key_name_2 = "ProductName"
key_values_2 = retrieve_key_values(json_input, key_name_2)
print(f"{key_name_2} values:", key_values_2)

def write_data_to_txt_file(data):
    file_exists = True  # Check if the file exists, change to False if the file does not exist
    mode = "a" if file_exists else "w"
    with open("data.txt", mode) as file:
        file.write(data)
        file.write('\n')
    print("Data saved successfully.")

data_to_write = "Hello, this is sample data."
write_data_to_txt_file(data_to_write)

