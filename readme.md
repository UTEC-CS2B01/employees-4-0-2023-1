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

## Arturo task

### GET /Departments

@app.route('/departments', methods=['GET'])

##### success

```
    curl -X GET http://localhost:5004/departments
```

### POST /Departments

@app.route('/departments', methods=['POST'])

##### success

```
  curl -F "name=Departamento de Ventas" -F "short_name=DV" -X POST http://localhost:5004/departments

  {
    "id": "3e65eddc-3d69-48a8-bf23-89b785ed3285",
    "message": "Department created successfully",
    "name": "Departamento de Ventas",
    "short_name": "DV",
    "success": true
  }
```

##### failed

curl -X POST http://localhost:5004/departments

```
  {
    "errors": [
      "name is required",
      "short_name is required"
    ],
    "message": "Error creating department",
    "success": false
  }
```

### PATCH /Departments

@app.route('/departments/\<id>', methods=['PATCH'])

##### success

curl -F "name=Departamento de Ventas patch" -F "short_name=DV_patch" -X PATCH http://localhost:5004/departments/3e65eddc-3d69-48a8-bf23-89b785ed3285

```
  {
    "message": "Departamento actualizado exitosamente"
  }
```

##### failed

curl -X PATCH http://localhost:5004/departments/1

```
  {
  "message": "Departamento no encontrado"
  }
```

### DELETE /Departments

@app.route('/departments/\<id>', methods=['DELETE'])

##### success

curl -X DELETE http://localhost:5004/departments/3e65eddc-3d69-48a8-bf23-89b785ed3285

```
  {
    "message": "Departamento eliminado exitosamente"
  }
```

##### failed

curl -X DELETE http://localhost:5004/departments/1

```
  {
  "message": "Departamento no encontrado"
  }
```

### PATCH /Employees

@app.route('/employees/\<id>', methods=['PATCH'])

##### success

curl -F "first_name=Arturo" -F "last_name=Magno" -F "job_title=Bioingeniero" -F "selectDepartment=812e31fc-53f4-4218-ba63-32229b9efc13" -X PATCH http://localhost:5004/employees/93554847-8619-4352-9e3e-f82d0d822da4

```
  {
    "message": "Empleado actualizado correctamente"
  }
```

##### failed

curl -F "first_name=Arturo" -F "last_name=Magno" -F "job_title=Bioingeniero" -F "selectDepartment=812e31fc-53f4-4218-ba63-32229b9efc13" -X PATCH http://localhost:5004/employees/1

```
  {
    "message": "Empleado no encontrado"
  }
```

### DELETE /Employees

@app.route('/employees/\<id>', methods=['DELETE'])

##### success

curl -X DELETE http://localhost:5004/employees/93554847-8619-4352-9e3e-f82d0d822da4

```
  {
    "message": "Empleado eliminado correctamente"
  }
```

##### failed

curl -X DELETE http://localhost:5004/employees/1

```
  {
    "message": "Empleado no encontrado"
  }
```

### Search EMPLOYEES

curl -X GET http://localhost:5004/employees/1

### Search DEPARTMENT

curl -X GET http://localhost:5004/departments/1

