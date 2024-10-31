while True:
    location = input("Where do you live?\n")
    if location.lower() == "portland":
        while True:
            location = input("Portland, OR?\n")
            if location.startswith(("y", "or", "portland, or")):
                location = "portland, or"
                break
            elif location.startswith("n"):
                break
    break

while True:
    if location == "portland, or":
        print("Portland?! You better bring a raincoat!")
        quit()
    else:
        chance = input("What % likelihood is there of rain?\n")
        try:
            chance = int(chance)
            if chance > 50:
                print("I'd wear a raincoat")
                break
            else:
                print("Leave that raincoat at home.")
                break
        except ValueError:
            print("Type in a number from 1-100.")
