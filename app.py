from flask import Flask

app = Flask(__name__)

from db_config import db

from models.Department import Department
from models.Employee import Employee
from models.Dependent import Dependent

import endpoints

if __name__ == '__main__':
    app.run(debug=True)