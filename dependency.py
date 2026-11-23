import os

from dotenv import load_dotenv
from fastapi import Depends
from pwdlib import PasswordHash

from security.password import PasswordService
from security.jwt import JwtService

from repositories.user_repository import UserRepository
from repositories.startup_repository import StartupRepository

from services.auth_service import AuthService
from services.funding_api import FundingApiService
from services.groq_service import GroqService
from services.startup_service import StartupService

from database.connection import users_collection, db

load_dotenv()


# ==========================================
# 1. PASSWORD HASH PROVIDER
# ==========================================

def get_password_hash() -> PasswordHash:
    return PasswordHash.recommended()


# ==========================================
# 2. PASSWORD SERVICE PROVIDER
# ==========================================

def get_password_service(
    password_hash: PasswordHash = Depends(get_password_hash)
) -> PasswordService:

    return PasswordService(password_hash)


# ==========================================
# 3. JWT SERVICE PROVIDER
# ==========================================

def get_jwt_service() -> JwtService:

    secret_key = os.getenv("JWT_SECRET_KEY")

    if not secret_key:
        raise RuntimeError("JWT_SECRET_KEY is missing")

    return JwtService(
        secret_key=secret_key,
        algorithm=os.getenv("JWT_ALGORITHM", "HS256"),
        expire_minutes=int(os.getenv("JWT_EXPIRE_MINUTES", "30"))
    )


# ==========================================
# 4. USER REPOSITORY PROVIDER
# ==========================================

def get_user_repository() -> UserRepository:

    return UserRepository(users_collection)


# ==========================================
# 5. AUTH SERVICE PROVIDER
# ==========================================

def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository),
    password_service: PasswordService = Depends(get_password_service),
    jwt_service: JwtService = Depends(get_jwt_service)
) -> AuthService:

    return AuthService(
        user_repository,
        password_service,
        jwt_service
    )


# ==========================================
# 6. FUNDING API SERVICE
# ==========================================

def get_funding_api_service() -> FundingApiService:

    return FundingApiService()


# ==========================================
# 7. GROQ SERVICE
# ==========================================

def get_groq_service() -> GroqService:

    return GroqService()


# ==========================================
# 8. STARTUP REPOSITORY
# ==========================================

def get_startup_repository() -> StartupRepository:

    return StartupRepository(db)


# ==========================================
# 9. STARTUP SERVICE
# ==========================================

def get_startup_service() -> StartupService:

    funding_api_service = get_funding_api_service()
    groq_service = get_groq_service()
    startup_repository = get_startup_repository()

    return StartupService(
        funding_api_service=funding_api_service,
        groq_service=groq_service,
        startup_repository=startup_repository
    )