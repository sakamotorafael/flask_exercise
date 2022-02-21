from flask import Flask

app = Flask(__name__)

from db_config import db

from models.Department import Department
from models.Employee import Employee
from models.Dependent import Dependent

from endpoints import home, page, dept_employees

if __name__ == '__main__':
    app.run(debug=True)