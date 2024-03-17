from app.repository.transaction import TransactionRepository
from app.seeder import seed_user_with_transactions


class TransactionService:
    def __init__(self, transaction_repo: TransactionRepository):
        self.transaction_repo = transaction_repo

    def list_transactions(self, user_id):
        return self.transaction_repo.list(user_id)

    def create_transactions(self, user_id):
        transactions = seed_user_with_transactions(user_id)
        self.transaction_repo.create_many(transactions)
        return self.list_transactions(user_id)

