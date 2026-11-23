import jwt

from datetime import datetime, timedelta, timezone


class JwtService:

    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        expire_minutes: int
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expire_minutes = expire_minutes

    def create_access_token(self, user_id: str) -> str:

        expire = datetime.now(timezone.utc) + timedelta(
            minutes=self.expire_minutes
        )

        payload = {
            "sub": user_id,
            "exp": expire
        }

        token = jwt.encode(
            payload,
            self.secret_key,
            algorithm=self.algorithm
        )

        return token

    def verify_token(self, token: str):

        return jwt.decode(
            token,
            self.secret_key,
            algorithms=[self.algorithm]
        )