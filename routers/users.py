from fastapi import APIRouter, HTTPException, status
from models.users import (
    User,
    GetUsersResponse,
    CreateUserResponse,
    DeleteUserResponse,
    UpdateUserRequest,
)

router = APIRouter()

usuarios: list[User] = [
    User(id=1, name="juan perez"),
    User(id=2, name="pepe sanchez"),
]


@router.delete("/user/{id}")
def delete_user(id: int) -> DeleteUserResponse:
    for user in usuarios:
        if user.id == id:
            usuarios.remove(user)
            return DeleteUserResponse(message="usuario borrado")

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


@router.get("/user/{id}")
def get_user(id: int) -> User:
    for user in usuarios:
        if user.id == id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )


@router.get("/user")
def get_users(is_active: bool | None = None) -> GetUsersResponse:
    if is_active is None:
        return GetUsersResponse(users=usuarios)

    filtrados = [u for u in usuarios if u.is_active == is_active]
    return GetUsersResponse(users=filtrados)


@router.put("/user/{id}")
def update_user(id: int, datos: UpdateUserRequest) -> User:
    for user in usuarios:
        if user.id == id:
            user.name = datos.name
            user.is_active = datos.is_active
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )

@router.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user: User) -> CreateUserResponse:
    for existente in usuarios:
        if existente.id == user.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Ya existe un usuario con ese id"
            )

    usuarios.append(user)
    return CreateUserResponse(message="usuario creado")