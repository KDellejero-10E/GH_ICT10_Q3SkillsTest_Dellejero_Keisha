from pyscript import document
import re

def check_account(event=None):
    username = document.getElementById("username").value
    password = document.getElementById("password").value
    output = document.getElementById("output")

    # Username check
    if len(username) < 7:
        output.innerHTML = "<p class='text-danger'>Username must be at least 7 characters long.</p>"
        return

    # Password checks
    if len(password) < 10:
        output.innerHTML = "<p class='text-danger'>Password must be at least 10 characters long.</p>"
        return

    if not re.search(r"[A-Za-z]", password):
        output.innerHTML = "<p class='text-danger'>Password must contain at least one letter.</p>"
        return

    if not re.search(r"[0-9]", password):
        output.innerHTML = "<p class='text-danger'>Password must contain at least one number.</p>"
        return

    # Success
    output.innerHTML = "<h4 class='text-success'>Account created successfully!</h4>"
