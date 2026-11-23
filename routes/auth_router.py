from fastapi import APIRouter, Depends

from schemas.user_schema import UserRegister
from schemas.auth_schema import UserLogin

from services.auth_service import AuthService
from dependency import get_auth_service


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user: UserRegister,
    auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.register_user(user)


@router.post("/login")
def login(
    user: UserLogin,
    auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.login_user(user)