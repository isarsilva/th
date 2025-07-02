from beanie import Document, Indexed # Importando o Beanie, que é um ODM (Object Document Mapper) para MongoDB
# Importando Indexed para criar índices nos campos do documento
from uuid import UUID, uuid4    # Importando UUID e uuid4 para gerar identificadores únicos
from pydantic import EmailStr, Field    # Importando EmailStr para validação de e-mails e Field para definir campos do modelo
from datetime import datetime      # Importando datetime para trabalhar com datas e horas
from typing import Optional, Annotated  # Importando Optional para campos que podem ser nulos e Annotated para anotações de tipos


class User(Document):
    user_id: UUID = Field(default_factory=uuid4)

    username: Annotated[str, Indexed(unique=True)]
    email: Annotated[EmailStr, Indexed(unique=True)]

    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = False


def __repr__(self) -> str: #Representação técnica/detalhada	repr(user) ou debug automático
    return f"<User{self.email}>"

def __str__(self) -> str: #	Representação amigável para humanos	print(user)
    return self.email

def __hash__(self) -> int: #Garante uso em set, dict como chave	set([user]), {user: "info"}
    return hash(self.email)

def __eq__(self, other: object) -> bool: #Comparação de igualdade	user1 == user2
    if not isinstance(other, User):
        return self.email == other.email
        return False
    
