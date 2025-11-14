from app.repositories.user_repository import UserRepository
from app.core.security import create_access_token

# Placeholder authenticate
def authenticate_user(username: str, password: str):
    # In a real app, verify hashed password
    # For now return a mock user
    return {"username": username}

def create_access_token_for_user(user):
    return create_access_token({"sub": user['username']})
