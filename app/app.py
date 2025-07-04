from fastapi import FastAPI
from app.core.config import settings  # Importando as configurações definidas no arquivo config.py
from beanie import init_beanie  # Importando o Beanie, que é um ODM (Object Document Mapper) para MongoDB
from motor.motor_asyncio import AsyncIOMotorClient # Importando o cliente assíncrono do MongoDB     
from app.models.user_model import User  # Importando o modelo de usuário definido no arquivo user_model.py
from app.api_v1.handlers import user   # Importando as rotas da API definidas no arquivo routes.py


app = FastAPI(
    title=settings.PROJECT_NAME,  # Definindo o nome do projeto na documentação da API
    openapi_url=f"{settings.API_V1_STR}/openapi.json",  # Definindo a URL para o OpenAPI
)


#eventos que acob=ntecem antes da aplicação iniciar 
@app.on_event("startup")
async def app_init():
    cliente_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todoapp # Criando uma instância do cliente MongoDB usando a string de conexão definida nas configurações

    await init_beanie(database=cliente_db,
                       document_models=[ User ])  # dentro do []  defini os modelos de documento que serão usados com o Beanie, depois inicia o Beanie com o banco de dados MongoDB criado anteriormente. Isso permite que o Beanie saiba quais modelos de documento estão disponíveis para serem usados na aplicação.                        
                                                   




app.include_router(
    User.user_router,  # Incluindo o roteador de usuários no roteador principal
    prefix=settings.API_V1_STR,  # Definindo o prefixo para as rotas de usuários
    tags=["users"],  # Adicionando uma tag para agrupar as rotas de usuários na documentação da API
)
    
    #intalaçao de duas bibliotecas pip install email-validator para validação de email e pip install pydantic[email]
     # instalar bibliotecas  pip install "python-jose[cryptography]" "passlib[bcrypt]"
