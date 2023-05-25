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
## PATCH
@app.route('/employees/<employee_id>', methods=['PATCH'])

curl -F "first_name=Christian" -F "last_name=Frisancho" -F "job_title=Medico" -F "selectDepartment=3cf975cb-ad8f-4e79-ac83-a9f4a0f466c9" -F "image=cristiano.jpg" -X PATCH http://localhost:5004/employees/7bba1ceb-14ab-463c-a883-50ca5295c68a
{
"message": "Empleado cambiado exitosamente"
}
## DELETE
@app.route('/employees/<employee_id>', methods=['DELETE']) 
curl -X DELETE http://localhost:5004/employees/7bba3ceb-14ba-463c-a883-50ca5395c68a { "message": "Empleado eliminado exitosamente" }
## POST
@app.route('/departments', methods=['POST']) 
curl -F "name=Suite" -F "short_name=S" - F"employees=7bba3ceb-14ba-463c-a883-50ca5395c68a" -X POST http://localhost:5004/departments { "message":"Departamento creado exitosamente" }
## PATCH
@app.route('/departments/<department_id>', methods=['PATCH']) 
curl -F "name=Suite_Presidencial" -F "short_name=SP" -F "employees=7bcb3ceb-07ba-473c-a883-50ca5395c68a" -X PATCH http://localhost:5004/departments/4bca6bec-25ab-483c-a983-50ca7391c68a { "message":"Departamento actualizado correctamente" }
## DELETE 
@app.route('/departments/<department_id>', methods=['DELETE']) 
curl -X DELETE http://localhost:5004/departments/4bca6bec-25ab-483c-a983-50ca7391c68a { "message":"Departamento eliminado correctamente" }

## SEARCH
curl -X GET "http://localhost:5004/employees/keyword?keyword=Christian"

## SEARCH
curl -X GET "http://localhost:5004/departments/keyword?keyword=S"


### Tarea 1 - 24/05/2023

- Implementar los endpoints de departmentos (GET/POST/PATCH/DELETE)

- Implementar los endpoints de empleados (PATCH/DELETE)
- Agregar sus respectivos CURLS en el archivo README.md
- Tendran que crear un branch
- git checkout -b feature/tarea-24-05-2023-<username>
- git push

Esto forma parte de la evaluacion continua de laboratorio

| Nombre                            | Usuario       | Nota |
| --------------------------------- | ------------- | ---- |
| Christian Maxim Frisancho Mayorga | CHRISTIANUTEC | 05   |
| Rohan Kumar Punjabi               | rkumar-lab    | 03   |
| Arturo Magno Barrantes Chuquimia  | arturombc     | 18   |

### Tarea 2 - 25/05/2023

- Implementar endpoint search de empleados, departamentos
- Van a investigar la libreria unittest
