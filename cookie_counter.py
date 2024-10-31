def errormsg():
    print("Type in a number (ex. 1, 23, 456).")

while True:
    num_cookies = input("How many cookies do we have?\n")
    try:
        num_cookies = int(num_cookies)
        break
    except ValueError:
        errormsg()

while True:
    num_cookies_potential = input("How many are you going to eat?\n")
    try:
        num_cookies_potential = int(num_cookies_potential)
        break
    except ValueError:
        errormsg()
