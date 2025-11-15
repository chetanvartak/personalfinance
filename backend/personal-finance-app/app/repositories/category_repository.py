from app.models.category import Category


class CategoryRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Category).all()

    def get(self, category_id: int):
        return self.db.query(Category).filter(Category.id == category_id).one_or_none()

    def create(self, payload):
        cat = Category(name=payload.name, parent_id=payload.parent_id)
        self.db.add(cat)
        self.db.commit()
        self.db.refresh(cat)
        return cat

    def update(self, cat: Category, updates: dict):
        for key, value in updates.items():
            if hasattr(cat, key) and value is not None:
                setattr(cat, key, value)
        self.db.add(cat)
        self.db.commit()
        self.db.refresh(cat)
        return cat

    def delete(self, cat: Category):
        self.db.delete(cat)
        self.db.commit()
        return None
