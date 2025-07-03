from fastapi import FastAPI
from app.core.config import settings  # Importando as configurações definidas no arquivo config.py
from beanie import init_beanie  # Importando o Beanie, que é um ODM (Object Document Mapper) para MongoDB
from motor.motor_asyncio import AsyncIOMotorClient # Importando o cliente assíncrono do MongoDB     
from app.models.user_model import User  # Importando o modelo de usuário definido no arquivo user_model.py



app = FastAPI(
    title=settings.PROJECT_NAME,  # Definindo o nome do projeto na documentação da API
    openapi_url=f"{settings.API_V1_STR}/openapi.json",  # Definindo a URL para o OpenAPI
)


#eventos que acob=ntecem antes da aplicação iniciar 
# @app.on_event("startup")
# async def app_init():
#     cliente_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todoapp # Criando uma instância do cliente MongoDB usando a string de conexão definida nas configurações

#     await init_beanie(database=cliente_db,
#                        document_models=[ User ])  # dentro do []  defini os modelos de documento que serão usados com o Beanie, depois inicia o Beanie com o banco de dados MongoDB criado anteriormente. Isso permite que o Beanie saiba quais modelos de documento estão disponíveis para serem usados na aplicação.                        
                                                   
@app.on_event("startup")
async def app_init():
    try:
        # Adicione timeout para evitar travamentos
        client = AsyncIOMotorClient(
            settings.MONGO_CONNECTION_STRING,
            serverSelectionTimeoutMS=5000
        )
        await client.server_info()  # Testa a conexão
        client_db = client.todoapp
        
        await init_beanie(
            database=client_db,
            document_models=[User]
        )
        print("✅ Conexão com MongoDB estabelecida!")
    except Exception as e:
        print(f"❌ Erro ao conectar ao MongoDB: {e}")
        raise
    
    #intalaçao de duas bibliotecas pip install email-validator para validação de email e pip install pydantic[email]
     
