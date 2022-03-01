def execute(db, models):
    dept1 = models.Department(name="Produto")
    dept2 = models.Department(name="Comercial")
    dept3 = models.Department(name="Marketing")


    db.session.add(dept1)
    db.session.add(dept2)
    db.session.add(dept3)



    e1 = models.Employee(name="Hamilton", department_id=2)
    e2 = models.Employee(name="Jorge", department_id=2)
    e3 = models.Employee(name="Vannys", department_id=2)
    e4 = models.Employee(name="Regis", department_id=3)
    e5 = models.Employee(name="Sabino", department_id=2)


    db.session.add(e1)
    db.session.add(e2)
    db.session.add(e3)
    db.session.add(e4)
    db.session.add(e5)


    d1 = models.Dependent(name="Gustavo", employee_id=1)

    d2 = models.Dependent(name="Francisco", employee_id=1)

    db.session.add(d1)
    db.session.add(d2)

    db.session.commit()