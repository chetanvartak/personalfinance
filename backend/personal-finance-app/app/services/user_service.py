from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def create_user(self, user_create):
        return self.repo.create(user_create)

    def list_users(self):
        return self.repo.list_all()
