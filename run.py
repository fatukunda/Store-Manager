from app import create_app
import os
app = create_app('prod')

if __name__ == '__main__':
   app.run()