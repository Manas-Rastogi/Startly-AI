from fastapi import HTTPException

from schemas.user_schema import UserRegister
from schemas.auth_schema import UserLogin
from models.user_model import UserModel

from repositories.user_repository import UserRepository
from security.password import PasswordService
from security.jwt import JwtService


class AuthService:

    def __init__(
        self,
        user_repository: UserRepository,
        password_service: PasswordService,
        jwt_service: JwtService
    ):
        self.user_repository = user_repository
        self.password_service = password_service
        self.jwt_service = jwt_service

    # REGISTER
    def register_user(self, user: UserRegister):

        existing_user = self.user_repository.find_by_email(
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

        hashed_password = self.password_service.hash_password(
            user.password
        )

        user_model = UserModel(
            username=user.username,
            email=str(user.email).lower(),
            hashed_password=hashed_password
        )

        user_id = self.user_repository.create_user(
            user_model.model_dump()
        )

        return {
            "id": user_id,
            "username": user.username,
            "email": str(user.email).lower()
        }

    # LOGIN
    def login_user(self, user: UserLogin):

        existing_user = self.user_repository.find_by_email(
            str(user.email).lower()
        )

        if not existing_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        is_valid = self.password_service.verify_password(
            user.password,
            existing_user["hashed_password"]
        )

        if not is_valid:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        token = self.jwt_service.create_access_token(
            str(existing_user["_id"])
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }