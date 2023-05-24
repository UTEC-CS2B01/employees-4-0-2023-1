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
