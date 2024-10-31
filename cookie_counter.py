# Rewrote Oct 30th, 2024
def errormsg():
    print("Type in a number (ex. 1, 23, 456).")

def define(a, b):
    while True:
        try:
            globals()[a] = int(b)
            break
        except ValueError:
            errormsg

define("cookies", input("How many cookies do we have?\n"))
define("cookiesPot", input("How many are you going to eat?\n"))

while True:
    eaten = input("Have you eaten them? [Y]es or [N]o.\n").lower()
    if eaten.startswith("y"):
        print(f"You have {cookies - cookiesPot} cookies left.")
        break
    elif eaten.startswith("n"):
        print(f"Wise decision, you still have {cookies} to enjoy later.")
        break
    else:
        print("This is a yes or no question\n")
