#To calculate number of characters in string and storing in dictionary

str1=input("Enter a string : ")

#Using built in len function
numChars=len(str1)

spaces=0

#Calculating number of spaces
for x in str1:
    if x==" ":
        spaces=spaces+1

numChars=numChars-spaces

#Storing into dictionary
dict1={"numOfChars" : numChars}
print(dict1)
