class User:
    first_name = '',
    last_name = ''
    role = 'user'
    def __init__(self, username = '', email = '', password =''):
        self.username = username
        self.email = email
        self.password = password
        
