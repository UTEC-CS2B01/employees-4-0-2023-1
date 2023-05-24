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

### Patch

```
@app.route('/employees/<employee_id>', methods=['PATCH'])

curl -F "first_name=Christian" -F "last_name=Frisancho" -F "job_title=Medico" -F "selectDepartment=3cf975cb-ad8f-4e79-ac83-a9f4a0f466c9" -X PATCH http://localhost:5004/employees/7bba1ceb-14ab-463c-a883-50ca5295c68a
{
"message": "Empleado cambiado exitosamente"
}
```

### Delete

@app.route('/employees/borrar', methods=['DELETE'])
curl -X DELETE http://localhost:5004/employees/12
{
"message": "Empleado eliminado exitosamente"
}

### POST

@app.route('/departments', methods=['POST'])
curl -F "name=Suite" -F "short_name=S" - F"employees=1" -X POST http://localhost:5004/departments
{
"message":"Departamento creado exitosamente"
}

### PATCH

@app.route('/departments/new', methods=['PATCH'])
curl -F "new_name=Suite Presidencial" -F "new_short_name=SP" -F "new_employees=2" -X PATCH http://localhost:5004/departments/3
{
"message":"Departamento actualizado correctamente"
}

### DELETE

@app.route('/departments/borrar', methods=['DELETE'])
curl -X DELETE http://localhost:5004/departments/3
{
"message":"Departamento eliminado correctamente"
}
### Prueba