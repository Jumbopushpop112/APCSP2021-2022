#validating PIN

pin = "12345"

usersEntry = input("Enter your PIN: ")

while usersEntry != pin:
    print("Invalid PIN. Try again please!")
    usersEntry = input("Try Again. Enter your PIN: ")

print("while loop stopped. Valid PIN entered")