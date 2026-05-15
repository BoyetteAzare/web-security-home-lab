
from flask import Flask
from flask_mysqldb import MySQL
from config import Config
import os


app = Flask(__name__, 
    template_folder=os.path.join('..', 'frontend', 'templates'),
    static_folder=os.path.join('..', 'frontend', 'static')
)
app.config.from_object(Config)
mysql = MySQL(app)

from routes import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)