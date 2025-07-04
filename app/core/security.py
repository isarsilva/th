from passlib.context import CryptContext


password_context = CryptContext(
    schemes=["bcrypt"],  # Especifica o algoritmo de hash a ser usado
    deprecated="auto"  # Permite que o Passlib escolha automaticamente o algoritmo mais seguro disponível
)

#converte a senha em um hash
def get_password(password: str) -> str:       
    return password_context.hash(password)


#compara a senha com o hash
def verify_password(password: str, hashed_password: str) -> bool:       
    return password_context.verify(password, hashed_password)