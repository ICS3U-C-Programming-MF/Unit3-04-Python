#!usr/bin/env python3
# Made by Maximiliano Fairman
# Created on oct 20th 2025
# This program is a number checker
# that checks if the input is positive or negative
# or zero.

# Ask the user to enter an integer
user_input = float(input("Enter an integer: "))

# Check if the number is positive
if user_input > 0:
    print("The number is positive.")

# Check if the number is negative
elif user_input < 0:
    print("The number is negative.")

# If the number is zero
else:
    print("The number is zero.")

# Print done once program is finished
print("\nDone.")
