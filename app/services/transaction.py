from app.repository.transaction import TransactionRepository


class TransactionService:
    def __init__(self, transaction_repo: TransactionRepository):
        self.transaction_repo = transaction_repo

    def list_transactions(self, user_id):
        return self.transaction_repo.list(user_id)

    def create_transactions(self, transactions):
        return self.transaction_repo.create_many(transactions)


