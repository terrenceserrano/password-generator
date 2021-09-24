#create a program that will produce a strong password

#declare the module that we need to use

import random
import array

#declare the max length of the password

max = 12

#declare the arrays of the letters, numbers, and characters we need to use

num = ["0", "1", "2","3","4","5","6","7","8","9","0"]
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","p","w","x","y","z"]
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

#combining all the variables

combined = num + lower + upper + symbol

#randomizing all the variables inside the array

rand_num = random.choice(num) #we use the random.choice for randomizing atleast one character
rand_lower = random.choice(lower)
rand_upper = random.choice(upper)
rand_symbol = random.choice(symbol)

#this is where we combine the selected characters
#but this is only 4 characters we need atleast 12

temp = rand_num + rand_lower + rand_upper + rand_symbol

#this is where we combine the first four of the selected characters
#we are going to use the for loops

for x in range(max - 4): #we use the arguement of max - 4 bacause we already have the 4 characters

    temp = temp + random.choice(combined) #this means that the temp of 4 plus the random choice in the combined list

    #this is where we convert it into an array and shuffle it to prevent from having a consistent pattern

    temp_pass = array.array("u", temp)
    random.shuffle(temp_pass)

#this is where we concatenate the temporary password array and append the chars

password = "" #this will make the password into a string

for x in temp_pass:

    password = password + x

print(password) #if this is indented it will print 12 samples of passwords, if not it will print only one 12 char password


























