"""The concept of looping is important because it’s one of the most common 
ways a computer automates repetitive tasks.""" 

# Looping Through an Entire List
"""Let’s say we have a list of magicians’ names, and we want to print out 
each name in the list. We could do this by retrieving each name from the 
list individually, but this approach could cause several problems. For one, 
it would be repetitive to do this with a long list of names. Also, we’d have to 
change our code each time the list’s length changed. A for loop avoids both 
of these issues by letting Python manage these issues internally.
Let’s use a for loop to print out each name in a list of magicians."""


magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)


# The output of the above code
# alice 
# david 
# carolina

# Above code first we defininglist. 
# for magician in magicians:
"""This line tells Python to retrieve the first value from the list magicians
and store it in the variable magician. This first value is 'alice'. Python then 
reads the next line:"""
#  print(magician)
# Then it print david and carolina on the screen
"""Because no more values are in the list, Python moves on to the 
next line in the program. In this case nothing comes after the for loop, so 
the program simply ends."""

"""Also keep in mind when writing your own for loops that you can choose 
any name you want for the temporary variable that holds each value in the 
list. However, it’s helpful to choose a meaningful name that represents a 
single item from the list. For example, here’s a good way to start a for loop 
for a list of cats, a list of dogs, and a general list of items:"""
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

# Doing More Work Within a for Loop
"""You can do just about anything with each item in a for loop. Let’s build on 
the previous example by printing a message to each magician, telling them 
that they performed a great trick:"""

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")

# The output of the above code:
# Alice, that was a great trick! 
# David, that was a great trick! 
# Carolina, that was a great trick!

"""You can also write as many lines of code as you like in the for loop. 
Every indented line following the line for magician in magicians is cosidered inside the loop, and each indented line is executed once for each 
56 Chapter 4
value in the list. Therefore, you can do as much work as you like with 
each value in the list."""
"""Let’s add a second line to our message, telling each magician that we’re 
looking forward to their next trick:"""

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# The output of the above code:
# Alice, that was a great trick! 
# I can't wait to see your next trick, Alice. 

# David, that was a great trick! 
# I can't wait to see your next trick, David. 

# Carolina, that was a great trick! 
# I can't wait to see your next trick, Carolina.


# Doing Something After a for Loop
"""Any lines of code after the for loop that are not indented are executed 
once without repetition."""

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
 
print("Thank you, everyone. That was a great magic show!")

# The output of the above code:
# Alice, that was a great trick! 
# I can't wait to see your next trick, Alice. 

# David, that was a great trick! 
# I can't wait to see your next trick, David. 

# Carolina, that was a great trick! 
# I can't wait to see your next trick, Carolina.

# Thank you, everyone. That was a great magic show!


# Avoiding Indentation Errors
# Forgetting to Indent
"""Always indent the line after the for statement in a loop. If you forget, Python 
will remind you:"""

# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians: 
# print(magician)

# The above code give the indentation error
"""You can usually resolve this kind of indentation error by indenting the 
line or lines immediately after the for statement."""


# Indenting Unnecessarily
"""If you accidentally indent a line that doesn’t need to be indented, Python 
informs you about the unexpected indent:"""

# message = "Hello Python world!"
#    print(message)

"""We don’t need to indent the print statement , because it doesn’t 
belong to the line above it; hence, Python reports that error"""


# Indenting Unnecessarily After the Loop
"""If you accidentally indent code that should run after a loop has finished, that 
code will be repeated once for each item in the list. Sometimes this prompts 
Python to report an error, but often you’ll receive a simple logical error."""

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
 
    print("Thank you everyone, that was a great magic show!")

# The output of the above code:
# Alice, that was a great trick! 
# I can't wait to see your next trick, Alice. 

# Thank you everyone, that was a great magic show! 
# David, that was a great trick! 
# I can't wait to see your next trick, David. 

# Thank you everyone, that was a great magic show! 
# Carolina, that was a great trick! 
# I can't wait to see your next trick, Carolina. 

#  Thank you everyone, that was a great magic show!


# Forgetting the Colon
"""The colon at the end of a for statement tells Python to interpret the next 
line as the start of a loop. """

# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians
#     print(magician)

"""If you accidentally forget the colon, as shown , you’ll get a syntax 
error because Python doesn’t know what you’re trying to do. Although 
this is an easy error to fix, it’s not always an easy error to find."""


# Making Numerical Lists
"""Many reasons exist to store a set of numbers. For example, you’ll need to 
keep track of the positions of each character in a game, and you might want 
to keep track of a player’s high scores as well. In data visualizations, you’ll 
almost always work with sets of numbers, such as temperatures, distances, 
population sizes, or latitude and longitude values, among other types of 
numerical sets."""


# Using the range() Function
"""Python’s range() function makes it easy to generate a series of numbers. 
For example, you can use the range() function to print a series of numbers 
like this:"""

for value in range(1,5):
    print(value)

"""Although this code looks like it should print the numbers from 1 to 5, it 
doesn’t print the number 5:"""
# The output of the above code:
# 1
# 2
# 3
# 4

"""In the above example, range() prints only the numbers 1 through 4. The range() function causes Python to start counting at the first 
value you give it, and it stops when it reaches the second value you provide. 
Because it stops at that second value, the output never contains the end 
value, which would have been 5 in this case.
To print the numbers from 1 to 5, you would use range(1,6):"""

for value in range(1,6):
    print(value)
# This time the output starts at 1 and ends at 5:
# The output of the above code:
# 1
# 2
# 3
# 4
# 5


# Using range() to Make a List of Numbers
"""If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a 
call to the range() function, the output will be a list of numbers."""

numbers = list(range(1,6))
print(numbers)

# And this is the result:
# [1, 2, 3, 4, 5]

"""We can also use the range() function to tell Python to skip numbers 
in a given range. For example, here’s how we would list the even numbers 
between 1 and 10:"""

even_numbers = list(range(2,11,2)) 
print(even_numbers)

# And this is the result:
# [2, 4, 6, 8, 10]

"""You can create almost any set of numbers you want to using the range()
function. For example, consider how you might make a list of the first 10 
square numbers (that is, the square of each integer from 1 through 10)"""

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# And this is the result:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""To write this code more concisely, omit the temporary variable square
and append each new value directly to the list:"""

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)


# Simple Statistics with a List of Numbers
"""A few Python functions are specific to lists of numbers. For example, you 
can easily find the minimum, maximum, and sum of a list of numbers:"""

# >>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# >>> min(digits)
# 0
# >>> max(digits)
# 9
# >>> sum(digits)
# 45


# List Comprehensions
"""The approach described earlier for generating the list squares consisted of 
using three or four lines of code. A list comprehension allows you to generate 
this same list in just one line of code. A list comprehension combines the 
for loop and the creation of new elements into one line, and automatically 
appends each new element."""

squares = [value**2 for value in range(1,11)]
print(squares)

# And this is the result:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Working with Part of a List
# Slicing a List
"""To make a slice, you specify the index of the first and last elements you 
want to work with. As with the range() function, Python stops one item 
before the second index you specify. To output the first three elements 
in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2."""

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])

# And this is the result:
# ['charles', 'martina', 'michael']


"""You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list, you would start the slice at index 1 and 
end at index 4:"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# This time the slice starts with 'martina' and ends with 'florence':
# ['martina', 'michael', 'florence'] 

"""If you omit the first index in a slice, Python automatically starts your 
slice at the beginning of the list:"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# Without a starting index, Python starts at the beginning of the list:
# ['charles', 'martina', 'michael', 'florence']

"""A similar syntax works if you want a slice that includes the end of a list. 
For example, if you want all items from the third item through the last item, 
you can start with index 2 and omit the second index:"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# Python returns all items from the third item through the end of the list:
# ['michael', 'florence', 'eli']


# Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Here are the first three players on my team: 
# Charles 
# Martina 
# Michael


# Copying a List
"""To copy a list, you can make a slice that includes the entire original list 
by omitting the first index and the second index ([:]). This tells Python to 
make a slice that starts at the first item and ends with the last item, producing a copy of the entire list."""

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# The output of the above code is:
# My favorite foods are: 
# ['pizza', 'falafel', 'carrot cake'] 

# My friend's favorite foods are: 
# ['pizza', 'falafel', 'carrot cake'] 

"""To prove that we actually have two separate lists, we’ll add a new food 
to each list and show that each list keeps track of the appropriate person’s 
favorite foods:"""

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# The output of the above code is:
# My favorite foods are: 
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

# My friend's favorite foods are: 
# ['pizza', 'falafel', 'carrot cake', 'ice cream']


# what happens when you try to copy a list without using a slice:

my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

"""Instead of storing a copy of my_foods in friend_foods at u, we set 
friend_foods equal to my_foods. This syntax actually tells Python to connect the new variable friend_foods to the list that is already contained in 
my_foods, so now both variables point to the same list. As a result, when we 
add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice 
cream' will appear in both lists, even though it appears to be added only to 
friend_foods."""

# The output shows that both lists are the same now, which is not what we wanted:

# My favorite foods are: 
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# My friend's favorite foods are: 
# ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']


# Tuples
""" However, sometimes you’ll want to create a list of items that cannot 
change. Tuples allow you to do just that. Python refers to values that cannot 
change as immutable, and an immutable list is called a tuple."""

# Defining a Tuple
"""A tuple looks just like a list except you use parentheses instead of square 
brackets. Once you define a tuple, you can access individual elements by 
using each item’s index, just as you would for a list."""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# And this is the result:
# 200
# 50

# Let’s see what happens if we try to change one of the items in the tuple dimensions:
dimensions = (200, 50)
dimensions[0] = 250

"""The code at u tries to change the value of the first dimension, but 
Python returns a type error. Basically, because we’re trying to alter a tuple, 
which can’t be done to that type of object, Python tells us we can’t assign a 
new value to an item in a tuple:"""


# Writing over a Tuple
"""Although you can’t modify a tuple, you can assign a new value to a variable 
that holds a tuple. So if we wanted to change our dimensions, we could 
redefine the entire tuple:"""

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
 
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    

# Original dimensions: 
# 200 
# 50 
# Modified dimensions: 
# 400 
# 100