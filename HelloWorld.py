# __author__ = 'dev'
# print('Hello ,World')
# print(1*2)

# print("hello"+"FakeWorld"+"Works")
# greeting = "hello"
# Fake = "helloeeee"
# print(greeting +' '+Fake)
# splitString = "This String has been\nsplit ober\n "
# print(splitString)
#
# tabbedString = "1\t1\t3\t4"
# print(tabbedString)
#
# anotherSplitString = """This String has been split over several lines"""
# print(anotherSplitString)
# a=12
# b=33
# parrot = "Norwegian Blue"
# print(parrot)
# # print(parrot[3])
# print(parrot[-1])
# print(parrot[0:6:7])

# number="9,44,3334,4448,442,548"
# print(number[1::4])
# print("hello" *(4+4))
# today = "frinday"
# print("day" in today)
# print("fri" in today)
# print("thrs"in today)
# print("paroo"in today)
# print("frinday"in today)

# __author__ = 'dev'
# age = 99
# print("My age is"+str(age)+"years")
# print("My age is {0}years".format(age))
# print("My age is %d years"%age)
# print("My age is %d %s, %d %s"%(age,"years",6,"months"))
# for i in range(1,12):
#     print("No. %2d squared is %4d and cubed is %4d"%(i,i**2,i**3))
# print("pi is approximitley %12.69f"%(22/7))

##########################################
__author__ = 'dev'

# for i in range(1,12):
#    print("No {} Square i {} cubed is {:4}".format(i,i**2,i**4))

#####################################################
### name = input("Please enter Your name:")
# age = str(input("How Old are you,{0}?:".format(name)))
# print("My age is:" +age )
#
# if age >= 18:
# 	print("You Are odl Ength to vote")
# else:
# 	print("Please Come back in {0}".format(18-age))
######################################################
# print("Please guess a number between 1 and 10:")
# guess = int(input())
# if guess <5 :
# 	print("Please guess higher")
# 	guess = int(input())
# 	if guess ==5:
# 		print("Well Done ,You guess it")
# 	else:print("Sorry You Have not guesse Correctly")
# elif guess>5:
# 	print("Please guess Lower")
# 	guess = int(input())
# else:
# 	 print("No It's Erro")

# age = int(input("How Old Are You?"))
# if(age>=16) and (age<=65):
# 	print("Have agood day at work")

# if 16 <= age <=65:
# 	print("Have a good Day")
#
# x= input("Please Enter some Text")
# if x:
# 	print("You entered :'{}'".format(x))
# else:
# 	print("You did not enter anything")
# age=int(input("how old are you"))
# if not (age <18):
# 	print("You old ength to vote")
# else:
# 	print("plese come back in {0} years".format(18-age))
#
#
#
# name = input("Please Enter Your name")
# age = int(input("Please Enter Your age {0}".format(name)))
# if (age>18 and age<30):
# 	 print("Welcome "+name+" You Will Go To Holiday")
# else:
# 	print("You Will Not Enter The Holiday")

# for i in range(1,20):
#  	print("i is new {}".format(i))
#
# number = "9,233,238,2384,9230,48"
# for i in range(0,len(number)):
# 	print(number[i])

# number = "9,4434,535,6477,86654,34342,645454"
# cleanedNumber = ''
# for i in range(0,len(number)):
# 	if number[i]in '0124545':
# 		cleanedNumber = cleanedNumber+number[i]
# 		newNumber = int(cleanedNumber)
# 		print("the Number is {}".format(newNumber))
#
#
# number = "9,232,42,484,453,434"
# cleanNumber = ''
# for char in number:
# 	if char in '01283738484':
# 		cleanNumber = cleanNumber+char
# 		newNumber = int(cleanNumber)
# 		print("the number is {}".format(newNumber))

# for state in ['ram','ralod','dskfs','sdfsdi']:
# 	print("this is Num4"+state)
# for i in range(0,288,5):
# 	print("is is {}".format(i))
######FOR LOOP ITERATION #############
# for i in range(1,13):
# 	for j in range(1,13):
# 		print("{1}time{0} is {2}".format(i,j,i*j))
# 		print("========================")

# shopping_list = ["milk","pasta","eggs","span","bread","rice"]
# for item in shopping_list:
# 	if item =='eggs':
# 		break
# 	print("Buy"+item)
#
#
# meal = ['egg','abcon','susage','spam','sdshs','ksdk']
# nasty_food_item = ''
# for item in meal:
# 	if item=='spam':
# 		nasty_food_item = item
# 		break
# if nasty_food_item =='spam':
# 	print("ca't i have anything")

# number = "9,2323,44384,8439,3484"
# clearNumber = ''
# for i in range(0,len(number)):
# 	if number[i]in '03874929832':
# 		clearNumber += number[i]
# newNumber = int(clearNumber)
# print("the number is {}".format(newNumber))
#
# x=21
# x+=1
# print(x)
# x-=4
# print(x)
#
# x**=2
# print(x)
# avilable_exists = ['easet','north','sout']
# chosen_exist=""
# while chosen_exist not in avilable_exists:
# 	chosen_exist = input("Please Choose the direction")
# while chosen_exist in avilable_exists:
# 	chosen_exist = print("it is Hear")

#
# ipAdress = input("Please enter an IP adress:")
# print(ipAdress.cont("."))

parrot_list = ["non pinin ","no more","a stiff","bereft of live"]
parrot_list.append("A Norwegian Coole")
for state in parrot_list:
	print("This parrot is "+state)



############################ PRACTICE LIST###################################
# even = [11,23,34,55,58]
# odd = [1,2,3,8,6]
#
# numbers = even+odd
#
# numbersOrder = sorted(numbers)
# print(numbersOrder)
#
# if numbers==numbersOrder:
# 	print("The list are not equel")
# else:
# 	print("The lists is equel")
#
# if numbersOrder ==sorted(numbers):
# 	print("The list are not equel")
# else:
# 	print("The lists is equel")
#
#
#
#
##################################################
###############################################
list_1 = [5,6]
list_2 = list()

print("list1:{}".format(list_1))
print("list2:{}".format(list_2))

if list_1 ==list_2:
	print("The list are equal")
else:
	print("the lists not equal")

print(list("The day is Very Nice"))
################################################
#####################################
# even = [2,3,4,5,6]
# odd=[1,3,5,7,9]
#
# numbers = [even,odd]
# print(numbers)
#
# for set_num in numbers:
# 	print(set_num)
#
# for value in set_num:
# 	print(value)


































































































































































































































































































































































































































































































































