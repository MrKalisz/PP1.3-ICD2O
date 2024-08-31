# Lesson plan
  
**Output**

printing without a new line
print("Sample Output", end = "") #Replaces ending newline character with nothing.  Anything can be put in the quotations to replace the newline character.

newline character _\n_

escape character _\_

Concatenation

Example Lesson:

'''
Lesson 3 - Using Strings
Author: Mr. Kalisz
Date Created: September 4th, 2023
Date Last Modified: September 4th, 2023
'''

#Output review

#Can output any type
print("hello") #Strings
print(5) #Integers
print(3.4) #Floats

#output without a newline

print ("hello", end = "") #Must have a comma after what you want to output, then end = ""
print ("This should be on the same line")

#This replaces the usual end of the output which is the newline character (see below)



#Escape Character "\"

#The escape character (backslash) is used to change the usage of a character in the string.
#If it has a special function, such as the escape character or quoation, they become a normal character.
#If it is a normal character, it may give it a special function.

#removing special function
print("\\ this is a backslash") #escape the escape character.
print("\" This is a double quotation") #Escape a strings ending character (quotation)

#Giving a special function.

#newline character - "\n"  Creating a newline without another print statment
#This is the standard end to a print statement

print("Hello\nbye") #Adds a new line between Hello and bye

#tab - "\t"