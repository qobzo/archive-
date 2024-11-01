def define(a, b):
    if isinstance(b, int):
        globals()[a] = int(b)
    else:
        globals()[a] = b.lower()

while True:
    define("location", input("Where do you live?\n"))
    if location == "portland":
        while True:
            location = input("Portland, OR?\n")
            if location.startswith(("y", "or", "portland, o")):
                location = "portland, or"
                break
            elif location.startswith("n"):
                break
    break

while True:
    if location == "portland, or":
        print("Portland, OR?! You better bring that raincoat!")
        quit()        
    try:
        define("chance", int(input("What % likelihood is there of rain?\n")))
        if chance > 50:
            print("I'd wear a raincoat")
            break
        else: 
            print("Leave that raincoat at home.")
            break
    except ValueError:
        print("Type in a number from 1-100.")
