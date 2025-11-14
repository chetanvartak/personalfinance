from app.models.institution import Institution


class InstitutionRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Institution).all()

    def get(self, institution_id: int):
        return self.db.query(Institution).filter(Institution.id == institution_id).one_or_none()

    def create(self, inst_create):
        inst = Institution(name=inst_create.name, type=getattr(inst_create, 'type', None), website=getattr(inst_create, 'website', None))
        self.db.add(inst)
        self.db.commit()
        self.db.refresh(inst)
        return inst

    def update(self, inst: Institution, updates: dict):
        for key, value in updates.items():
            if hasattr(inst, key) and value is not None:
                setattr(inst, key, value)
        self.db.add(inst)
        self.db.commit()
        self.db.refresh(inst)
        return inst

    def delete(self, inst: Institution):
        self.db.delete(inst)
        self.db.commit()
        return None
