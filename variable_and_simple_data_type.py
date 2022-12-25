message = "Hello Python world!"
print(message)

# When run the above code you see the output:
# Hello Python world!

"""We’ve added a variable named message. Every variable holds a value, which 
is the information associated with that variable. In this case the value is the 
text “Hello Python world!” 
Adding a variable makes a little more work for the Python interpreter. 
When it processes the first line, it associates the text “Hello Python world!” 
with the variable message. When it reaches the second line, it prints the value 
associated with message to the screen"""

message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)

# Now when you run the above code, you should see two lines of output:
# Hello Python world! 
# Hello Python Crash Course world!

"""You can change the value of a variable in your program at any time, 
and Python will always keep track of its current value."""

# Simple Data types 
"""Because most programs define and gather some sort of data, 
and then do something useful with it, it helps to classify different types of data. """

# Strings
"""The first data type we’ll look at is the string. Strings are quite simple at first glance, 
but you can use them in many different ways."""

"""A string is simply a series of characters. Anything inside quotes is considered a string in Python, 
and you can use single or double quotes around your strings like this:"""

# -> "This is a string."
# -> 'This is also a string.'

# Changing Case in a String with Methods
"""One of the simplest tasks you can do with strings is change the case of the words in a string"""

name = "ada lovelace"
print(name.title())

# The output of the abvoe code: -> Ada Lovelace

"""In this example, the lowercase string "ada lovelace" is stored in the variable name. The method title() appears after the variable in the print() statement. A method is an action that Python can perform on a piece of data. The 
dot (.) after name in name.title() tells Python to make the title() method 
act on the variable name. Every method is followed by a set of parentheses, 
because methods often need additional information to do their work. 
That information is provided inside the parentheses. The title() function 
doesn’t need any additional information, so its parentheses are empty. 
title() displays each word in titlecase, where each word begins with a 
capital letter. This is useful because you’ll often want to think of a name as a 
piece of information. For example, you might want your program to recognize the input values Ada, ADA, and ada as the same name, and display all of 
them as Ada"""

"""Several other useful methods are available for dealing with case as well. 
For example, you can change a string to all uppercase or all lowercase letters 
like this:"""

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# The output of the above code: -> ADA LOVELACE
#                               -> ada lovelace


# Combining or Concatenating Strings
"""It’s often useful to combine strings. For example, you might want to store 
a first name and a last name in separate variables, and then combine them 
when you want to display someone’s full name:"""


first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# The output of the above code: ->ada lovelace

# Python uses the plus symbol (+) to combine strings. 
# This method of combining strings is called concatenation.

"""You can use 
concatenation to compose complete messages using the information you’ve 
stored in a variable. Let’s look at an example:"""

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

# The output of the above code: -> Hello, Ada Lovelace!

"""You can use concatenation to compose a message and then store the 
entire message in a variable:"""

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# The output of the above code: ->  Hello, Ada Lovelace

# Adding Whitespace to Strings with Tabs or Newlines
"""
In programming, whitespace refers to any nonprinting character, such as 
spaces, tabs, and end-of-line symbols. You can use whitespace to organize 
your output so it’s easier for users to read.
To add a tab to your text, use the character combination \t
"""

# >>> print("Python")
# Python 
# >>> print("\tPython")
#     Python

# To add a newline in a string, use the character combination \n:

# >>> print("Languages:\n\tPython\n\tC\n\tJavaScript") 
# Languages: 
#     Python 
#     C 
#     JavaScript

# Stripping Whitespace

"""It’s important to think about whitespace, because often you’ll want to 
compare two strings to determine whether they are the same. For example, 
one important instance might involve checking people’s usernames when 
they log in to a website. Extra whitespace can be confusing in much simpler 
situations as well. Fortunately, Python makes it easy to eliminate extraneous 
whitespace from data that people enter"""

# >>> favorite_language = 'python ' 
# >>> favorite_language 
# 'python ' 
# >>> favorite_language.rstrip()
# 'python'
# >>> favorite_language
# 'python '

"""To remove the whitespace from the string permanently, you have to 
store the stripped value back into the variable:"""

# >>> favorite_language = 'python ' 
# >>> favorite_language = favorite_language.rstrip()
# >>> favorite_language 
# 'python' 

"""You can also strip whitespace from the left side of a string using the 
lstrip() method or strip whitespace from both sides at once using strip():"""

# >>> favorite_language = ' python ' 
# >>> favorite_language.rstrip()
# ' python' 
# >>> favorite_language.lstrip()
# 'python ' 
# >>> favorite_language.strip()
# 'python'

# Numbers

"""Numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so 
on. Python treats numbers in several different ways, depending on how they 
are being used. Let’s first look at how Python manages integers, because 
they are the simplest to work with"""

"""Integers
You can add (+), subtract (-), multiply (*), and divide (/) integers in Python."""

# >>> 2 + 3 
# 5 
# >>> 3 - 2 
# 1 
# >>> 2 * 3
# 6 
# >>> 3 / 2
# 1.5

# Python uses two multiplication symbols to represent exponents:

# >>> 3 ** 2
# 9 
# >>> 3 ** 3
# 27 
# >>> 10 ** 6
# 1000000

"""Python supports the order of operations too, so you can use multiple 
operations in one expression. You can also use parentheses to modify the 
order of operations so Python can evaluate your expression in the order 
you specify. For example:"""

# >>> 2 + 3*4
# 14
# >>> (2 + 3) * 4
# 20

# Floats
# Python calls any number with a decimal point a float. 

# >>> 0.1 + 0.1
# 0.2 
# >>> 0.2 + 0.2 
# 0.4 
# >>> 2 * 0.1 
# 0.2 
# >>> 2 * 0.2 
# 0.4

# Comments
"""Comments are an extremely useful feature in most programming languages. 
Everything you’ve written in your programs so far is Python code. As your 
programs become longer and more complicated, you should add notes within 
your programs that describe your overall approach to the problem you’re 
solving. A comment allows you to write notes in English within your programs."""

# How Do You Write Comments?
"""In Python, the hash mark (#) indicates a comment. Anything following a 
hash mark in your code is ignored by the Python interpreter. For example:"""

# Say hello to everyone.
# print("Hello Python people!")

# Python ignores the first line and executes the second line. 