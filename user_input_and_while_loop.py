"""Most programs are written to solve an end 
user’s problem. To do so, you usually need 
to get some information from the user. For a 
simple example, let’s say someone wants to find 
out whether they’re old enough to vote. If you write a 
program to answer this question, you need to know the user’s age before 
you can provide an answer. The program will need to ask the user to enter, 
or input, their age; once the program has this input, it can compare it to the 
voting age to determine if the user is old enough and then report the result."""

# How the input() Function Works
"""The input() function pauses your program and waits for the user to enter 
some text. Once Python receives the user’s input, it stores it in a variable to 
make it convenient for you to work with."""

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# The output of the above code:
# Tell me something, and I will repeat it back to you: Hello everyone!
# Hello everyone!

# Writing Clear Prompts
"""Each time you use the input() function, you should include a clear, easy-tofollow prompt that tells the user exactly what kind of information you’re 
looking for. Any statement that tells the user what to enter should work. For 
example:"""
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# Let's suppose you will  enter Mursleen:
# Then the output of the above code
# Please enter your name: Mursleen
# Hello, Mursleen!

# Using int() to Accept Numerical Input
"""When you use the input() function, Python interprets everything the user 
enters as a string. Consider the following interpreter session, which asks for 
the user’s age:"""

# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age
# '21' 

"""The user enters the number 21, but when we ask Python for the value of 
age, it returns '21', the string representation of the numerical value entered. 
If all you want to do is print the input, this works well. But 
if you try to use the input as a number, you’ll get an error:"""

"""We can resolve this issue by using the int() function, which tells 
Python to treat the input as a numerical value. The int() function converts a string representation of a number to a numerical representation, 
as shown here:"""

# >>> age = input("How old are you? ")
# How old are you? 21
# u >>> age = int(age)
# >>> age >= 18
# True

# Another example
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
   print("\nYou're tall enough to ride!")
else:
   print("\nYou'll be able to ride when you're a little older.")

# Let's suppose you enter 70 
# How tall are you, in inches? 70
# You're tall enough to ride!


# The Modulo Operator
"""A useful tool for working with numerical information is the modulo operator (%), 
which divides one number by another number and returns the remainder:"""

# >>> 4 % 3 
# 1 
# >>> 5 % 3 
# 2 
# >>> 6 % 3 
# 0 
# >>> 7 % 3 
# 1 

"""When one number is divisible by another number, the remainder is 0, 
so the modulo operator always returns 0. You can use this fact to determine 
if a number is even or odd:"""
"""Even numbers are always divisible by two, so if the modulo of a number 
and two is zero (here, if number % 2 == 0) the number is even. Otherwise, 
it’s odd."""

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
   print("\nThe number " + str(number) + " is even.")
else:
   print("\nThe number " + str(number) + " is odd.")

# Enter a number, and I'll tell you if it's even or odd: 42
# The number 42 is even.

# Introducing while Loops
"""The for loop takes a collection of items and executes a block of code once 
for each item in the collection. In contrast, the while loop runs as long as, 
or while, a certain condition is true. """

# The while Loop in Action
"""You can use a while loop to count up through a series of numbers. For 
example, the following while loop counts from 1 to 5:"""
current_number = 1
while current_number <= 5:
      print(current_number)
      current_number += 1

"""In the first line, we start counting from 1 by setting the value of 
current_number to 1. The while loop is then set to keep running as long 
as the value of current_number is less than or equal to 5. The code inside 
the loop prints the value of current_number and then adds 1 to that value 
with current_number += 1. (The += operator is shorthand for current_number = 
current_number + 1.) 
Python repeats the loop as long as the condition current_number <= 5 
is true. Because 1 is less than 5, Python prints 1 and then adds 1, making the current number 2. Because 2 is less than 5, Python prints 2
and adds 1 again, making the current number 3, and so on. Once the 
value of current_number is greater than 5, the loop stops running and the 
program ends:"""
# The output of the above code:
# 1
# 2
# 3
# 4
# 5

# Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello again.
# Hello again. 

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit
# quit

"""This program works well, except that it prints the word 'quit' as if it 
were an actual message. A simple if test fixes this:"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
 
    if message != 'quit':
        print(message)

"""Now the program makes a quick check before displaying the message 
and only prints the message if it does not match the quit value:"""
# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello everyone!
# Hello everyone!

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. Hello again.
# Hello again. 

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit

# Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
 
active = True
while active:
   message = input(prompt)
 
   if message == 'quit':
       active = False
   else:
       print(message)


# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
 
    if city == 'quit':
      break
    else:
       print("I'd love to go to " + city.title() + "!")

"""A loop that starts with while True  will run forever unless it reaches a 
break statement. The loop in this program continues asking the user to enter 
the names of cities they’ve been to until they enter 'quit'. When they enter 
'quit', the break statement runs, causing Python to exit the loop:"""

# Using continue in a Loop
"""Rather than breaking out of a loop entirely without executing the rest of its 
code, you can use the continue statement to return to the beginning of the 
loop based on the result of a conditional test. For example, consider a loop 
that counts from 1 to 10 but prints only the odd numbers in that range:"""
current_number = 0
while current_number < 10:
   current_number += 1
   if current_number % 2 == 0:
       continue
 
   print(current_number)

"""First we set current_number to 0. Because it’s less than 10, Python 
enters the while loop. Once inside the loop, we increment the count by 1 
, so current_number is 1. The if statement then checks the modulo of 
current_number and 2. If the modulo is 0 (which means current_number is 
divisible by 2), the continue statement tells Python to ignore the rest of 
the loop and return to the beginning. If the current number is not divisible by 2, the rest of the loop is executed and Python prints the current 
number:"""
# 1 
# 3 
# 5 
# 7 
# 9

"""if you accidentally omit the line x += 1 (as shown next), the loop 
will run forever:"""
# This loop runs forever!
# x = 1
# while x <= 5:
#    print(x)