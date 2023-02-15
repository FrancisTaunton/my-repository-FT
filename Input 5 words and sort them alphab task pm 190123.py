#opens empty list called input_words
input_words = []
#user preamble
print("This program will sort five words alphabetically.")
print("\n")
print("Please enter only 1 word after each prompt below.")
#starts counter for word entry and populates list with words
for i in range(1, 6):
    print("Enter word:", i, )
    item =(input())
    input_words.append(item)
#print list unsorted
print("\n")
print("Your unsorted word list is ", input_words)
#sorts
input_words.sort()
print("\n")
# print sorted list
print('Your list sorted alphabetically is: ', input_words)
print("\n")
print("Thank you for using Francis' incredible word sorter that took hours to make")





