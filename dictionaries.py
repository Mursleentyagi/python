"""A dictionary in Python is a collection of key-value pairs. Each key is connected 
to a value, and you can use a key to access the value associated with that key. 
A key’s value can be a number, a string, a list, or even another dictionary. 
In fact, you can use any object that you can create in Python as a value in a 
dictionary."""


"""Consider a game featuring aliens that can have different colors and point 
values. This simple dictionary stores information about a particular alien:"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# The dictionary alien_0 stores the alien’s color and point value. 
# The two print statements access and display that information, as shown here:
# green
# 5

"""In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces."""

alien_0 = {'color': 'green', 'points': 5}
"""A key-value pair is a set of values associated with each other. When you 
provide a key, Python returns the value associated with that key. Every key 
is connected to its value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value pairs as you want in a 
dictionary."""
"""The simplest dictionary has exactly one key-value pair, as shown in this 
modified version of the alien_0 dictionary:"""
alien_0 = {'color': 'green'}

# Accessing Values in a Dictionary
"""To get the value associated with a key, give the name of the dictionary and 
then place the key inside a set of square brackets, as shown here:"""
alien_0 = {'color': 'green'}
print(alien_0['color'])

# Adding New Key-Value Pairs
"""Dictionaries are dynamic structures, and you can add new key-value pairs 
to a dictionary at any time. For example, to add a new key-value pair, you 
would give the name of the dictionary followed by the new key in square 
brackets along with the new value."""
"""Let’s add two new pieces of information to the alien_0 dictionary: the 
alien’s x- and y-coordinates, which will help us display the alien in a particular position on the screen. Let’s place the alien on the left edge of the 
screen, 25 pixels down from the top. Because screen coordinates usually 
start at the upper-left corner of the screen, we’ll place the alien on the left 
edge of the screen by setting the x-coordinate to 0 and 25 pixels from the 
top by setting its y-coordinate to positive 25, as shown here:"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# The output of the above code:
# {'color': 'green', 'points': 5}
# {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

"""Here we define an empty alien_0 dictionary, and then add color and 
point values to it."""
# The output of the above code:
# {'color': 'green', 'points': 5}


# Modifying Values in a Dictionary 
"""To modify a value in a dictionary, give the name of the dictionary with the 
key in square brackets and then the new value you want associated with 
that key. For example, consider an alien that changes from green to yellow 
as a game progresses:"""

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# The output of the above code:
# The alien is green.
# The alien is now yellow.

# Removing Key-Value Pairs
"""When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair. 
All del needs is the name of the dictionary and the key that you want to 
remove."""
"""For example, let’s remove the key 'points' from the alien_0 dictionary 
along with its value:"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# The output of the above code:
# {'color': 'green', 'points': 5}
# {'color': 'green'}
# Be aware that the deleted key-value pair is removed permanently. 

# A Dictionary of Similar Objects
"""The previous example involved storing different kinds of information about 
one object, an alien in a game. You can also use a dictionary to store one 
kind of information about many objects."""
"""For example, say you want to poll a number of people and ask them what their favorite programming language 
is."""

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

"""To use this dictionary, given the name of a person who took the poll, 
you can easily look up their favorite language:"""

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}
print("Sarah's favorite language is " +favorite_languages['sarah'].title() +".")

# The output of the above code:
# Sarah's favorite language is C.


# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
"""Before we explore the different approaches to looping, let’s consider a 
new dictionary designed to store information about a user on a website. 
The following dictionary would store one person’s username, first name, 
and last name:"""

user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

"""As shown at line 1, to write a for loop for a dictionary, you create names for 
the two variables that will hold the key and value in each key-value pair. You 
can choose any names you want for these two variables. This code would work 
just as well if you had used abbreviations for the variable names, like this:"""
# for k, v in user_0.items()

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favorite_languages.items(): 
     print(name.title() + "'s favorite language is " +language.title() + ".")

# The output of the above code
# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Phil's favorite language is Python.
# Edward's favorite language is Ruby.

# Looping Through All the Keys in a Dictionary
"""The keys() method is useful when you don’t need to work with all of the 
values in a dictionary. """

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in favorite_languages.keys():
    print(name.title())

# The output of the above code is
# Jen
# Sarah
# Phil
# Edward

# Looping Through a Dictionary’s Keys in Order
"""A dictionary always maintains a clear connection between each key and 
its associated value, but you never get the items from a dictionary in any 
predictable order. That’s not a problem, because you’ll usually just want 
to obtain the correct value associated with each key."""
"""One way to return items in a certain order is to sort the keys as they’re 
returned in the for loop. You can use the sorted() function to get a copy of 
the keys in order:"""

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# The output of the above code is
# Edward, thank you for taking the poll. 
# Jen, thank you for taking the poll. 
# Phil, thank you for taking the poll. 
# Sarah, thank you for taking the poll.

# Looping Through All Values in a 
"""If you are primarily interested in the values that a dictionary contains, 
you can use the values() method to return a list of values without any keys."""

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# The output of the above code is
# The following languages have been mentioned: 
# Python 
# C 
# Python 
# Ruby

"""This approach pulls all the values from the dictionary without checking 
for repeats. That might work fine with a small number of values, but in a 
poll with a large number of respondents, this would result in a very repetitive list. To see each language chosen without repetition, we can use a set. 
A set is similar to a list except that each item in the set must be unique:"""
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

"""When you wrap set() around a list that contains duplicate items, Python 
identifies the unique items in the list and builds a set from those items. At 1
we use set() to pull out the unique languages in favorite_languages.values().
The result is a nonrepetitive list of languages that have been mentioned 
by people taking the poll:"""

# The output of the above code is
# The following languages have been mentioned:
# Python
# C
# Ruby


# Nesting
"""Sometimes you’ll want to store a set of dictionaries in a list or a list of 
items as a value in a dictionary. This is called nesting. You can nest a set 
of dictionaries inside a list, a list of items inside a dictionary, or even a 
dictionary inside another dictionary."""

# A List of Dictionaries
"""The alien_0 dictionary contains a variety of information about one alien, 
but it has no room to store information about a second alien, much less a 
screen full of aliens. How can you manage a fleet of aliens? One way is to 
make a list of aliens in which each alien is a dictionary of information about 
that alien. For example, the following code builds a list of three aliens:"""

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# The output of the above code:
# {'color': 'green', 'points': 5} 
# {'color': 'yellow', 'points': 10} 
# {'color': 'red', 'points': 15}


"""A more realistic example would involve more than three aliens with 
code that automatically generates each alien. In the following example we 
use range() to create a fleet of 30 aliens:"""

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
 
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# The output of the above code:
# {'speed': 'slow', 'color': 'green', 'points': 5} 
# {'speed': 'slow', 'color': 'green', 'points': 5} 
# {'speed': 'slow', 'color': 'green', 'points': 5} 
# {'speed': 'slow', 'color': 'green', 'points': 5} 
# {'speed': 'slow', 'color': 'green', 'points': 5} 
# ...
# Total number of aliens: 30


"""These aliens all have the same characteristics, but Python considers each 
one a separate object, which allows us to modify each alien individually.
How might you work with a set of aliens like this? Imagine that one 
aspect of a game has some aliens changing color and moving faster as the 
game progresses. When it’s time to change colors, we can use a for loop and 
an if statement to change the color of aliens. For example, to change the 
first three aliens to yellow, medium-speed aliens worth 10 points each, we 
could do this:"""

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
 
for alien in aliens[0:3]:
   if alien['color'] == 'green':
      alien['color'] = 'yellow'
      alien['speed'] = 'medium'
      alien['points'] = 10
 
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")

# The output of the above code:
# {'speed': 'medium', 'color': 'yellow', 'points': 10} 
# {'speed': 'medium', 'color': 'yellow', 'points': 10} 
# {'speed': 'medium', 'color': 'yellow', 'points': 10} 
# {'speed': 'slow', 'color': 'green', 'points': 5} 
# {'speed': 'slow', 'color': 'green', 'points': 5} 
# ...


# A List in a Dictionary
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# The output of the above code:
# Jen's favorite languages are: 
#  Python 
#  Ruby 
# Sarah's favorite languages are: 
#  C 
# Phil's favorite languages are: 
#  Python 
#  Haskell 
# Edward's favorite languages are: 
#  Ruby 
#  Go


# A Dictionary in a Dictionary
users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# The output of the above code:
# Username: aeinstein 
#    Full name: Albert Einstein 
#    Location: Princeton 
# Username: mcurie 
#    Full name: Marie Curie 
#    Location: Paris