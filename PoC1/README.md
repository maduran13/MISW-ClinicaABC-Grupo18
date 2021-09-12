# PoC 1: 
### Detección de fallas en la generación de reporte detallado a través de un componente Monitor


Buscamos validar la detección de fallas en el funcionamiento del componente de Reportes a través del componente Monitor que utiliza la estrategia Echo/Ping.  
  
    

![Diagrama PoC](https://drive.google.com/file/d/17xKYJS3mSZpDdahclNV2Gwjq3tXetxpC/view?usp=sharing)


  
#### Componentes

| Microservicio      | Propósito y comportamiento esperado | Tecnología Asociada |
| :---        |    :----:   |          ---: |
| Reportes      | Encargado de realizar consultas para la generación de reportes para usuarios Administrativos        | Python/ Flask   |
| Monitor   | Encargado de realizar el chequeo de salud del componente Reportes a través de un proceso de Ping/Echo        | Python/ Flask      |
| Notificador   | Encargado de enviar un correo electrónico a los interesados al momento que el componente monitor se lo indique         | Python/ Flask      |

Antes de iniciar, reemplazar la variable de entorno `MAILGUN_SECRET_KEY` en el archivo `.env` con el valor que está en el siguiente [link](https://uniandes-my.sharepoint.com/:w:/g/personal/as_santamaria_uniandes_edu_co/EWVbiOpATw5HuNX-JdiR1soB-eoXnQgxr3SlTZm3IWzPdA?e=zSvem2 )

IMPORTANTE: Porfavor entrar al link anterior con un correo uniandes.

### Run MongoDB database
```
cd monitor
docker-compose up
```
    

### Run Reportes component
```
cd reportes
flask run
```

### Run Notificador component
```
cd notificador
flask run -p 5001
```

### Run Monitor component
```
cd monitor
flask run -p 5002
```
