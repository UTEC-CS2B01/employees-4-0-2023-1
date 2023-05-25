## Structure Project - Microservice in Flask

### Mantenimiento de Empleados

app/

<ul>
    <li>`__init__.py`</li>
    <li>models.py</li>
    <li>controllers.py</li>
    <li>services.py</li>
</ul>
config/
<ul>
    <li>`__init__.py`</li>
    <li>default.py</li>
    <li>qa.py</li>
    <li>integration.py</li>
    <li>production.py</li>
</ul>

-- tests/

<ul>
    <li>`__init__.py`</li>
    <li>test_controllers.py</li>
</ul>

-- requerimientos.py

-- readme.md

-- run.py

# Test endpoints:

#### POST /employees

### success

```
    curl -F "first_name=Juan" -F "last_name=perez" -F "job_title=Reclutador" -F "selectDepartment=3cf975cb-ad8f-4e79-ac83-a9f4a0f466c9" -F "image=@cristiano.jpeg;type=image/jpeg" -X POST http://localhost:5004/employees
```

### failed

Request

```
    curl -F "job_title=Reclutador" -F "selectDepartment=3cf975cb-ad8f-4e79-ac83-a9f4a0f466c9" -F "image=@cristiano.jpeg;type=image/jpeg" -X POST http://localhost:5004/employees
```

Response

```
{
  "errors": [
    "first_name is required",
    "last_name is required"
  ],
  "message": "Error creating employee",
  "success": false
}
```

```
$ curl -X POST http://localhost:5004/employees
{
  "errors": [
    "first_name is required",
    "last_name is required",
    "job_title is required",
    "selectDepartment is required",
    "image is required"
  ],
  "message": "Error creating employee",
  "success": false
}
```

Tarea 24/05/2021
1.- Implementar los endpoints de departmentos (GET/POST/PATCH/DELETE)
2.- Implementar los endpoints de empleados (PATCH/DELETE)


3.- Agregar sus respectivos CURLS en el archivo README.md
4.- Tendran que crear un branch
git checkout -b feature/tarea-24-05-2021-<username de gitbhub>
git push

Esto forma parte de la evaluacion continua de laboratorio

##Tarea Renzo

#### Get/departments

curl -X GET http://localhost:5004/departments
    

#### POST/departments

  curl -F "name=Double" -F "short_name=D" -X POST http://localhost:5004/departments

#### Patch/Departaments

@app.route('/departments/<deparments/<id>', methods=['PATCH'])
    
curl -X PATCH -H "Content-Type: application/json" -d '{"name": "Nuevo nombre", "short_name": "NN"}'

http://localhost:5004/departments/2a0b0877-070c-4510-aBa2-cff3b3c110bd
    
{ "message": "Departamente editado correctamente" }
    
#### Delete/Departments

@app.route('/departments/<id>', methods=['DELETE'])
    
curl -X DELETE http://localhost:5004/departments/2a0b0877-070c-4510-aBa2-cff3b3c110bd
    
{ "message": "Departamente eliminado correctamente" }

#### Patch/Employees

@app.route('/employees/<id>', methods=['PATCH']) 
    
curl -F "first_name=Renzo" -F "last_name=Acervo" -F "new_job_title=Medico" -F "new_employee.department_id=2a0b0877-070c-4510-aBa2-cff3b3c110bd" 
-X PATCH http://localhost:5004/employees 
    
{ "message": "Empleado editado correctamente" }

#### Delete/Employees

@app.route('/employees/<employeeid>', methods=['DELETE'])

curl -X DELETE http://localhost:5004/employees/2a0b0877-070c-4510-aBa2-cff3b3c110bd

{ "message": "Empleado eliminado correctamente" }
