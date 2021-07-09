#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user
from app.db.schemas import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="juan@energetica.coop",
            password="9103ea9c24a7afbf21f3b061ed5cb63b04c3c0c2c0aaf8d97e7832ef5c70e86d",
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser juan@energetica.coop")
    init()
    print("Superuser created")
