from typing import List

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import oauth2

# from sqlalchemy.sql.functions import func
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/budget", tags=["Budget"])


@router.get("/", response_model=List[schemas.DailySpending])
def get_budget(
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # budget = cursor.execute("""SELECT * FROM budget""")
    # budget = cursor.fetchall()

    # Get only your budget.(Not review other users budgets!)
    budget = (
        db.query(models.Budget).filter(models.Budget.owner_id == current_user.id).all()
    )
    return budget


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserSpend)
def daily_spending(
    spend: schemas.UserSpend,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # cursor.execute(
    #     """INSERT INTO budget (daily_spending) VALUES (%s) RETURNING *""",
    #     (spend.daily_spending,),
    # )
    # new_budget = cursor.fetchone()
    # conn.commit()
    daily_spend = models.Budget(owner_id=current_user.id, **spend.dict())
    db.add(daily_spend)
    db.commit()
    db.refresh(daily_spend)
    return daily_spend


@router.get("/{id}")
def get_budget(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    budget = db.query(models.Budget).filter(models.Budget.id == id).first()
    if not budget:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"budget with id:{id} was not found",
        )
    if budget.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action!",
        )
    return budget


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_budget(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    budget_query = db.query(models.Budget).filter(models.Budget.id == id)
    budget = budget_query.first()
    if budget == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"budget with {id} does not exist!",
        )
    if budget.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action!",
        )
    budget.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(
    id: int,
    updated_spend: schemas.DailySpending,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    budget_query = db.query(models.Budget).filter(models.Budget.id == id)
    budget = budget_query.first()
    if budget == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"budget with id:{id} does not exist",
        )
    if budget.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action!",
        )
    budget_query.update(updated_spend.dict(), synchronize_session=False)
    db.commit()
    return budget_query.first()
