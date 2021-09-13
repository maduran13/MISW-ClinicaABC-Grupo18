# PoC 1: 
### Detección de fallas en la generación de reporte detallado a través de un componente Monitor


Buscamos validar la detección de fallas en el funcionamiento del componente de Reportes a través del componente Monitor que utiliza la estrategia Echo/Ping.  
  
    

![Diagrama PoC](https://user-images.githubusercontent.com/83253644/133001721-03ad018d-1550-4dde-835b-3400b93ef945.png)


  
#### Componentes

| Microservicio      | Propósito y comportamiento esperado | Tecnología Asociada |
| :---        |    :----:   |          ---: |
| Reportes      | Encargado de realizar consultas para la generación de reportes para usuarios Administrativos        | Python/ Flask   |
| Monitor   | Encargado de realizar el chequeo de salud del componente Reportes a través de un proceso de Ping/Echo        | Python/ Flask      |
| Notificador   | Encargado de enviar un correo electrónico a los interesados al momento que el componente monitor se lo indique         | Python/ Flask      |

  
    

### Run Reportes component
```
cd monitor
flask run
```

### Run Monitor component
```
cd monitor
flask run
```

### Run grafana
```
git clone https://github.com/ajeje93/grafana-mongodb-docker.git
cd grafana-mongodb-docker
docker-compose up -d
```
