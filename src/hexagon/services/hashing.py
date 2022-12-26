from passlib.context import CryptContext

password_crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_str(str_to_hash: str) -> str:
    return password_crypt_context.hash(str_to_hash)


def verify_hash(source_str: str, target_str: str) -> bool:
    return password_crypt_context.verify(source_str, target_str)
