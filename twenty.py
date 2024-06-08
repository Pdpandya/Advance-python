def onumber():
    try:
        number = int(input("Enter an odd number: "))
        if number % 2 == 0:
            raise ValueError("The number is not odd!")
    except ValueError as ve:
        print("Error:", ve)
    else:
        print("odd number:", number)

onumber()
