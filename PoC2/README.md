# PoC 2: 
### Rastreo de registros sobre validación de roles por medio de generación de tokens JWT

Se busca validar el rol de un funcionario para autorizar su acceso a la información de un servicio específico de la clínica.

#### Componentes

| Microservicio      | Propósito y comportamiento esperado | Tecnología Asociada |
| :---        |    :----:   |          :--- |
| Authorizing      |  Encargado de crear usuario con contraseña y rol respectivo en base de datos, y encargado de generar token de acuerdo al nombre, contraseña y rol del usuario. Además, encargado de validar token y crear registros de las validaciones exitosas y fallidas.        | Python/ Flask   |
| HistoriasClinicas   | Encargado de validar si el usuario que desea consultar el servicio cuenta con permisos y devolver la información del servicio.         | Python/ Flask      |
| API Gateway | Encargado de enrutar las peticiones que lleguen al sistema y redireccione al microservicio requerido.       | Python/ Flask      |

## Puesta a punto de Ambiente para prueba

A continuación se especifica el paso a paso necesario para adecuar el ambiente de la prueba de concepto.

Establecer mongoDB en contenedor en ambiente Docker Desktop.
### Configurar Docker en el computador local:
#### Windows
Para configurar el docker desktop en windows es necesario seguir el siguiente paso a paso que provee docker.

[Instalación Docker Windows](https://docs.docker.com/desktop/windows/install/)

#### Otros Sistemas operativos
Para la configuración de docker en otros sistemas operativos se provee el siguiente enlace con los pasos a seguir, construido en docker docs.

[Instalación Docker](https://docs.docker.com/engine/install/)

### Construcción de Contenedor MongoDB en docker local:
```
docker-compose up
```

## Run install dependencies 
```
pip install -r authorizing/requirements.txt
pip install -r historiasCLinicas/requirements.txt
pip install -r gateway/requirements.txt

```
## Run authorizing component
```
cd authorizing
flask run -p 5001
```

## Run Historias Clinicas component
```
cd historiasCLinicas
flask run -p 5002
```

## Run Gateway component
```
cd gateway
flask run -p 5000
```
