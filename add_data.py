from app import db, Department, Employee, Dependent

dept1 = Department(name="Produto")
dept2 = Department(name="Comercial")
dept3 = Department(name="Marketing")


db.session.add(dept1)
db.session.add(dept2)
db.session.add(dept3)



e1 = Employee(name="Hamilton", department_id=2)
e2 = Employee(name="Jorge", department_id=2)
e3 = Employee(name="Vannys", department_id=2)
e4 = Employee(name="Regis", department_id=3)
e5 = Employee(name="Sabino", department_id=2)


db.session.add(e1)
db.session.add(e2)
db.session.add(e3)
db.session.add(e4)
db.session.add(e5)


d1 = Dependent(name="Gustavo", employee_id=1)

d2 = Dependent(name="Francisco", employee_id=1)

db.session.add(d1)
db.session.add(d2)

db.session.commit()