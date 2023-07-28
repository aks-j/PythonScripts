Create function for a given string, get the middle 5 characters
 Example :-

 Input String :- pythonscripts

 Expected Output :- onscr

"""""

#Function Declare
def printMiddleCharacter(str,chara):
    len_str=len(str)
    middle_index=len_str // 2
    if len_str % 2 ==0:
        first_char=middle_index-chara // 2
        last_char=first_char+chara
    else:
        first_char=middle_index-chara // 2
        last_char= first_char+chara

    if middle_chara_count >= 1:
        print("****")
        middle_char = str[first_char:last_char]
        print(f'Middle {chara} character are:-{middle_char}')
    else:
        middle_char = str[first_char:last_char]
        print(f'Middle {chara} character are:-{middle_char}')
        print("Not getting middle character of",Input_Char)

#User Prompt
Input_Char=input("Enter The Character:- ")
#User Prompt
middle_chara_count=int(input("How many middle character required:- "))
if middle_chara_count<=len(Input_Char):
    #function call
    printMiddleCharacter(Input_Char,middle_chara_count)
else:
    print("Length of string is less than the middle character count")



# Output:-

#string "pythonscripts" 5 middle characters output:- onscr
#string "Administrator" 5 middle characters output:- nistr
#string "Entertainment" 5 middle characters output:- rtain
#string "Development" 5 middle characters output:- elopm


'''''
# *************--Thank You!!--:)**************
'''''
