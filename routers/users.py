from fastapi import APIRouter, status
from schemas.users import UserListPublicSchema

router = APIRouter()

@router.get(path='/', 
            status_code=status.HTTP_200_OK, 
            response_model=UserListPublicSchema)
async def list_users():
    return {
        'users': [
            {
                'id': 1,
                'username': 'Magno1',
                'email': 'pycodebr@gmail.com',
            },
            {
                'id': 2,
                'username': 'Magno1',
                'email': 'joao@gmail.com',
            },
            {
                'id': 3,
                'username': 'Magno1',
                'email': 'mario@gmail.com',
            },
        ]
    }