from importlib.resources import Resource
from app import app
from flask_restx import Resource, Api
from service.response_payloads_service import assembleDeptsJson, assembleEmployeesJson

api = Api(app,
          title="ACMEVita API",
          doc="/doc")

ns = api.namespace(
    'dept', description='Api for departments of ACMEVita Company')


@ns.route('/<int:dept_id>/employees')
@ns.doc('list_employees', params={'dept_id': 'Department ID'})
class DepartmentEmployees(Resource):

    @ns.doc(responses={404: 'Department not found', 200: 'Success'})
    def get(self, dept_id):
        """Lists all employees of a department"""
        jsonResponse = assembleEmployeesJson(dept_id)
        return jsonResponse


@ns.route('/all')
class Departments(Resource):

    @ns.doc('list_all')
    def get(self):
        """Lists all departments"""
        jsonResponse = assembleDeptsJson()
        return jsonResponse
