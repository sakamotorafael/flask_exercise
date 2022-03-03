import json
from app import create_app

from models.Department import Department

app = create_app()

def assembleDeptsJson():
    query = Department.query.all()
    result = []
    for dept in query:
        result.append({
            "id": dept.id,
            "name": dept.name
        })

    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )


def assembleEmployeesJson(dept_id: int):
    dept = Department.query.get(dept_id)

    if(dept == None):
        response = app.response_class(
            response=json.dumps("Department {} not found!".format(dept_id)),
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
