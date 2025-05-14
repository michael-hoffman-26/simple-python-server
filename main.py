from flask import Flask
from routes.trucks import trucks_bp
from routes.packages import package_bp

app = Flask(__name__)

# Register the users blueprint
app.register_blueprint(trucks_bp)
app.register_blueprint(package_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
