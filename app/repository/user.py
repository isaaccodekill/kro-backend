from sqlmodel import Session, create_engine

from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        return user

    def get(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()

