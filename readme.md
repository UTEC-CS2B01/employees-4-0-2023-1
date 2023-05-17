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

```
    #curl -F "first_name=Juan" -F "last_name=perez" -F "job_title=Reclutador" -F "selectDepartment=3cf975cb-ad8f-4e79-ac83-a9f4a0f466c9" -F "image=@cristiano.jpeg;type=image/jpeg" -X POST http://localhost:5004/employees
```
