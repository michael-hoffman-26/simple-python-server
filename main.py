from flask import Flask
from routes.users import users_bp

app = Flask(__name__)

# Register the users blueprint
app.register_blueprint(users_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
