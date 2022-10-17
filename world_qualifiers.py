import math

"""
The formula for the number of world qualifiers considering the number of 
competitors at oireachtas is:

- If the number of competitiors is/exceeds 20, there are 5 world qualifiers

- For every world medal holder in the competiton, there is one extra world qualifier spot

- If the number of competitors fall below 20, (I'm not sure but in the meantime use the usual rules)

- After the first 20 competitors are counted there is one world qualifier for every 10 competitors

- If the final number is not an integer, (I'm not 100% sure but) round DOWN to the nearest integer (use math.floor)
"""



# The main function "world_qualifiers" will calculate the number of world qualifiers based on the user's input estimate
# the argument 'n' represents the user's input (estimated number of competitors) 
def world_qualifiers(n):
    wq = 0
    get_wmh()
    mixed_agegroup = input("Is your age group mixed with another? Type 'y' if so, and anything else if not... ")
    if n < 20 or (mixed_agegroup == "y" or mixed_agegroup == "Y"):
        # Less than 20 competitiors or combined age gorups
        wq += 7
    else:
        # 20 or more competitors and not combined, follow regualr rules
        wq += 5
        remaining = n - 20
        wq += math.floor(remaining / 10)
    wq += get_wmh()
    print("There will be about ", wq, " world qualifying spots. ") 


# Prompts the user to get the number of world medal holders dancing
def get_wmh():
    wmh = 0
    while True: 
        try: 
            wmh = int(input("\nHow many world medal holders will be in your competition? \n(If you don't know, just take a good guess or type 0) "))
        except ValueError:
            print("Error! Please enter a whole number!")
        else:
            if wmh < 0:
                print("Error! Type a positive whole number!")
            else:
                print("\n", wmh, "World medal holders means that they will add", wmh, "more world qualifying spots. ")
                break
    return wmh


# Displays the introduction
def intro():
    print("Remember that the number of world qualifiers is based on the number of competitors who show up and complete all their rounds ")
    print("This formula only applies to oireachtas, not any other major\n")


# Takes user's input/estimate of dancers, prompts the user until they enter an integer
def get_num_dancers():
    num_dancers = 0
    while True: 
        try: 
            num_dancers = int(input("\nEnter your estimate of competitors: "))
        except ValueError:
            print("Error! Please enter a whole number!")
        else:
            if num_dancers <= 0:
                print("Error! There must be at least one dancer in your competition!")
            else:
                print(num_dancers, " dancers in your competition? Let me calculate... ")
                break
    return num_dancers



# Calls the functions in order
def main():
    intro()
    n = get_num_dancers()
    world_qualifiers(n) 
    # ask if user wants to check another age group using while loop
    y_or_n = input("Did you want to check another age group? Type 'y' if so, and anything else if not... ")
    run_again = True
    while (y_or_n == "y" or y_or_n == "Y") and run_again:
        # run_again = True
        n = get_num_dancers()
        world_qualifiers(n)
        y_or_n = input("Did you want to check another age group? Type 'y' if so, and anything else if not...")
        if y_or_n != "y" or y_or_n != "Y":
            run_again = False
    print("Remember to point, turn out, and keep your arms back! Best of luck! ")
    

# Calls the functions in order
if __name__ == "__main__": 
    main()
