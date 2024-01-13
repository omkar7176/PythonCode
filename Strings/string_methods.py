# # String Methods

''' 1. upper() Converts all lowercase characters in string into uppercase'''

name = "Mahendra_Singh_Dhoni"
# print(name.upper())

# #2nd Way
str1 = "abcdefghiklmnopqrst"
str2 = str1.upper()
# print(str2)





'''2. lower() converts all uppercase characters in lowercase'''

Fname = "STEVE_JOBS"
print(Fname.lower())

# #2nd Way
aname = "KANYE_WEST"
bname = aname.lower()
print(bname)





'''3. title(): converting the first letter of every word to uppercase(capital)
               and keeping the rest of the letters lowercase.'''

headline = "heLLo eVRYone, hOW ARE you ?"
line = headline.title()
print(line)

# #2nd Way
intro = "To KAISE ho aAp saB log"
print(intro.title())





'''4. capitalize():  returns a copy of the original string and converts the first character of the string to a capital (uppercase) letter 
                     while making all other characters in the string lowercase letters.'''

ide = "visual studio code"
print(ide.capitalize())
#OP : Visual studio code





'''5. swapcase() method: converts all uppercase characters to lowercase and vice versa 
                         of the given string and returns it.''' 

# prints after swapping all cases


string = "TecHnoLOGy"
print(string.swapcase())
# #OP: tEChNOlogY

string = "artificial_intelligence"
print(string.swapcase())
# #OP: ARTIFICIAL_INTELLIGENCE 

string = "DEVELOPMENT + OPERATION"
print(string.swapcase())
# #OP: development + operation





'''6. count(): it count the number of specific letter or word also in string.'''

my_string = "Banana"
other_string = my_string.count("a")
print(other_string)
# #OP: 3

# # it will count the word also.
string = "okay ok okay ok okay yes yes"
string2 = string.count("okay")
print(string2)
# #OP: 3





''' 7. endswith() and startswit(), the answer will get in "True" & "False"'''

fruit = "Mango"
string = fruit.startswith("Man")
print(string)
# # OP: True


fruit = "Mango"
string = fruit.endswith("go")
print(string)
# OP: True





'''8. expandtabs(): specified the amount of space to be substitued the string'''

string = "Hello\tEveryone\tMorning"
print(string.expandtabs(20))
#OP: Hello               Everyone            Morning






'''9. find(): searching the word in string & output gives you the index numb'''

string = " hello world is the first code of every programmer"
print(string.find("first"))
# # OP: 20






'''10.index(): searching the word in string & output gives you the index numb'''

string = "first code of every programmer"
print(string.find("code"))
# OP: 6






'''11.format(): we can use as the f-string the forrmat() method
              - allows developers to create formatted strings by embedding variables and values into placeholders within a template string.
              - format() function has been introduced for handling complex string formatting more efficiently.'''

name = "rocky"
age = 23
location = "Pune"

# 1st way:
print(f"My name is {name}, age is {age} & live in {location}.")

# 2nd way
print("My name is {0}, age is {1} & live in {2}.".format(name, age, location))

# 3rd Way
string = "My name is {0}, age is {1} & live in {2}."
print(string.format(name, age, location))

# 4th way
string1 = "{} is a popular programming language."
print(string1.format("Python"))






'''12.format_map(): is an inbuilt function in Python, which is used to return a dictionary key’s value.'''

# 1st way
player = {'x':"Rohit", 'y':"Virat", 'z':"Shubhman"}
print("World cup 2023 indian player name are {x}, {y}, {z} & etc.".format_map(player))

# 2nd way --> it is .format() still we can use with dictionary.
print("{x} is captain of Mumbai & {y} is captain of India, player {z}".format(**player))

# 3rd way
emp = {'name': ["Shon", "John"],
               'age': [25, 26],
               'add': ["Pune", "Mumbai"]}
print("The emp name is {name[0]} & age {age[0]} & live in {add[0]}".format_map(emp))

print("The emp name is {name[1]} & age {age[1]} & live in {add[1]}".format_map(emp))





''' 13 join() : returns a concated things '''
# ex.1
str = "omkar"
print("-".join(str))

# ex.2
numb = ('9123451278')
s = "-"
result = s.join(numb)
print(result)






''' 14. replace() : Replace the word '''

string = "Hello EveryOne"
print(string.replace("Hello", "Byee"))
print(string.replace("EveryOne", "folks"))
#OP: Byee EveryOne  ||  Hello folks