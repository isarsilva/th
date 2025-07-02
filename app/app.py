from fastapi import FastAPI
from core.config import settings 
from beanie import init_beanie  # Importando o Beanie, que é um ODM (Object Document Mapper) para MongoDB
from motor.motor_asyncio import AsyncIOMotorClient # Importando o cliente assíncrono do MongoDB     



app = FastAPI(
    title=settings.PROJECT_NAME,  # Definindo o nome do projeto na documentação da API
    openapi_url=f"{settings.API_V1_STR}/openapi.json",  # Definindo a URL para o OpenAPI
)


#eventos que acob=ntecem antes da aplicação iniciar 
@app.on_event("startup")
async def app_init():
    cliente_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todoapp # Criando uma instância do cliente MongoDB usando a string de conexão definida nas configurações

    await init_beanie(database=cliente_db, document_models=[ # Aqui você deve definir os modelos de documento que serão usados com o Beanie
      ])  # Inicializando o Beanie com o banco de dados e os modelos de documento    
     