def define(a, b):
    while True:
        try:
            globals()[a] = b
            break
        except ValueError:
            print("Type in a number (ex. 1, 50, 100).")

while True:
    define("location", input("Where do you live?\n"))
    if location.lower() == "portland":
        location = input("Portland, OR?\n").lower()
    if location.startswith(("y", "or")) or location == "portland, or":
        location = "portland, or"
        print("Portland, OR?! You better bring that raincoat!")
        quit()
    else:
        define("chance", int(input("What % likelihood is there of rain?\n")))
        if chance > 50:
            print("I'd wear a raincoat")
            break
        else: 
            print("Leave that raincoat at home.")
            break
