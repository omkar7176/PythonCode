# ** String Manipuation in Python** by Javatpoint

# 1.center()
text = "Python"
addtext = text.center(12,"*")
print(addtext)

# OUTPUT : ***Python***

# ** String Spliting **

sentence = "Hello everyone, my name is omkar & I live in India"
words = sentence.split()
print(words)

# # 2nd way
print(sentence.split())


fruit = "apple, orange, grapes, banana,watermelon"
print(fruit.split(','))

# OUTPUT: ['apple', ' orange', ' grapes', ' banana', 'watermelon']


# **  Eliminating Unnecessary Character of a String  -- strip() **
text = "!!!@@Hello World!!@@"
print(text.strip("!@"))

# 2nd way
another_vari = text.strip("!@")
print(another_vari)


# ** Search  the word in string or in substring

quote = "by learning the things, the learn never stop, through learning amkes better"
print(quote.find("learn"))
print(quote.find("goo"))

# 2nd way
line = quote.find("teach") #if the answer is wrong will show -1
print(line)