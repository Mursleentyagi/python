# What Is a List?
"""A list is a collection of items in a particular order. You can make a list that 
includes the letters of the alphabet, the digits from 0–9, or the names of 
all the people in your family.
the items in your list don’t have to be related in any particular way. Because 
a list usually contains more than one element, it’s a good idea to make the 
name of your list plural, such as letters, digits, or names. 
In Python, square brackets ([]) indicate a list, and individual elements 
in the list are separated by commas"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# The output of the above line of code:
# ['trek', 'cannondale', 'redline', 'specialized']

# Accessing Elements in a List
"""To access an element in a list, write the name of the list followed by the index of the item 
enclosed in square brackets."""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
# The output of the above code:
# trek

# You can also use the string method on any element in list.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
# The output of the above code:
# Trek

# Index Positions Start at 0, Not 1
# Python considers the first item in a list to be at position 0, not position 1.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
# The output of the above code:
# cannondale
# specialized

"""Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the """

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
# The output of the above code:
# specialized

"""Using Individual Values from a List
You can use individual values from a list just as you would any other variable. For example, you can use concatenation to create a message based on 
a value from a list."""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
# The output of the above code:
# My first bicycle was a Trek.

# Changing, Adding, and Removing Elements
"""Most lists you create will be dynamic, meaning you’ll build a list and 
then add and remove elements from it as your program runs its course. For 
example, you might create a game in which a player has to shoot aliens out 
of the sky. You could store the initial set of aliens in a list and then remove 
an alien from the list each time one is shot down. Each time a new alien 
appears on the screen, you add it to the list. Your list of aliens will decrease 
and increase in length throughout the course of the game. """

# Modifying Elements in a List
"""The syntax for modifying an element is similar to the syntax for accessing 
an element in a list. To change an element, use the name of the list followed 
by the index of the element you want to change, and then provide the new 
value you want that item to have"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# The output of the above code:
# ['honda', 'yamaha', 'suzuki']
# ['ducati', 'yamaha', 'suzuki']

# Adding Elements to a List
"""You might want to add a new element to a list for many reasons. For 
example, you might want to make new aliens appear in a game, add new 
data to a visualization, or add new registered users to a website you’ve 
built. Python provides several ways to add new data to existing lists."""

# Appending Elements to the End of a List
"""The simplest way to add a new element to a list is to append the item to the 
list. When you append an item to a list, the new element is added to the end 
of the list."""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
# The output of the above code:
# ['honda', 'yamaha', 'suzuki']
# ['honda', 'yamaha', 'suzuki', 'ducati']

"""The append() method makes it easy to build lists dynamically. For 
example, you can start with an empty list and then add items to the list 
using a series of append() statements."""

motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)
# The output of the above code:
['honda', 'yamaha', 'suzuki']

# Inserting Elements into a List
"""You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element and the 
value of the new item"""

motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati')
print(motorcycles)
# The output of the above code:
# ['ducati', 'honda', 'yamaha', 'suzuki'] 

# Removing Elements from a List
"""Often, you’ll want to remove an item or a set of items from a list. For 
example, when a player shoots down an alien from the sky, you’ll most 
likely want to remove it from the list of active aliens. Or when a user 
Introducing Lists 43
decides to cancel their account on a web application you created, you’ll 
want to remove that user from the list of active users. You can remove an 
item according to its position in the list or according to its value."""

# Removing an Item Using the del Statement
"""If you know the position of the item you want to remove from a list, you can 
use the del statement. """

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
del motorcycles[0] 
print(motorcycles)
# The output of the above code:
# ['honda', 'yamaha', 'suzuki']
# ['yamaha', 'suzuki']

# Removing an Item Using the pop() Method
"""Sometimes you’ll want to use the value of an item after you remove it from a 
list. For example, you might want to get the x and y position of an alien that 
was just shot down, so you can draw an explosion at that position. In a web 
application, you might want to remove a user from a list of active members 
and then add that user to a list of inactive members.
The pop() method removes the last item in a list, but it lets you work 
with that item after removing it. The term pop comes from thinking of a 
list as a stack of items and popping one item off the top of the stack. In 
this analogy, the top of a stack corresponds to the end of a list."""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)
# The output of the above code:
# ['honda', 'yamaha', 'suzuki'] 
# ['honda', 'yamaha']
# suzuki

"""How might this pop() method be useful? Imagine that the motorcycles 
in the list are stored in chronological order according to when we owned 
them. If this is the case, we can use the pop() method to print a statement 
about the last motorcycle we bought:"""

motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")
# The output of the above code:
# The last motorcycle I owned was a Suzuki.

# Popping Items from any Position in a List
"""You can actually use pop() to remove an item in a list at any position by 
including the index of the item you want to remove in parentheses."""

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
# The output of the above code:
# The first motorcycle I owned was a Honda.

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# The output of the above code:
# ['honda', 'yamaha', 'suzuki', 'ducati'] 
# ['honda', 'yamaha', 'suzuki'] 

"""You can also use the remove() method to work with a value that’s being 
removed from a list. Let’s remove the value 'ducati' and print a reason for 
removing it from the list:"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
# The output of the above code:
# ['honda', 'yamaha', 'suzuki', 'ducati'] 
# ['honda', 'yamaha', 'suzuki']
# A Ducati is too expensive for me.

# Organizing a List
"""Often, your lists will be created in an unpredictable order, because you can’t 
always control the order in which your users provide their data. Although 
this is unavoidable in most circumstances, you’ll frequently want to present 
your information in a particular order. Sometimes you’ll want to preserve the 
original order of your list, and other times you’ll want to change the original order. Python provides a number of different ways to organize your lists, 
depending on the situation"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# The output of the above code:
# ['audi', 'bmw', 'subaru', 'toyota'] 

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# The output of the above code:
# Here is the original list: 
# ['bmw', 'audi', 'toyota', 'subaru'] 
# Here is the sorted list: 
# ['audi', 'bmw', 'subaru', 'toyota']
# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']


# Printing a List in Reverse Order
"""To reverse the original order of a list, you can use the reverse() method. 
If we originally stored the list of cars in chronological order according to 
when we owned them, we could easily rearrange the list into reverse chronological order:"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# The output of the above code:
# ['bmw', 'audi', 'toyota', 'subaru'] 
# ['subaru', 'toyota', 'audi', 'bmw']

"""Notice that reverse() doesn’t sort backward alphabetically; it simply 
reverses the order of the list:"""
"""The reverse() method changes the order of a list permanently, but you 
can revert to the original order anytime by applying reverse() to the same 
list a second time."""

# Finding the Length of a List
# You can quickly find the length of a list by using the len() function.
# >>> cars = ['bmw', 'audi', 'toyota', 'subaru']
# >>> len(cars)
# 4