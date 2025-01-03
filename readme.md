# Stack for Django MongoDB by Andres Rojas



## ALB PORT 8000
- http://djangochdevelopalb-695091760.us-east-1.elb.amazonaws.com:8000/

## Dominio
- https://django-challenge-mongo.andres-rojas-l.live/swagger


## ⚙️ Correr proyecto con Docker

Creacion del .env a partir del .env-example


1. Asegúrate de haber configurado el archivo `.env` en la raíz del proyecto.

2. Construye las imágenes de Docker:
   ```bash
   docker-compose build
   ```

3. Inicia los contenedores:
   ```bash
   docker-compose up
   ```


## 🌐 Despliegue AWS

### Creación de ECR para imágenes Docker
![](images/deployment/creation_images_ecr.png)

### Ejecución exitosa de CodePipeline
![](images/aws/cluster_and_service_running_ecs_aws.png)

### Load Balancer activo
![](images/aws/creacion_load_balancer.png)

### Tarea ECS Fargate ejecutada exitosamente
![](images/aws/cluster_and_service_running_ecs_aws.png)

### CloudFormation ejecutado exitosamente
![](images/aws/cloudformation_success.png)

### Acceso al Load Balancer en el puerto 8000
![](images/aws/access_load_balancer_8000.png)


### Acceso al dominio
![](images/aws/domain_swagger.png)

### Test Success
![](images/require/test_success.png)


### Ejecucion comando que crea books
![](images/require/command_create_books.png)

### Mongo local books
![](images/require/mongo_local.png)

# Build Fargate

- Error windows push ecr
    - https://stackoverflow.com/questions/60807697/docker-login-error-storing-credentials-the-stub-received-bad-data
        - Remove file docker-credential-wincred.exe C:\Program Files\Docker\Docker\resources\bin
        - Remove "credStore""credsStore"C:\Users\PROFILE_NAME\.docker\config.json
            - C:\Users\andre\.docker
    - O:\AA-DOWNLOAD-D\resources\bin


docker build --no-cache -t django-mongo:v1 .

- Probar local
    - docker run -p 8000:8000 django-mongo:v1



## Consideraciones

- Como implemente el proyecto en una capa gratuita de mongo, esta conexion se cierra muy rapido.

