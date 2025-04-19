import re

def validate_username(username):
    # Alphanumeric usernames, underscores, 3-30 chars
    return re.match(r'^[a-zA-Z0-9_]{3,30}$', username) is not None

def validate_email(email):
    # Basic email validation pattern
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email) is not None
