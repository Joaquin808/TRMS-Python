from flask import Flask
from controllers import main_controller as mc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # For front-end (JavaScript and HTML)
mc.run(app)

if __name__ == '__main__':
    app.run(debug=True)

