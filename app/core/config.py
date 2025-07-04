#Foi instalada a biblioteca pip install python-decouple
from typing import List # biblioteca padrao do python (modulo typing) é usado par indicar o tipo de lista em anotações de tipo(type hints )principalmente em funções, classes e modelos com FastAPI e Pydantic.
from decouple import config # serve para carregar variaves de ambientes de forma segura e organizada
from pydantic_settings import BaseSettings       # BaseSettings é uma classe do Pydantic que permite criar configurações baseadas em variáveis de ambiente, facilitando a leitura de valores de configuração de forma segura e organizada.
from pydantic import AnyHttpUrl  # AnyHttpUrl é um tipo de dado do Pydatic que valida se uma string é uma URL HTTP/HTTPS válidas. BaseSusadaettings é uma classe do pydantic  para criar classes de configuração que automaticamente leem valores do ambiente,.env
from typing import ClassVar   # ClassVar é um tipo de dado do Python usado para indicar que uma variável é uma variável de classe, não uma variável de instância. É usado principalmente em anotações de tipo(type hints) para indicar que a variável pertence à classe como um todo, e não a uma instância específica da classe.

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"  # Caminho base da API

    # Pegando valores do .env
    JWT_SECRET_KEY: str = config("JWT_SECRET_KEY", cast=str)
    JWT_REFRESH_SECRET_KEY: str = config("JWT_REFRESH_SECRET_KEY", cast=str)

    # Constantes que não vêm do .env → precisam ser ClassVar
    ALGORITHM: ClassVar[str] = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: ClassVar[int] = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: ClassVar[int] = 60 * 24 * 7  # 7 dias

    # Lista de URLs confiáveis para CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # Nome do projeto
    PROJECT_NAME: str = "TODOFast"

    class Config:
        extra = "ignore"  # Ignora campos extras no .env

    # #Database
    # # MYSQL_CONNECTION_STRING: str = config("MYSQL_CONNECTION_STRING", cast=str)
    MONGO_CONNECTION_STRING: str = config("MONGO_CONNECTION_STRING", cast=str)  # conexão com o banco de dados MongoDB

    # conexão so com docker

    class Config:
        case_sensitive = True

settings = Settings()