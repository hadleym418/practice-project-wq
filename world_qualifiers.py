import math
"""
The formula for the number of world qualifiers considering the number of 
competitors at oireachtas is:

- If the number of competitiors is/exceeds 20, there are 5 world qualifiers

- If the number of competitors fall below 20, (I'm not sure but in the meantime use the usual rules)

- After the first 20 competitors are counted there is one world qualifier for every 10 competitors

- If the final number is not an integer, (I'm not 100% sure but) round DOWN to the nearest integer (use math.floor)
"""

# The main function "world_qualifiers" will calculate the number of world qualifiers based on the user's input estimate
def world_qualifiers():
    print("main function ")

# This function takes user's input/estimate of dancers
def getNumDancers():
    # print("Enter your estimate of competitors: ")
    try:
        # n = int(input)
        n = int(input("Enter your estimate of competitors: "))
        print("Correct, this is an int (remove later)")
    except ValueError:
        # print("Please try again and enter a whole number")
        n = int(input("Enter your estimate of competitors: "))
    # return n
    

# # This function checks whether the user input is an integer, throws an error and promts the user if not
# def checkInput(input): 
#     try:
#         n = int(input)
#         print("Correct, this is an int (remove later)")
#     except ValueError:
#         print("Please enter a whole number")

if __name__ == "__main__": 
    print("Remember that the number of world qualifiers is based on the number of competitors who show up and complete all their rounds ")
    print("This formula only applies to oireachtas, not any other major\n")
    # n = input(getNumDancers())
    n = getNumDancers()
    # world_qualifiers()
    # print("number of dancers was typed in")
