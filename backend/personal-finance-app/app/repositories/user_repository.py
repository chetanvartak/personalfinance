from app.models.user import User


class UserRepository:
    def __init__(self, db):
        self.db = db

    def create(self, user_create):
        user = User(username=user_create.username, email=user_create.email, password_hash=getattr(user_create, 'password_hash', getattr(user_create, 'password', None)))
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def list_all(self):
        return self.db.query(User).all()

    def get(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).one_or_none()

    def update(self, user: User, updates: dict):
        for key, value in updates.items():
            if hasattr(user, key) and value is not None:
                setattr(user, key, value)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()
        return None