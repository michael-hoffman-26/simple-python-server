from flask import request
from typing import Dict, List, Optional, Any, Union
from repositories.users import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def get_home(self) -> str:
        return 'Welcome to the Simple Flask Server!'

    def get_hello(self) -> Dict[str, str]:
        return {'message': 'Hello, World!'}

    def process_echo_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return data

    def create_greeting(self, name: str) -> Dict[str, str]:
        return {'message': f'Hello, {name}!'}

    def create_user(self, user_data: Dict[str, Any]) -> int:
        return self.user_repository.create_user(user_data)

    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        return self.user_repository.get_user(user_id)

    def get_all_users(self) -> List[Dict[str, Any]]:
        return self.user_repository.get_all_users()

    def update_user(self, user_id: int, user_data: Dict[str, Any]) -> bool:
        return self.user_repository.update_user(user_id, user_data)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repository.delete_user(user_id) 