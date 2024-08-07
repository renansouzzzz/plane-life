from MySQLdb import IntegrityError
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.users.user_adm import UserAdmCreate, UserAdmUpdate

from config.db.database import engine

from schemas.users.user_adm import UserAdmMapped, UserAdmSchema


def getAll():
    with Session(engine) as session:
        data = session.query(UserAdmMapped).all()
        if data is None:
            raise ValueError(f'Nenhum usuário encontrado!')
        return data


def getById(id: int):
    with Session(engine) as session:
        try:
            data = session.get(UserAdmMapped, id)

            if data is None:
                raise ValueError(f'O usuário com ID {id} não foi encontrado!')
        except:
            raise HTTPException(status_code=400, detail='Não foi possível coletar o usuário!')

        return data


def create(payload: UserAdmCreate):
    with Session(engine) as session:
        try:
            user = UserAdmSchema(**payload.dict())

            session.add(user)
            session.commit()
            session.refresh(user)
        except IntegrityError as e:
            session.rollback()
            raise HTTPException(status_code=400, detail=f'Error on database: {e}')

        return user


def update(user: UserAdmUpdate, id: int):
    with Session(engine) as session:

        try:
            getUserById = session.query(UserAdmSchema).filter(UserAdmSchema.id == id).one_or_none()

            if not getUserById:
                raise HTTPException(status_code=404, detail="Usuário não encontrado!")

            for var, value in vars(user).items():
                setattr(getUserById, var, value)

            session.add(getUserById)
            session.commit()
            session.refresh(getUserById)

        except IntegrityError as e:
            session.rollback()
            raise HTTPException(status_code=400, detail=f'Error on database: {e}')

        return getUserById


def delete(id: int):
    with Session(engine) as session:
        try:
            getUser = session.get(UserAdmSchema, id)

            if not getUser:
                raise HTTPException(status_code=404, detail='Usuário não encontrado!')

            session.delete(getUser)
            session.commit()

        except IntegrityError as e:
            session.rollback()
            raise HTTPException(status_code=400, detail=f'Error on database: {e}')

        return "Usuário deletado com sucesso!"
