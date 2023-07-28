
Create Python class with 2 instances of the same class and display attribute values of both instances
1)	Write a Python Class named Person with the attributes FirstName, MiddleName, LastName, Gender
2)	Create 2 instances of the Person class and assign values to its attributes
3)	Display attributes names along with values from both the instances
4) Display the one person having one or more address

"""""

# Solution:-

#Person class
class Person:
    def _init_(self,first_name,middle_name,last_name,gender,addresses):      #function declare
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender
        self.addresses=addresses
    def display_person(self):                                        #f for formatted string literals
        address_info=""
        for address in self.addresses:
            address_info += f'\nAddress:{address.display_address()}'
        return f'First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\nGender: {self.gender}{address_info}'


#Address class
class Address:
    def _init_(self,street,city,state,pin_code):                          #function declare
        self.street = street
        self.city = city
        self.state = state
        self.pin_code = pin_code
    def display_address(self):
        return f'{self.street},{self.city},{self.state},{self.pin_code}'     #f for formatted string literals
#objects of Address class
Address_01= Address('HighStreet','Pune','Maharashtra','-411035.')
Address_02= Address('Main Chowk','Shivajinagar','Maharashtra','-411036.')
Address_03=Address('Main Road','Pune','Maharashtra','-423102')
Address_04=Address('Main Chowk','Beed','Maharashtra','-423102')
# person objects with multiple addresses
Adrress_list=[Address_01,Address_02,Address_03]
#objects of Person class
person1 = Person ("Jaffer", "Tom", "Scott", "Male",Adrress_list)
person2 = Person ("Janny", "Doe", "Marek", "Female",Adrress_list)
person3 = Person ("John", "Sir", "Mar", "male",[Address_04])
person4=Person("Jaffer","Jack","Dat","Male",[Address_02,Address_01])
print("Person1 attributes with multiple address:-")
#funtion calling
print(person1.display_person())
print("**************")
print("Person2 attributes with multiple address:-")
print(person2.display_person())
print("**************")
print("Person3 Attributes with one address:-")
print(person3.display_person())
print("**************")
print("Person4 Attributes with two address:-")
print(person4.display_person())
print("**************")
"""""

# Output:-

Person1 attributes with multiple address:-
First Name: Jaffer
Middle Name: Tom
Last Name: Scott
Gender: Male
Address:HighStreet,Pune,Maharashtra,-411035.
Address:Main Chowk,Shivajinagar,Maharashtra,-411036.
Address:Main Road,Pune,Maharashtra,-423102
**************
Person2 attributes with multiple address:-
First Name: Janny
Middle Name: Doe
Last Name: Marek
Gender: Female
Address:HighStreet,Pune,Maharashtra,-411035.
Address:Main Chowk,Shivajinagar,Maharashtra,-411036.
Address:Main Road,Pune,Maharashtra,-423102
**************
Person3 Attributes with one address:-
First Name: John
Middle Name: Sir
Last Name: Mar
Gender: male
Address:Main Chowk,Beed,Maharashtra,-423102
**************
Person4 Attributes with two address:-
First Name: Jaffer
Middle Name: Jack
Last Name: Dat
Gender: Male
Address:Main Chowk,Shivajinagar,Maharashtra,-411036.
Address:HighStreet,Pune,Maharashtra,-411035.
**************


# *************--Thank You!!--:)**************
