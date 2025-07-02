#Foi instalada a biblioteca pip install python-decouple
from typing import List # biblioteca padrao do python (modulo typing) é usado par indicar o tipo de lista em anotações de tipo(type hints )principalmente em funções, classes e modelos com FastAPI e Pydantic.
from decouple import config # serve para carregar variaves de ambientes de forma segura e organizada
from pydantic import AnyHttpUrl, BaseSettings # AnyHttpUrl é um tipo de dado do Pydatic que valida se uma string é uma URL HTTP/HTTPS válidas. BaseSettings é uma classe do pydantic usada para criar classes de configuração que automaticamente leem valores do ambiente,.env

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1" # qual vai ser o nome da API_v1
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cst=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_SECRET_KEY", cst=str)
    ALGORITHM = "HS256" # vai ser referente a irformação de segurança 
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 #tempo de expiração do token
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  #token de expiraçção do refresh Token( quanto tempo o token vai expirar ) 60 * 24 * 7  isso equivale a 7 dias
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [] #informação de quais aplicações poderão ter acesso a comunicação dessa API
    PROJECT_NAME: str = "TODOFast" #serve para dar um nome identificador ao seu projeto em configurações


    #Database
    # MYSQL_CONNECTION_STRING: str = config("MYSQL_CONNECTION_STRING", cast=str)
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)  # conexão com o banco de dados MongoDB

    class Config:
        case_sensitive = True

settings = Settings()