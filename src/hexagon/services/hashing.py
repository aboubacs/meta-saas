from passlib.context import CryptContext

password_crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_str(password: str) -> str:
    return password_crypt_context.hash(password)


def verify_hash(password: str, hashed_password: str) -> bool:
    return password_crypt_context.verify(password, hashed_password)
