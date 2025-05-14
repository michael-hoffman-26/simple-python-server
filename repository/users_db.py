from repository.user_interface import UserRepository
from database.database import get_db
from database.models import User    

class UserDBRepo(UserRepository):
    def __init__(self):
        self.db = next(get_db())  # Get the actual session from the generator
        self.session = self.db

    def create_user(self, user_data):
        # Ensure we only use valid fields from user_data
        valid_fields = {
            'username': user_data.get('username'),
            'email': user_data.get('email'),
            'password_hash': user_data.get('password_hash')
        }
        new_user = User(**valid_fields)
        self.session.add(new_user)
        self.session.commit()
        return new_user.id      
    
    def get_user(self, user_id):
        user = self.session.query(User).filter(User.id == user_id).first()
        return user.to_dict() if user else None
    
    def get_all_users(self):
        users = self.session.query(User).all()
        return [user.to_dict() for user in users]   
    
    def update_user(self, user_id, user_data):
        user = self.session.query(User).filter(User.id == user_id).first()
        if user:
            # Only update valid fields
            valid_fields = ['username', 'email', 'password_hash']
            for key, value in user_data.items():
                if key in valid_fields:
                    setattr(user, key, value)
            self.session.commit()
            return True 
        return False
    
    def delete_user(self, user_id):
        user = self.session.query(User).filter(User.id == user_id).first()
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False