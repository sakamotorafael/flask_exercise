

from flask import Flask


def create_app():
    return Flask(__name__)

app = create_app()

from data.db_config import db

from models.Dependent import Dependent
from models.Employee import Employee
from models.Department import Department

import controller.api.depts_controller


if __name__ == '__main__':
    app.run(debug=True)
