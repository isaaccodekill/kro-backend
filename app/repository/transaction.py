from app.models.transaction import Transaction
from sqlmodel import Session


class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, user_id):
        return self.db.query(Transaction).filter(Transaction.user_id == user_id).all()

    def create_many(self, transactions):
        self.db.add_all(transactions)
        self.db.commit()
        return transactions
