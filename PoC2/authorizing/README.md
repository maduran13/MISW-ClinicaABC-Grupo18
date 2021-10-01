# Componente authorizing
El microservicio ofrece dos operaciones:

## Crear Usuario:

A partir de un json como se observa a continuación, permite crear un usuario en la base de datos asignada en el archivo __init__.py

```
{
    "name": "adur",
    "password": "Hola123",
    "role": 2
}
```
## Generar Token:
A partir de un json como se observa a continuación, permite generar un token de autenticación, tomando en cuenta que el usuario si existe y cuenta con la contraseña y el rol correctos.

```
{
    "name": "adur",
    "password": "Hola123",
    "role": 2
}
```

### Archivo postman_collection
Se anexa un archivo authorizing.postman_collection.json que se puede importar en postman con la colección de las operaciones del servicio.