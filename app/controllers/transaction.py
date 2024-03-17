from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request

from app.dependecies import get_current_user, get_transaction_service
from app.schemas import Transaction
from app.services.transaction import TransactionService

router = APIRouter()


@router.get("/all")
async def get_all_transactions(user_id: int = Depends(get_current_user),
                               transaction_service: TransactionService = Depends(get_transaction_service)):
    transactions: List[Transaction] = transaction_service.list_transactions(user_id)
    return transactions
