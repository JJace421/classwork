#1
word = input("Word: ")

for char in word:
    if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
        print(char)

# #2
num_list = [3,66,9,54,21,8]

for num in num_list:
    if num > 10:
        print(num)

#3
num_list2 = [21,54,6,87,51,42]

for num in num_list2:
    print (max(num_list2))
#the max number seems to be printed 6 times. number of numbers in the list. I dont know how to go from here.

#4
name = "Bob"

for char in range(len(name)):
    print(char, name[char])
