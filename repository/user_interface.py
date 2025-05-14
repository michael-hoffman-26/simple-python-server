from abc import ABC, abstractmethod

class UserRepository(ABC):
    """Abstract base class defining the interface for user repositories"""
    
    @abstractmethod
    def create_user(self, user_data):
        """Create a new user"""
        pass
    
    @abstractmethod
    def get_user(self, user_id):
        """Get a user by ID"""
        pass
    
    @abstractmethod
    def get_all_users(self):
        """Get all users"""
        pass
    
    @abstractmethod
    def update_user(self, user_id, user_data):
        """Update a user"""
        pass
    
    @abstractmethod
    def delete_user(self, user_id):
        """Delete a user"""
        pass 