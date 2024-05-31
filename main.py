# problem 1
# Write a program to check whether a person is eligible to vote or not?
# solution
# age=int(input("Enter your age \t"))
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible  to vote")

# =======================================================
# problem 2
# Write a program to check char is vowel or not.

# soluton
# char=input("Enter  char \t")
# if char=="a" or char=="e" or  char=="i" or char=="o" or char=="u"or char=="A" or char=="I" or  char=="O" or char=="U" or char=="E"    :
#     print("Vowel")  
# else:
#     print("not Vowel")
# ======================================================
# problem 3
# Write a program to check the number is positive or negative. User input.

# solution
# num=int(input("Enter number\t"))
# if num>=0:
#     print("positive ")
# else:
#     print("negative")


# ==============================================
# proble 4
# Write a program to check whether a number is odd or even?
# solution
# num=int(input("Enter number \n"))
# if num%2==0:
#     print("Even")
# else:
#     print("odd")

# ===============================================
# problem 5
# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100
# solution 
# marks=int(input("Enter subject marks out of 100 \n"))
# if marks>=90:
#     print("A+")
# elif marks>=80:
#     print("A")
# elif marks>=70:
#     print("B+")
# elif marks>=60:
#     print("b")
# elif marks>=50:
#     print("c")
# else:
#     print("fails")
# ==================================================
# problem 6
# Write a program to check whether a number is divisible by 7
# solution
# num=int(input(("Enter number ")))
# if num%7==0:
#     print(num,"number is divide by 7")
# else:
#         print(num," number is not divide by 7")
# =======================================================
# problem 7
# Write a program to check if year is leap year.
# solution 
# leap_year= int(input("Enter your years \n"))
# if leap_year%4==0:
#     print("yes this is leap years")
# else:
#     print("no this is not leap year")

#  problem 8
# Write a program to ask user its name and check whether name consists of 5 or more letters
# solution
# name=input("Enter your name \n")
# if len(name)>=5:
#     print("your name consists of 5 or more letters ")
# else:
#     print("your name not consists of 5 or more letters  ")

# ==============================
# problem 9
# Write a program to ask user its name and check whether name consists of 5 or more letters
# # solution
# first_input=int(input("Enter first number\t"))
# second_input=int(input("Enter second number\t"))
# math_input=input("Enter mathematical operator \t")
# if math_input=="+":
#     print(first_input+second_input)
# elif math_input=="-":
#     print(first_input-second_input)
# elif math_input=="*":
#     print(first_input*second_input)
# elif math_input=="/":
#     print(first_input/second_input)
# else:
#     print("this is not mathematical operator.")
# ==================================================
# problem 10
# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# solution
# number=int(input("Enter number:"))
# if number%2==0 and number%3==0:
#     print(number," is divide by 2 and 3 both. ")
# else:
#     print(number,"is  not divide by 2 and 3 both. ")

# ===========================================
# problem 11
#  Write a program that accepts 2 inputs from user and check which number is largest.
# solution
# first_number=int(input("Enter first number \t"))
# second_number=int(input("Enter second number \t"))

# if first_number>second_number:
#     print("the largest number is :",first_number)
# elif second_number>first_number:
#     print("the largest number is :",second_number)
# else:
#     print("both are equal value")
    
# ===================================================
# problem 12
# Write a program that accepts 3 input from user and check which number is largest.
# solution
# num_1=int(input("Enter first number:"))
# num_2=int(input("Enter Second number:"))
# num_3=int(input("Enter third number:"))
# if num_1>num_2 and num_1>num_3:
#     print("the largest number is:",num_1)
# elif num_2>num_3 and num_2>num_3:
#     print("the largest number is:",num_2)

# elif num_3>num_2  and num_3>num_1:
#     print("the largest number is:",num_3)
# else:
#     print("both are equal value")



# ==========================================================================
# problem 13
#  Write a program that accepts 3 input from user and check the second largest.
# solution
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# largest = max(num1, num2, num3)
# second_largest = float("-inf")
# if num1!=largest and num1>second_largest:
#     second_largest=num1
# elif num2!=largest and num2>second_largest:
#     second_largest=num2
# elif num3!=largest and num3>second_largest:
#     second_largest=num3
# if second_largest==float("-inf"):
#     print("All numbers are equal or there is no second largest number.")
# else:
#     print("The second largest number is: ", second_largest)
# ==================================
# problem 14
# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc 
# - RED or red or rEd etc 
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input
# solution
# user_input=input("Enter traffice light color:")
# if user_input=="green":
#     print("Car is allowed to go")
# elif user_input=="yellow":
#     print("car has to wait ")
# elif user_input=="red":
#     print("car has to stop")
# else:
#     print("invalid input")
# ========================================
# problem 15
"""
Write a program that takes two numbers as input and prints:

"First number is greater" if the first number is greater than the second number.
"Second number is greater" if the second number is greater than the first number.
"Both numbers are equal" if the two numbers are equal.
"""

# solution
# first_num=int(input("Enter first number\n"))
# second_num=int(input(" Enter second number\n"))
# if first_num>second_num:
#     print("first number is greater than second number")
# elif second_num>first_num:
#     print("second number is greater than first number")
# else:
#     print("both numbers are equal")
# =================================================
# problem 16
"""
Write a program that takes a password as input and checks its strength:

If the password length is less than 6, print "Weak password".
If the password length is between 6 and 12, print "Moderate password".
If the password length is more than 12, print "Strong password".
"""
# solution
# password=input("Enter your password:")
# # password_convert=int(password)
# if len(password)<6:
#     print("your password is weak password ")
# elif len(password)<=12:
#         print("your password is Moderate password ")
# elif len(password)>12:
#     print("your password is Strong password ")

# ====================================
# problem 17
""""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.
"""
# solution
# salary=int(input("Enter your salary:"))
# years_or_service=int(input("Enter your years or service:"))
# bonus=int(0)
# if years_or_service <5:
#     print("no bonus",bonus)
# elif years_or_service >=5 and years_or_service<10:
#     bonus=0.1*salary+salary
#     print("bonus is 10% of the salary",bonus)
# elif years_or_service>10:
#     bonus=0.2*salary+salary
#     print("bonus is 20% of the salary",bonus)
# else:
#     print("invalid input")
# =============================
# problem 18
"""
Write a program that takes the total amount of a purchase as input and applies a discount:

If the amount is less than $100, no discount.
If the amount is between $100 and $500, apply a 10% discount.
If the amount is more than $500, apply a 20% discount.
Print the final amount after the discount.

"""
# solution
# purchase_amount=int(input("Enter your purchase amount:"))
# discount=float(0)
# if purchase_amount <= 100:
    
#     print("no discount",discount)
# elif purchase_amount>=100 and purchase_amount<=500:
#     discount=0.1*purchase_amount
#     print("your 10% discount is:",discount)

# elif purchase_amount>500:
#         discount=0.2*purchase_amount
#         print("your 20% discount is:",discount)
# ==============================================
# problem 19
"""
Write a program that takes a person's age as input and prints the age group they belong to:

If the age is less than 13, print "Child".
If the age is between 13 and 19 (inclusive), print "Teenager".
If the age is 20 or above:
    If the age is less than 65, print "Adult".
    If the age is 65 or above, print "Senior".
"""
# solution
# age_program=int(input("Enter your age:"))
# if age_program <13:
#     print("you are a child")
# elif age_program>=13 and age_program<=19:
#     print("you are a Teenager")
# elif age_program>=20 and age_program<=65:
#     print("you are adults")
# elif age_program>65:
#     print("you are a senior citizen")
# else:
#     print("invaid age")
# ======================================
# problem 20
"""
Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:

If the customer is a member:
    If the purchase amount is $50 or more, print "Eligible for 10% discount".
    Otherwise, print "Eligible for 5% discount".
If the customer is not a member:
    If the purchase amount is $100 or more, print "Eligible for 5% discount".
    Otherwise, print "No discount".
"""
# solution
# purchase=int(input("Enter purchase amount : -$\n"))
# member=input("Are you member yes or no\n").lower()
# if member=="yes" and purchase<=50:
#     print("Eligible for 10% discount")
# elif member=="yes" and purchase>=50 :
#     print("Eligible for 5% discount")
# else:
#     print("no discount")
# =========================
# problem 21
""""
create the same ATM machine program that we do in last class.
features:
    allow only affiliated_card if age < 60
    allow govt employee regardless of age and affiliated_card
    charge 10 Rs more if grade is less than 18

# hint: filename: if_statement/if_with_nested_if.py
"""
# sloution
# balance = 0
# affiliated_card = True # meezan
# is_senior_citizen = True
# is_govt_employee = True
# high_grade = True


# print("initital balance", balance)

# withdraw_amount = 50

# if balance < withdraw_amount:
#     print("insufficient balance")
    
# deposit_amount = 500

# # balance = balance + deposit_amount
# balance += deposit_amount

# print("after first depost:", balance)

# withdraw_amount = 50
# if withdraw_amount <= balance and (affiliated_card == True or is_senior_citizen):
#     balance = balance - withdraw_amount
#     print("after withdraw:", balance)
# elif is_govt_employee and withdraw_amount <= balance:
#     if high_grade:
#         balance = balance - withdraw_amount
#         print("after withdraw:", balance)
#     elif is_govt_employee and withdraw_amount <= balance + 50:
#        balance -= deposit_amount + 50
        
        