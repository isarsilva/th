from fastapi import APIRouter  # Importando o APIRouter do FastAPI, que é usado para criar rotas da API
from api_v1.handlers import user  # Importando o roteador de usuários definido no arquivo user.py

router = APIRouter()  # Criando uma instância do APIRouter para definir as rotas da API


router.include_router(
    user.user_router,  # Incluindo o roteador de usuários no roteador principal
    prefix="/users",  # Definindo o prefixo para as rotas de usuários
    tags=["users"],  # Adicionando uma tag para agrupar as rotas de usuários na documentação da API
)  # Isso permite que todas as rotas definidas no roteador de usuários sejam acessíveis sob o prefixo "/users"  