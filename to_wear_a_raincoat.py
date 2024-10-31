def errormsg():
    print("Type in a number (ex. 1, 50, 100).")

while True:
    rainchance = input("What % likelihood is there of rain?\n")
    try:
        rainchance = int(rainchance)
        break
    except ValueError:
        errormsg()

while True:
    location = input("Where do you live?")
    try:
        location = str(location)
        break
    except ValueError:
        errormsg()

while True:
    if location == "portland":
        print("Portland?! You better bring that raincoat!")
    elif rainchance > 50:
        print("I'd wear a raincoat")
    else:
        print("Leave that raincoat at home.")
    break
