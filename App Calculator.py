# Programmed by: Rebekah Joy E. Sevial
# Assignment 4
# App Calcuator

# Print Simple Calculator
print("\033[0;33;47m===========================================")
print("\033[0;33;47m             " + "\033[0;33;47m\033[1mSIMPLE CALCULATOR\033[0m" + "\033[0;33;47m             ")
print("\033[0;33;47m===========================================" + "\n")

# Use while loop 
# Display the main menu of the calculator using user-defined functions
while True:
    def dispmenu():
        print("What operation do you like to do?\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        # Asks the user to decide which operation to use assigned from numbers 1 to 4
        # Use the try and except function to check for the errors
        try:
            user_choice = int(input("\n"+"Enter your choice from 1 to 4: "))
            # Add a condition when the user inputted an invalid number
            if user_choice <= 4: 

                # Ask the user for the two integers then assign them into variables
                try:
                    num1 = float(input("Enter your first number: "))
                    num2 = float(input("Enter your second number: "))  
                    # Call the add function if the user choose 1
                    if user_choice == 1:
                        sum = add(num1, num2)
                        print("\nResult:", sum)
                    # Call the subtract function if the user choose 2
                    elif user_choice == 2:
                        difference = subtract(num1, num2)
                        print("\nResult:", difference)
                    # Call the multiply function if the user choose 3
                    elif user_choice == 3:
                        product = multiply(num1, num2)
                        print("\nResult:", product)
                    # Call the divide function if the user choose 4 
                    elif user_choice == 4:
                        quotient = divide(num1, num2)
                        print("\nResult:", quotient)
                    
                # Use the except ValueError and TypeError if the user entered the wrong values
                except (ValueError, TypeError):
                    print("Error! You enter an invalid value! Please try again.\n")    
            # Use an else statement if the user entered an integer greater than 4
            else:
                print("Invalid Integer!")
        # Use the except ValueError and TypeError if the user entered the wrong values
        except (ValueError, TypeError):
            print("Error! You enter an invalid value! Please try again.")

# Define a function which is the sum, which will add the two inputted numbers
# Define a function which is the subtraction, which will subtract the two inputted numbers
# Define a function which is the multiplication, which will multiply the two inputted numbers
# Define a function which is the divison, which will divide the two inputted numbers
# Use the except ZeroDivisionError if the user divided by zero
# Call for the function display menu

# While loop for the program to continue unless the user stops it
# Ask the user if he/she wants to continue
# Continue the program
# Stop the program
# If what the user inputted is invalid then he/she will be asked to try again