# in python exception handling allows a programmer to deal with runtime errors or exceptions.
# an exception is an event that occurs during the execution of a program disrupting the normal flow of the programs execution.
# pythons try and except blocks are used to handle exceptions. the try block contains the code that may raise an exception, while the except block contains the code that will be executed if an exception occurs.

try:
    print(x)
except NameError:
    print("Variable x is not defined")  

else:
    print("Everything went wrong")

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")