Create a merge list with the given condition

 Part 1 : Given 2 lists as below. From List 1, pick only those values that are divisible of 5.
 and from List 2, pick the values that are divisible of 2. 
 Merge these values to form a single output as mentioned
                                 List 1 : [10, 50, 21, 46, 35]
                                 List 2 : [58, 88, 76, 100, 65]
 Expected Output : Merged_List : [10, 50, 35, 58, 88, 76, 100]

 Part 2 : Once the merge list is created, arrange the values in descending order
 
 Expected Output : Merged_List_Desc : [100, 88, 76, 58, 50, 35, 10]

"""""

#Declare function
def pick_up_numbers():
    try:
        num_1 = [float(num) for num in (input("Enter the comma separated list:-")).split(",")]
        divisor = float(input("Enter divisor:-"))
        if divisor>=1:
            divisible_1 = [num for num in num_1 if num % divisor == 0]
            return (divisible_1)
        else:
            print("Enter valid divisor")
    except ValueError:
        print("Invalid input, enter the valid numbers.")
        return
    except ZeroDivisionError:
        print("Invalid divisor, enter the valid divisor.")
        return


result_1 = pick_up_numbers()
print("**********")
result_2= pick_up_numbers()

#Merge Two List
merge_list=(result_1+result_2)
merge_list=[int(num) for num in merge_list]
print("Merged_List :- ",merge_list)

#Descending order of merge list
merge_list.sort(reverse=True)
print("Merged_List_Descending_order :- ",merge_list)



"""""

# Output:-

# List_01 :-  [10, 50, 35]                       #List 1 : [10, 50, 21, 46, 35]

# **********

# List_02 :- [58, 88, 76, 100]                   #List 2 : [58, 88, 76, 100, 65]

# **********

# Merged_List :- [10, 50, 35, 58, 88, 76, 100]

# **********

# Merged_List_Desc :-  [100, 88, 76, 58, 50, 35, 10]

# *************--Thank You!!--:)**************

"""""
