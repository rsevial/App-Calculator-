# Programmed by: Rebekah Joy E. Sevial
# Assignment 4
# App Calcuator

# Print Simple Calculator
print("\033[0;33m===========================================")
print("\033[0;33m             " + "\033[0;33m\033[1mSIMPLE CALCULATOR\033[0m" + "\033[0;33m             ")
print("\033[0;33m===========================================" + "\n")

# Use while loop 
# Display the main menu of the calculator using user-defined functions
while True:
    def dispmenu():
        print("\n\033[36mWhat operation do you like to do?\n")
        print("\033[36m1. Addition")
        print("\033[36m2. Subtraction")
        print("\033[36m3. Multiplication")
        print("\033[36m4. Division")

        # Asks the user to decide which operation to use assigned from numbers 1 to 4
        # Use the try and except function to check for the errors
        try:
            user_choice = int(input("\n"+"\033[36mEnter your choice from 1 to 4: \033[33m"))
            # Add a condition when the user inputted an invalid number
            if user_choice <= 4: 

                # Ask the user for the two integers then assign them into variables
                try:
                    num1 = float(input("\033[36mEnter your first number: \033[33m"))
                    num2 = float(input("\033[36mEnter your second number: \033[33m"))  
                    # Call the add function if the user choose 1
                    if user_choice == 1:
                        sum = add(num1, num2)
                        print("\n", "\033[33mResult:", sum, "\n")
                    # Call the subtract function if the user choose 2
                    elif user_choice == 2:
                        difference = subtract(num1, num2)
                        print("\n", "\033[33mResult:", difference, "\n")
                    # Call the multiply function if the user choose 3
                    elif user_choice == 3:
                        product = multiply(num1, num2)
                        print("\n", "\033[33mResult:", product, "\n")
                    # Call the divide function if the user choose 4 
                    elif user_choice == 4:
                        quotient = divide(num1, num2)
                        print("\n", "\033[33mResult:", quotient, "\n")
                    
                # Use the except ValueError and TypeError if the user entered the wrong values
                except (ValueError, TypeError):
                    print("\n\033[31mError! You enter an invalid value! Please try again.\n")    
            # Use an else statement if the user entered an integer greater than 4
            else:
                print("\n\033[31mInvalid Integer!")
        # Use the except ValueError and TypeError if the user entered the wrong values
        except (ValueError, TypeError):
            print("\n\033[31mError! You enter an invalid value! Please try again.")

    # Define a function which is the addition, which will add the two inputted numbers
    def add(num1,num2):
        sum = num1 + num2
        return sum
    
    # Define a function which is the subtraction, which will subtract the two inputted numbers
    def subtract(num1,num2):
        difference = num1 - num2
        return difference
    
    # Define a function which is the multiplication, which will multiply the two inputted numbers
    def multiply(num1,num2):
        product = num1 * num2
        return product
    
    # Define a function which is the divison, which will divide the two inputted numbers
    def divide(num1,num2):
        try:
            quotient = num1 / num2
            return quotient
        # Use the except ZeroDivisionError if the user divided by zero
        except ZeroDivisionError:
            print("\n\033[31mError! You are dividing by zero.")

    # Call for the function display menu
    dispmenu()

    # While loop for the program to continue unless the user stops it
    while True:
        # Ask the user if he/she wants to continue
        ask_again = input("\n\033[35mDo you still want to continue? (yes/no): ")
        # Continue the program
        if ask_again.casefold() == "yes":
            dispmenu()
            continue
        # Stop the program
        elif ask_again.casefold() == "no":
            print("\033[36mThank you!")
            break
        # If what the user inputted is invalid then he/she will be asked to try again
        else:
            print("\n","\033[31mInvalid input!")
            continue