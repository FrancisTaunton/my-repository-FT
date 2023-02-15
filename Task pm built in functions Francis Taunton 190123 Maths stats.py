# using built-in functions 
#preamble 
print("Welcome to the super function calculator tool by Francis")
print("You will be asked to enter some numbers below.")
print("Whole numbers ONLY please. No Decimals")
print("\n")
#defines the list of input numbers input string
input_string = input("Enter the numbers you want checked, seperated by spaces: ")
print("\n")
#defines new list called user list
user_list = input_string.split()
# print list
print("Your list of numbers is : ", user_list)
print("\n")
# starts a loop to change each item (i) in list into an integer, using len 
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
#print number of numbers
print("You have entered ", len(user_list), "numbers")
print("\n")
#print the numbers sorted from lowest to highest
print("Your list of numbers in order is:", sorted(user_list))
print("\n")
# Calculating the sum of list elements
print("The sum of the numbers = ", sum(user_list))
print("\n")
# calculate the maximum number
print("The highest number in your list is ", max(user_list))
print("\n")
#calculate the minimum number
print("The lowest number in your list is ", min(user_list))
print("\n")
#you have to import the statistics functions first
import statistics
#print average using rounding too
print("The Mean or average of the numbers (to 2 d.p.) = ", round(statistics.mean(user_list), 2))
#print the median
print("The median number in the list is ", statistics.median(user_list))
#print the mode
print("The number or numbers that appear most, the Mode, is ", statistics.multimode(user_list))
print("\n")
#print smallprint
print("I do hope these stats are right, thanks Francis")

      


