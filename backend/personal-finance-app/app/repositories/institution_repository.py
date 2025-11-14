from app.models.institution import Institution


class InstitutionRepository:
    def __init__(self, db):
        self.db = db

    def list_all(self):
        return self.db.query(Institution).all()

    def get(self, institution_id: int):
        return self.db.query(Institution).filter(Institution.id == institution_id).one_or_none()

    def create(self, inst_create):
        website_str = str(inst_create.website) if inst_create.website else None
        inst = Institution(name=inst_create.name, institution_type_id=inst_create.institution_type_id, website=website_str)
        self.db.add(inst)
        self.db.commit()
        self.db.refresh(inst)
        return inst

    def update(self, inst: Institution, updates: dict):
        update_data = updates.copy()
        if 'website' in update_data and update_data['website'] is not None:
            update_data['website'] = str(update_data['website'])

        for key, value in updates.items():
            if hasattr(inst, key) and value is not None:
                setattr(inst, key, update_data.get(key, value))

        self.db.add(inst)
        self.db.commit()
        self.db.refresh(inst)
        return inst

    def delete(self, inst: Institution):
        self.db.delete(inst)
        self.db.commit()
        return None
