"""Programming often involves examining 
a set of conditions and deciding which 
action to take based on those conditions. 
Python’s if statement allows you to examine the 
current state of a program and respond appropriately 
to that state."""

# A Simple Example
"""The following short example shows how if tests let you respond to special 
situations correctly. Imagine you have a list of cars and you want to print 
out the name of each car. Car names are proper names, so the names of 
most cars should be printed in title case. However, the value 'bmw' should 
be printed in all uppercase. The following code loops through a list of car 
names and looks for the value 'bmw'. Whenever the value is 'bmw', it’s printed 
in uppercase instead of title case:"""

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
       print(car.upper())
    else:
       print(car.title())

# The output of the above code:
# Audi 
# BMW 
# Subaru 
# Toyota


# Conditional Tests
"""At the heart of every if statement is an expression that can be evaluated as 
True or False and is called a conditional test. Python uses the values True and 
False to decide whether the code in an if statement should be executed. If a 
conditional test evaluates to True, Python executes the code following the if
statement. If the test evaluates to False, Python ignores the code following 
the if statement."""

# Checking for Equality
"""Most conditional tests compare the current value of a variable to a specific 
value of interest. The simplest conditional test checks whether the value of a 
variable is equal to the value of interest:"""

# >>> car = 'bmw'
# >>> car == 'bmw'
# True 

# When the value of car is anything other than 'bmw', this test returns False:

# >>> car = 'audi'
# >>> car == 'bmw'
# False


# Ignoring Case When Checking for Equality
"""Testing for equality is case sensitive in Python. For example, two values with 
different capitalization are not considered equal:"""

# >>> car = 'Audi'
# >>> car == 'audi'
# False

"""If case matters, this behavior is advantageous. But if case doesn’t matter 
and instead you just want to test the value of a variable, you can convert the 
variable’s value to lowercase before doing the comparison:"""

# >>> car = 'Audi'
# >>> car.lower() == 'audi'
# True

# Checking for Inequality
"""When you want to determine whether two values are not equal, you can 
combine an exclamation point and an equal sign (!=). The exclamation 
point represents not, as it does in many programming languages.
Let’s use another if statement to examine how to use the inequality 
operator. We’ll store a requested pizza topping in a variable and then print 
a message if the person did not order anchovies:"""

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
   print("Hold the anchovies!")

"""The line 2 compares the value of requested_topping to the value 
'anchovies'. If these two values do not match, Python returns True and executes the code following the if statement. If the two values match, Python 
returns False and does not run the code following the if statement."""

"""Because the value of requested_topping is not 'anchovies', the print statement is executed:"""
# Hold the anchovies!


# Numerical Comparisons
"""Testing numerical values is pretty straightforward. For example, the following code checks whether a person is 18 years old:"""

# >>> age = 18
# >>> age == 18
# True

"""You can also test to see if two numbers are not equal. For example, the 
following code prints a message if the given answer is not correct:"""
answer = 17
if answer != 42:
   print("That is not the correct answer. Please try again!")
"""The conditional test at 2 line passes, because the value of answer (17) is not 
equal to 42. Because the test passes, the indented code block is executed:
That is not the correct answer. Please try again!
You can include various mathematical comparisons in your conditional 
statements as well, such as less than, less than or equal to, greater than, and 
greater than or equal to:"""

# >>> age = 19
# >>> age < 21
# True
# >>> age <= 21
# True
# >>> age > 21
# False
# >>> age >= 21
# False

# Checking Multiple Conditions
# >>> age_0 = 22 
# >>> age_1 = 18 
# >>> age_0 >= 21 and age_1 >= 21 
# False 
# >>> age_1 = 22 
# >>> age_0 >= 21 and age_1 >= 21 
# True 


# Checking Whether a Value Is in a List
"""Sometimes it’s important to check whether a list contains a certain value 
before taking an action. For example, you might want to check whether a 
new username already exists in a list of current usernames before completing someone’s registration on a website. In a mapping project, you might 
want to check whether a submitted location already exists in a list of known 
locations."""
"""To find out whether a particular value is already in a list, use the keyword in. Let’s consider some code you might write for a pizzeria. We’ll 
make a list of toppings a customer has requested for a pizza and then 
check whether certain toppings are in the list."""

# >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
# >>> 'mushrooms' in requested_toppings
# True
# >>> 'pepperoni' in requested_toppings
# False


# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# And the output of this:
# Marie, you can post a response if you wish.


# Boolean Expressions
"""As you learn more about programming, you’ll hear the term Boolean 
expression at some point. A Boolean expression is just another name for a 
conditional test. A Boolean value is either True or False, just like the value 
of a conditional expression after it has been evaluated.
Boolean values are often used to keep track of certain conditions, such 
as whether a game is running or whether a user can edit certain content on 
a website:"""
# game_active = True
# can_edit = False


# if Statements
# Simple if Statements
# The simplest kind of if statement has one test and one action:
# if conditional_test:
#    do something

"""You can put any conditional test in the first line and just about any 
action in the indented block following the test. If the conditional test 
evaluates to True, Python executes the code following the if statement. 
If the test evaluates to False, Python ignores the code following the if
statement."""
"""Let’s say we have a variable representing a person’s age, and we want to 
know if that person is old enough to vote. The following code tests whether 
the person can vote:"""

age = 19
if age >= 18:
   print("You are old enough to vote!")

"""At line 2 Python checks to see whether the value in age is greater than or 
equal to 18. It is, so Python executes the indented print statement at line 3:"""

# The output of the above code:
# You are old enough to vote!

"""Indentation plays the same role in if statements as it did in for loops. 
All indented lines after an if statement will be executed if the test passes, 
and the entire block of indented lines will be ignored if the test does 
not pass."""
"""You can have as many lines of code as you want in the block following the if statement. Let’s add another line of output if the person is old 
enough to vote, asking if the individual has registered to vote yet:"""

age = 19
if age >= 18:
   print("You are old enough to vote!")
   print("Have you registered to vote yet?")

"""The conditional test passes, and both print statements are indented, so 
both lines are printed:"""

# The output of the above code:
# You are old enough to vote!
# Have you registered to vote yet?


# if-else Statements
"""Often, you’ll want to take one action when a conditional test passes and a different action in all other cases. Python’s if-else syntax makes this possible. 
An if-else block is similar to a simple if statement, but the else statement 
allows you to define an action or set of actions that are executed when the 
conditional test fails."""

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

"""Because age is less than 18 this time, the conditional test fails and 
the code in the else block is executed:"""

# The output of the above code:
# Sorry, you are too young to vote.
# Please register to vote as soon as you turn 18!


# The if-elif-else Chain
"""Often, you’ll need to test more than two possible situations, and to evaluate 
these you can use Python’s if-elif-else syntax. Python executes only one 
block in an if-elif-else chain. It runs each conditional test in order until 
one passes. When a test passes, the code following that test is executed and 
Python skips the rest of the tests."""

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    
# The output of the above code:
# Your admission cost is $5.

"""Rather than printing the admission price within the if-elif-else block, 
it would be more concise to set just the price inside the if-elif-else chain 
and then have a simple print statement that runs after the chain has been 
evaluated:"""

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# Using Multiple elif Blocks
# You can use as many elif blocks in your code as you like
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")


# Omitting the else Block
"""Python does not require an else block at the end of an if-elif chain. Sometimes an else block is useful; sometimes it is clearer to use an additional 
elif statement that catches the specific condition of interest:"""
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")


# Testing Multiple Conditions
"""The if-elif-else chain is powerful, but it’s only appropriate to use when you 
just need one test to pass. As soon as Python finds one test that passes, it 
skips the rest of the tests. This behavior is beneficial, because it’s efficient 
and allows you to test for one specific condition."""
"""However, sometimes it’s important to check all of the conditions of 
interest. In this case, you should use a series of simple if statements with no 
elif or else blocks. This technique makes sense when more than one condition could be True, and you want to act on every condition that is True."""
"""Let’s reconsider the pizzeria example. If someone requests a two-topping 
pizza, you’ll need to be sure to include both toppings on their pizza:"""

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
 
print("\nFinished making your pizza!")
  
"""We start at line 1 with a list containing the requested toppings. The if
statement at 2 checks to see whether the person requested mushrooms 
on their pizza. If so, a message is printed confirming that topping. The 
test for pepperoni at 4 is another simple if statement, not an elif or else
statement, so this test is run regardless of whether the previous test passed 
or not. The code at x checks whether extra cheese was requested regardless of the results from the first two tests. These three independent tests 
are executed every time this program is run."""
"""Because every condition in this example is evaluated, both mushrooms 
and extra cheese are added to the pizza:"""

# The output of the above code:
# Adding mushrooms.
# Adding extra cheese.
# Finished making your pizza!

"""This code would not work properly if we used an if-elif-else block, 
because the code would stop running after only one test passes."""


# Using if Statements with Lists
# Checking for Special Items

"""Let’s continue with the pizzeria example. The pizzeria displays a message 
whenever a topping is added to your pizza, as it’s being made. The code for 
this action can be written very efficiently by making a list of toppings the 
customer has requested and using a loop to announce each topping as it’s 
added to the pizza:"""

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

"""The output is straightforward because this code is just a simple for loop:"""
# Adding mushrooms.
# Adding green peppers.
# Adding extra cheese.

# Finished making your pizza


"""But what if the pizzeria runs out of green peppers? An if statement 
inside the for loop can handle this situation appropriately:"""

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# The output of the above code:
# Adding mushrooms.
# Sorry, we are out of green peppers right now.
# Adding extra cheese.

# Finished making your pizza!


# Checking That a List Is Not Empty
"""We’ve made a simple assumption about every list we’ve worked with so far; 
we’ve assumed that each list has at least one item in it. Soon we’ll let users 
provide the information that’s stored in a list, so we won’t be able to assume 
that a list has any items in it each time a loop is run. In this situation, it’s 
useful to check whether a list is empty before running a for loop."""

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

"""This time we start out with an empty list of requested toppings at line 1. 
Instead of jumping right into a for loop, we do a quick check at 2. When the 
name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False. If requested_toppings
passes the conditional test, we run the same for loop we used in the previous 
example. If the conditional test fails, we print a message asking the customer 
if they really want a plain pizza with no toppings ."""

"""The list is empty in this case, so the output asks if the user really wants 
a plain pizza:"""
# Are you sure you want a plain pizza?


# Using Multiple Lists
"""People will ask for just about anything, especially when it comes to pizza 
toppings. What if a customer actually wants french fries on their pizza? You 
can use lists and if statements to make sure your input makes sense before 
you act on it."""

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
 
print("\nFinished making your pizza!")

"""At line 1 we define a list of available toppings at this pizzeria. Note that 
this could be a tuple if the pizzeria has a stable selection of toppings. At 2, 
we make a list of toppings that a customer has requested. Note the unusual 
request, 'french fries'. At 3 we loop through the list of requested toppings. 
Inside the loop, we first check to see if each requested topping is actually 
in the list of available toppings 4. If it is, we add that topping to the pizza. 
If the requested topping is not in the list of available toppings, the else block 
will run 6. The else block prints a message telling the user which toppings 
are unavailable."""

# The output of the above code:
# Adding mushrooms.
# Sorry, we don't have french fries.
# Adding extra cheese.

# Finished making your pizza!