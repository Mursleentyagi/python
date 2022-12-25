"""Functions are named blocks of code 
that are designed to do one specific job. 
When you want to perform a particular task 
that you’ve defined in a function, you call the name 
of the function responsible for it. If you need to 
perform that task multiple times throughout your program, you don’t 
need to type all the code for the same task again and again; you just call 
the function dedicated to handling that task, and the call tells Python to 
run the code inside the function. You’ll find that using functions makes 
your programs easier to write, read, test, and fix."""

# Defining a Function
# Here’s a simple function named greet_user() that prints a greeting:
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
 
greet_user()

"""This example shows the simplest structure of a function. The line at line 1
uses the keyword def to inform Python that you’re defining a function. This 
is the function definition, which tells Python the name of the function and, if 
applicable, what kind of information the function needs to do its job. The 
parentheses hold that information. In this case, the name of the function 
is greet_user(), and it needs no information to do its job, so its parentheses 
are empty. (Even so, the parentheses are required.) Finally, the definition 
ends in a colon."""
"""Any indented lines that follow def greet_user(): make up the body of 
the function. The text at 2 is a comment called a docstring, which describes 
what the function does. Docstrings are enclosed in triple quotes, which 
Python looks for when it generates documentation for the functions in your 
programs. """
"""The line print("Hello!") 3 is the only line of actual code in the body 
of this function, so greet_user() has just one job: print("Hello!").
When you want to use this function, you call it. A function call tells 
Python to execute the code in the function. To call a function, you write 
the name of the function, followed by any necessary information in parentheses, as shown at 4. Because no information is needed here, calling our 
function is as simple as entering greet_user(). As expected, it prints Hello!:"""
# Hello!


# Passing Information to a Function
"""Modified slightly, the function greet_user() can not only tell the user Hello!
but also greet them by name. For the function to do this, you enter username
in the parentheses of the function’s definition at def greet_user(). By adding username here you allow the function to accept any value of username you 
specify. The function now expects you to provide a value for username each 
time you call it. When you call greet_user(), you can pass it a name, such as 
'Kadir Tyagi', inside the parentheses:"""
def greet_user(username):
 """Display a simple greeting."""
 print("Hello, " + username.title() + "!")
 
greet_user('Kadir Tyagi')

"""Entering greet_user('Kadir Tyagi') calls greet_user() and gives the function the 
information it needs to execute the print statement. The function accepts 
the name you passed it and displays the greeting for that name:"""
# Hello, Kadir Tyagi!

# Arguments and Parameters
"""The variable username in the definition of greet_user() is an example of a 
parameter, a piece of information the function needs to do its job. The value 
'Kadir Tyagi' in greet_user('Kadir Tyagi') is an example of an argument. An argument 
is a piece of information that is passed from a function call to a function. 
When we call the function, we place the value we want the function to work 
with in parentheses. In this case the argument 'Kadir Tyagi' was passed to the 
function greet_user(), and the value was stored in the parameter username."""


# Passing Arguments
"""Because a function definition can have multiple parameters, a function call 
may need multiple arguments. You can pass arguments to your functions 
in a number of ways."""

# Positional Arguments
"""When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to 
do this is based on the order of the arguments provided. Values matched 
up this way are called positional arguments.
To see how this works, consider a function that displays information 
about pets. The function tells us what kind of animal each pet is and the 
pet’s name, as shown here:"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet('hamster', 'harry')

# I have a hamster. 
# My hamster's name is Harry

# Multiple Function Calls
# You can call a function as many times as needed. 
# describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


# Order Matters in Positional Arguments
"""You can get unexpected results if you mix up the order of the arguments in 
a function call when using positional arguments:"""
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet('harry', 'hamster')
"""In this function call we list the name first and the type of animal second. 
Because the argument 'harry' is listed first this time, that value is stored in 
the parameter animal_type. Likewise, 'hamster' is stored in pet_name. Now we 
have a “harry” named “Hamster”:"""

# I have a harry. 
# My harry's name is Hamster.
"""If you get funny results like this, check to make sure the order of the 
arguments in your function call matches the order of the parameters in the 
function’s definition."""

# Keyword Arguments
"""A keyword argument is a name-value pair that you pass to a function. You 
directly associate the name and the value within the argument, so when you 
pass the argument to the function, there’s no confusion (you won’t end up 
with a harry named Hamster). Keyword arguments free you from having 
to worry about correctly ordering your arguments in the function call, and 
they clarify the role of each value in the function call"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
"""The order of keyword arguments doesn’t matter because Python 
knows where each value should go. The following two function calls are 
equivalent:"""
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
"""When writing a function, you can define a default value for each parameter. 
If an argument for a parameter is provided in the function call, Python uses 
the argument value. If not, it uses the parameter’s default value."""

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
   
# The output of the above code:
# I have a dog. 
# My dog's name is Willie.


# Return Values
"""A function doesn’t always have to display its output directly. Instead, it can 
process some data and then return a value or set of values. The value the 
function returns is called a return value. The return statement takes a value 
from inside a function and sends it back to the line that called the function."""

# Returning a Simple Value
"""Let’s look at a function that takes a first and last name, and returns a neatly 
formatted full name:"""
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
student = get_formatted_name('Mursleen', 'Tyagi')
print(student)

"""The definition of get_formatted_name() takes as parameters a first and last 
name 1. The function combines these two names, adds a space between 
them, and stores the result in full_name 3. The value of full_name is converted to title case, and then returned to the calling line at 4.
When you call a function that returns a value, you need to provide a 
variable where the return value can be stored. In this case, the returned 
value is stored in the variable musician at 5."""
# The output of the above code
# Mursleen Tyagi


# Making an Argument Optional
"""Sometimes it makes sense to make an argument optional so that people 
using the function can choose to provide extra information only if they 
want to. You can use default values to make an argument optional.
For example, say we want to expand get_formatted_name() to handle 
middle names as well. A first attempt to include middle names might look 
like this:"""
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
 
student = get_formatted_name('Ravi', 'Prakash', 'Mishra')
print(student)

"""This function works when given a first, middle, and last name. The 
function takes in all three parts of a name and then builds a string out of 
them. The function adds spaces where appropriate and converts the full 
name to title case:"""
# Ravi Praksh Mishra

"""But middle names aren’t always needed, and this function as written 
would not work if you tried to call it with only a first name and a last name. 
To make the middle name optional, we can give the middle_name argument 
an empty default value and ignore the argument unless the user provides a 
value. To make get_formatted_name() work without a middle name, we set the 
default value of middle_name to an empty string and move it to the end of the 
list of parameters:"""
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
       full_name = first_name + ' ' + last_name
    return full_name.title()

student = get_formatted_name('vishal', 'houdhary')
print(student)
student = get_formatted_name('ravi', 'rakash', 'ishra')
print(student)

# Returning a Dictionary
"""A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries. For example, the following function takes in parts of a name and returns a dictionary representing 
a person:"""
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
student = build_person('fareed', 'abbasi')
print(student)

# {'first': 'jimi', 'last': 'hendrix'} 



# Using a Function with a while Loop
"""You can use functions with all the Python structures you’ve learned about 
so far. For example, let’s use the get_formatted_name() function with a while
loop to greet users more formally. Here’s a first attempt at greeting people 
using their first and last names:"""
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop!
while True:
   print("\nPlease tell me your name:")
   f_name = input("First name: ")
   l_name = input("Last name: ")
   
formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")

"""For this example, we use a simple version of get_formatted_name() that 
doesn’t involve middle names. The while loop asks the user to enter their 
name, and we prompt for their first and last name separately u.
But there’s one problem with this while loop: We haven’t defined a quit 
condition. Where do you put a quit condition when you ask for a series of 
inputs? We want the user to be able to quit as easily as possible, so each 
prompt should offer a way to quit. The break statement offers a straightforward way to exit the loop at either prompt:"""
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
   print("\nPlease tell me your name:")
   print("(enter 'q' at any time to quit)")
 
   f_name = input("First name: ")
   if f_name == 'q':
      break
 
   l_name = input("Last name: ")
   if l_name == 'q':
      break

formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")

# Passing a List
def greet_users(names):
   """Print a simple greeting to each user in the list."""
   for name in names:
       msg = "Hello, " + name.title() + "!"
       print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# The output of the above code:
# Hello, Hannah! 
# Hello, Ty! 
# Hello, Margot!


# Modifying a List in a Function
"""When you pass a list to a function, the function can modify the list. Any 
changes made to the list inside the function’s body are permanent, allowing 
you to work efficiently even when you’re dealing with large amounts of data.
Consider a company that creates 3D printed models of designs that """
"""users submit. Designs that need to be printed are stored in a list, and after 
being printed they’re moved to a separate list. The following code does this 
without using functions:"""

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
 
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
 
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# The output of the above code :
# Printing model: dodecahedron 
# Printing model: robot pendant 
# Printing model: iphone case 
# The following models have been printed: 
# dodecahedron 
# robot pendant 
# iphone case

"""We can reorganize this code by writing two functions, each of which 
does one specific job. Most of the code won’t change; we’re just making it 
more efficient. The first function will handle printing the designs, and the 
second will summarize the prints that have been made:"""
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
       current_design = unprinted_designs.pop()
 
       # Simulate creating a 3D print from the design.
       print("Printing model: " + current_design)
       completed_models.append(current_design)
 
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
 
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Passing an Arbitrary Number of Arguments
"""Sometimes you won’t know ahead of time how many arguments a function 
needs to accept. Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement. 
For example, consider a function that builds a pizza. It needs to accept a 
number of toppings, but you can’t know ahead of time how many toppings 
a person will want. The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling 
line provides:"""
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
 
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

"""The asterisk in the parameter name *toppings tells Python to make an 
empty tuple called toppings and pack whatever values it receives into this 
tuple. The print statement in the function body produces output showing 
that Python can handle a function call with one value and a call with three 
values. It treats the different calls similarly. Note that Python packs the 
arguments into a tuple, even if the function receives only one value:"""
# ('pepperoni',) 
# ('mushrooms', 'green peppers', 'extra cheese')