from app import app, Department
import json

@app.route('/')
def home():
    return "<h1>HOME PAGE</h1>"

@app.route('/page')
def page():
    return "<h1>I am another page</h1>"

@app.route('/dept/<int:dept_id>/employees')
def dept_employees(dept_id):
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