# Vangaurd Intel - Authentication & Access Control 
# Controls who can access protected Vangaurd security 

USERS = {
    "admin": {
        "password": "Vanguard123",
        "role": "admin"
    },
    "analyst": {
        "password": "OilData123",
        "role": "analyst"
    }
}

def authenticate(username, password):
    """Check whether the user name and password are valid."""

    if username not in USERS:
        return False, "ACCESS DENIED: Unknown user"
    if USERS[username]["password"] != password:
        return False, "ACCESS DENIED: Incorrect password"
    role = USERS[username]["role"]
    return True, f"ACCESS GRANTED: {username} authenticated as {role}"


username = input ("Username: ")
password = input ("Password: ")

success, message = authenticate(username, password)
print(message)