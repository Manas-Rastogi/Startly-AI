from pwdlib import PasswordHash


class PasswordService:

    def __init__(self, password_hash: PasswordHash):
        self.password_hash = password_hash

    def hash_password(self, password: str) -> str:
        return self.password_hash.hash(password)

    def verify_password(
        self,
        password: str,
        hashed_password: str
    ) -> bool:
        return self.password_hash.verify(
            password,
            hashed_password
        )