password = input("Password: ")

special = "!@#$%^&*"

while True:
    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False

    if len(password) < 8:
        print("Password must be at least 8 characters long.")

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch in special:
            has_special = True

    if not has_digit:
        print("Invalid: must contain a digit.")
    if not has_upper:
        print("Invalid: must contain an uppercase letter.")
    if not has_lower:
        print("Invalid: must contain a lowercase letter.")
    if not has_special:
        print("Invalid: must contain a special character.")

    if has_digit and has_upper and has_lower and has_special:
        print("Password Accepted!")
        break
    else:
        print()
        password = input("Password: ")
