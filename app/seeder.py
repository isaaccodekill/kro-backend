from sqlmodel import Session, create_engine
from app.models.user import User
from app.models.transaction import Transaction
from app.enums import TransactionType

# every user will be seeded with 10 - 20 transactions
# each transaction will have a random amount between 1200 and 10000
# each transaction will have a random type of either deposit or withdrawal
# each transaction will have a random timestamp
# each transaction will have a random payment method
# each transaction will be associated with a user


def seedUserWithTransactions(user: User):
    for i in range(10, 20):
        transaction = Transaction(
            amount= 1200 + i * 1000,
            type=  , # or "withdrawal"
            timestamp="2021-10-10 10:10:10",
            payment_method="cash",
            user_id=user.id
        )
        user.transactions.append(transaction)
