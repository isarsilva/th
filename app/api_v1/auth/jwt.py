from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService

auth_router = APIRouter()

# Rota para autenticação de usuário
# Esta rota recebe os dados de login e retorna um token JWT se as credenciais forem válidas.
# O token JWT é usado para autenticar o usuário em outras rotas protegidas da API
@auth_router.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email=data.email,
        password=data.password
    )
