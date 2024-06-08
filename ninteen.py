'''handle exceptions using a combination of try, except, and finally blocks. '''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Execution of finally block is complete.")

 
