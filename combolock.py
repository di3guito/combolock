print("The first step to finding the lock's combination is to find the 'sticky number.' You can do this by pulling the shackle on the lock so that it is slightly less than fully extended while moving the dial counterclockwise to find on which number the dial consistently sticks.  \n \nWhat is that number?")
sticky = int(input())

if (sticky + 5) < 40:
    digit_1 = sticky + 5
else: 
   digit_1 = (sticky + 5) - 40

print ("Your first combo digit is: ", digit_1, " \n \n Now we need to start a different process where we find two 'guess numbers.'") 
remainder_digit_1 = digit_1 % 4

print("The first guess number will be between 0 and 11.  You can find it by starting the lock at zero, pulling up fully on the shackle, and seeing which where the shackle gets stuck between X.5-Y.5. If it is stuck between two whole numbers, move past those numbers and continue to the next place it gets stuck.  Enter your first guess number.")
guess_1 = int(input("Guess 1: "))

"Using the same method, find the second guess number between 0 and 11.  Enter your second guess number."

guess_2 = int(input("Guess 2: "))

digit_3_guesses = [g + i for g in (guess_1, guess_2) for i in range(0, 40, 10)]
valid_digit_3_possibilities = []  # List to store valid possibilities

for digit_3_possibility in digit_3_guesses:
    if digit_3_possibility % 4 == remainder_digit_1: 
        print("Your third digit is one of these two possibilities: ", digit_3_possibility)
        valid_digit_3_possibilities.append(digit_3_possibility)

print("With these two possibilities, we can now eliminate one of them by moving the dial to the first number, putting heavy tension on the shackle, and trying to move the dial back and forth. The number with the looser movement is the correct third digit. \n \nCould you find the looser number? y/n")

found3 = input().lower()  # Convert the input to lowercase to handle 'Y', 'y', 'YES', 'Yes', etc.

if found3 and found3[0] == "y":  # Check if the first character is 'y'
    digit_3 = int(input("Which one was it? "))    
    print("Great! You now have the first and third digits (", digit_1, " and ", digit_3, ") and there will be only 8 possibilities for the second digit that you'll have to try.")

else:
    digit_3 = valid_digit_3_possibilities  # Use the list of possibilities
    print("No worries. You'll just have 16 possibilities for digit 2 to try rather than 8.")


digit_2_possibilities = [(remainder_digit_1 + offset + 8 * i - 40 if remainder_digit_1 + offset + 8 * i > 39 else remainder_digit_1 + offset + 8 * i) for offset in [2, 6] for i in range(5)]

if isinstance(digit_3, int):
    # Single digit_3 value
    filtered_digit_2_possibilities = [value for value in digit_2_possibilities if not (digit_3 - 2 <= value <= digit_3 + 2)]
else:
    # Multiple digit_3 possibilities
    filtered_digit_2_possibilities = digit_2_possibilities
    for d3 in digit_3:
        filtered_digit_2_possibilities = [value for value in filtered_digit_2_possibilities if not (d3 - 2 <= value <= d3 + 2)]

# Special filtering for cases when digit_3 is 0 or 1
if isinstance(digit_3, int) and (digit_3 == 0 or digit_3 == 1):
    filtered_digit_2_possibilities = [value for value in filtered_digit_2_possibilities if value not in (38, 39)]

# Final print statement
if isinstance(digit_3, int):
    print("The combination possibilities to try will be: ", digit_1, filtered_digit_2_possibilities, digit_3)
else:
    for d3 in valid_digit_3_possibilities:
        print("One set of possibilities to try is: ", digit_1, filtered_digit_2_possibilities, d3)
