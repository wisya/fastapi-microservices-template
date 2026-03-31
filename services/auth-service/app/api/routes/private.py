from typing import Any

from fastapi import APIRouter, HTTPException

from app import crud
from app.api.deps import SessionDep
from app.models import (
    UserCreate,
    UserPublic,
)

router = APIRouter(tags=["private"], prefix="/private")


@router.post("/users/", response_model=UserPublic)
def create_user(user_in: UserCreate, session: SessionDep) -> Any:
    """
    Create a new user.
    """
    user = crud.get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user = crud.create_user(session=session, user_create=user_in)
    return user
