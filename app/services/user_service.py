from schemas.user_schemas import UserAuth
from models.user_model import User
from core.security import get_password


#cadastro de usuário
class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        usuario = User(
            username = user.username,
            email = user.email,
            hash_password = get_password(user.password)
        )
        await usuario.save()
        return usuario