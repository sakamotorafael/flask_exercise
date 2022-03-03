from importlib.resources import Resource
from flask_restx import Resource, Api
from app import app
from service.response_payloads_service import assembleDeptsJson, assembleEmployeesJson


api = Api(app,
    title="ACMEVita API",
    doc="/doc")

namespace = api.namespace(
    'dept', description='Api for departments of ACMEVita Company')


@namespace.route('/<int:dept_id>/employees')
@namespace.doc('list_employees', params={'dept_id': 'Department ID'})
class DepartmentEmployees(Resource):

    @namespace.doc(responses={404: 'Department not found', 200: 'Success'})
    def get(self, dept_id):
        """Lists all employees of a department"""
        jsonResponse = assembleEmployeesJson(dept_id)
        return jsonResponse


@namespace.route('/all')
class Departments(Resource):

    @namespace.doc('list_all')
    def get(self):
        """Lists all departments"""
        jsonResponse = assembleDeptsJson()
        return jsonResponse


