# 1)	Create a function to take JSON input along with another input parameter which will be a key name
# For example :
# JSON Input : [{“ProductID”:”1”, “ProductName”:”Car”}, {“ProductID”:”2”, “ProductName”:”Bus”}]
# functionA(JSON input, keyName)

# 2)	Based on the key name passed, the function should retrieve the values for that particular key
# In the above sample, if the function is called as below

# functionA(JSON Input, ProductName)  The function should give the Output as Car, Bus
# functionA(JSON Input, ProductID)  The function should give the Output as 1, 2
# Create Python function for write data into the text file
# Check if the file exists then open the file in append mode and add data otherwise create new file in write mode
"""""

# Solution:-

#import package
import json
# This function return key value from json
def Return_Key_value(json_input,key_name):
    values=[]
    for item in json_input:
        if key_name in item:
            values.append(item[key_name])
    return values

# This function write data to text file
def write_data_to_txtFile(data):
    data=var_03
    file_exists=True
# if the file is present then data is in append mode else it's create a new file and data added.
    mode ="a" if file_exists else "w"
    with open("JSON_data.txt", mode) as file:
        file.write(data)
        file.write('\n')
    print("Data saved successfully.")

json_input =[{"ProductID":"1", "ProductName":"Car"},
             {"ProductID":"2", "ProductName":"Bus"}]
var=input("Enter KeyName:-")
if var in json_input[0]:
    var_01 = Return_Key_value(json_input,var)
    var_03=(var)+" "+(str(var_01))
    print(var_03)
    #function calling
    write_data_to_txtFile(var_03)
else:
    print("Key Name Not Found")

"""""

# Output:
First_case:-Enter KeyName:-ProductID
            ProductID ['1', '2']
            Data saved successfully.

Second_case:-Enter KeyName:-Van
             Key Name Not Found

# *************--Thank You!!--:)**************

"""""
******************
