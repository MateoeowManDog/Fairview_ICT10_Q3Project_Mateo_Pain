from flask import document

def validate_account(event=None):
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    output = document.getElementById("output")

    # Check username length
    if len(username) < 7:
        output.innerText = "Username must contain at least 7 characters."
        return

    # Password conditions
    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True

    if len(password) < 10:
        output.innerText = "Password must be at least 10 characters long."
        return

    if not has_letter:
        output.innerText = "Password must contain at least one letter."
        return

    if not has_number:
        output.innerText = "Password must contain at least one number."
        return

    # If all conditions are met
    output.innerText = ("Account successfully created")