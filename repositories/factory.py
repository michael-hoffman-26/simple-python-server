from repositories.users import UserRepository

def create_user_repository() -> UserRepository:
    """
    Factory function to create and return a UserRepository instance.
    This allows for dependency injection and easier testing.
    
    Returns:
        UserRepository: A new instance of UserRepository
    """
    return UserRepository()