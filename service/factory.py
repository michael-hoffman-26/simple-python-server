from service.users import UserService
from typing import Protocol

class UserRepository(Protocol):
    """Protocol defining the interface for user repositories."""
    pass

def create_user_service(user_repository: UserRepository) -> UserService:
    """
    Factory function to create and return a UserService instance.
    
    Args:
        user_repository: An instance of UserRepository to be used by the service
        
    Returns:
        UserService: A configured instance of UserService
    """
    return UserService(user_repository)