from repository.users_in_memory import UserInMemoryRepo
from repository.user_interface import UserRepository
from utils.constant import DEFAULT_REPOSITORY_TYPE, REPOSITORY_TYPE_IN_MEMORY, REPOSITORY_TYPE_DATABASE
from repository.users_db import UserDBRepo

def create_user_repository(repository_type: str = DEFAULT_REPOSITORY_TYPE) -> UserRepository:
    """
    Factory function to create and return a UserRepository instance.
    This allows for dependency injection and easier testing.
    
    Args:
        repository_type (str): Type of repository to create. Defaults to DEFAULT_REPOSITORY_TYPE.
    
    Returns:
        UserRepository: A new instance of UserRepository
        
    Raises:
        ValueError: If an unsupported repository type is provided
    """
    if repository_type == REPOSITORY_TYPE_IN_MEMORY:
        return UserInMemoryRepo()
    elif repository_type == REPOSITORY_TYPE_DATABASE:
        return UserDBRepo()
    else:
        raise ValueError(f"Unsupported repository type: {repository_type}")