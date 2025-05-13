class UserRepository:
    def __init__(self):
        # Simulating an in-memory database
        self._users = {}
        print("UserRepository initialized")

    def create_user(self, user_data):
        """Create a new user"""
        user_id = len(self._users) + 1
        self._users[user_id] = user_data
        print(f"Creating user with data: {user_data}")
        return user_id

    def get_user(self, user_id):
        """Get a user by ID"""
        print(f"Fetching user with ID: {user_id}")
        return self._users.get(user_id)

    def get_all_users(self):
        """Get all users"""
        print("Fetching all users")
        return list(self._users.values())

    def update_user(self, user_id, user_data):
        """Update a user"""
        if user_id in self._users:
            print(f"Updating user {user_id} with data: {user_data}")
            self._users[user_id] = user_data
            return True
        return False

    def delete_user(self, user_id):
        """Delete a user"""
        if user_id in self._users:
            print(f"Deleting user with ID: {user_id}")
            del self._users[user_id]
            return True
        return False 