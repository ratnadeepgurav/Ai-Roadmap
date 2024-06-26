# String :- sequence of characters which encoded with quote
            #string are immutable

# string start from 0 index to length -1 index

name="Ratnadeep"

print(name[0:4]) #Ratn (start from 0 index to length-1)

print(name[0:5]) #Ratna (start from 0 index to length-1)    

print(name[-9:-1]) #Ratnadee (start from 0 index to length-1)

print(name[1:9]) #atnadeep (start from 0 index to length-1)

print(name[:4]) #Ratn (start from 0 index to length-1)

print(name[2:]) #tnadeep (start from 0 index to length-1)


#skiping the characters in the string

word = "amazing"

print(word[1:6:2]) #am (start from 0 index to length-1)

word2= "Loyalty"

print(word2[::2]) #Lyt (start from 0 index to length-1)

# String Function 

print(len(word)) #length of word string 

print(word.upper()) #upper case

print(word.lower()) #lower case

print(word.capitalize()) #capitalize

print(word.count("a")) #count of a in word string

print(word.find("a")) #find of a in word string

print(word.isalpha()) #isalpha

print(word.endswith("zing")) #Check given string is ended with word string

print(word.startswith("ama"))

print(word.replace("a","A")) #replace a with A in word string


#Escape Sequence character

print("Hello\nWorld") #new line

print("Hello\tWorld") #tab

print("Hello\bWorld") #backspace

print("Hello paragraph \f World \"this is escape sequence character\"") 


# string Practice set 

#display user entered name followed by good afternoon using input function

a=input("Enter name")

print(f"Good afternoon {a}")


#replace with name and date
letter = '''
Dear <|Name|>
You are Selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Ratnadeep").replace("<|Date|>","22/07/2024"))



#Detect double spaces from string

string = "I am Ratnadeep  "

print(string.find("  "))

#replace double spaces with single spaces

string = "I am  Ratnadeep"

print(string.replace("  "," "))


#TO format following string using escape sequences character

letter = "Dear Ratnadeep,\n this \"python\" course is nice.\t Thanks!"

print(letter)