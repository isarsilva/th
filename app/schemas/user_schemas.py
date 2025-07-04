from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional

# Modelo de autenticação do usuário
# Este modelo é usado para validar os dados de entrada ao criar ou autenticar um usuário.
class UserAuth(BaseModel):           # Definindo o modelo de autenticação do usuário
    email: EmailStr = Field(..., description='Email do usuário')    # Validando o email com EmailStr
    username: str = Field(..., min_length=5, max_length=50, description='Username de usuário') #validando o username com min e max length
    password: str = Field(..., min_Lenght=5, max_length=20, description='Senha do usuário',)   #validando a senha com min e max length

## Modelo de usuário para retorno de dados
# Este modelo é usado para retornar os dados do usuário após a criação ou consulta.
class UserDetail(BaseModel):
    user_id: UUID
    username: str 
    email: EmailStr
    first_name: Optional[str] 
    last_name: Optional[str]
    disabled: Optional[bool] 