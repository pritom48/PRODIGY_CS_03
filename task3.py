import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine the strength level
    if strength == 5:
        feedback.append("Password strength: Strong")
    elif strength >= 3:
        feedback.append("Password strength: Medium")
    else:
        feedback.append("Password strength: Weak")

    return feedback

def main():
    password = input("Enter a password to assess: ")
    feedback = assess_password_strength(password)
    for comment in feedback:
        print(comment)

if __name__ == "__main__":
    main()
