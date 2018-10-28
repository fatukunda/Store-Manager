from app.models.user import User


class Attendant (User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.user_type = 'attendant'
        
