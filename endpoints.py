from importlib.resources import Resource
from app import app, Department
from flask_restx import Resource, Api
import json

api = Api(app,
    title="ACMEVita API",
    doc="/doc")

@api.route('/dept/<int:dept_id>/employees')
@api.doc(params={'dept_id': 'Department ID'})
class DepartmentEmployees(Resource):

    @api.doc(responses={404: 'Departamento não encontrado', 200: 'Nome do departamento e colaboradores'})
    def get(self, dept_id):
        dept = Department.query.get(dept_id)

        if(dept == None):
            response = app.response_class(
                response=json.dumps("Department not found!"),
                status=404,
                mimetype='application/json'
            )
        else:
            result = {
                "department": dept.name,
                "employees": []
            }

            for employee in dept.employees:
                employee_dict = {
                    "name": employee.name,
                    "has_dependents": len(employee.dependents) > 0
                }
                result['employees'].append(employee_dict)

            response = app.response_class(
                response=json.dumps(result),
                status=200,
                mimetype='application/json'
            )    
        
        return response