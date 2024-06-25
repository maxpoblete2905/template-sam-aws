# AWS Lambda Starter Function

Este proyecto es un punto de partida para una función AWS Lambda utilizando AWS Serverless Application Model (SAM).

## Descripción

Este proyecto crea una función Lambda simple en Python que interactúa con una tabla DynamoDB. La función se puede invocar a través de una API HTTP GET en la ruta `/hello`.

## Estructura de la Plantilla

La plantilla `template.yaml` define los siguientes recursos:

### helloworldpython

Este recurso es una función AWS Lambda con las siguientes propiedades:

- **Handler**: `app.lambda_handler`
- **Runtime**: `python3.8`
- **CodeUri**: `src/`
- **Description**: Una función Lambda de inicio.
- **MemorySize**: 128 MB
- **Timeout**: 3 segundos
- **Environment Variables**:
  - `TABLE_NAME`: Nombre de la tabla DynamoDB referenciada.
  - `REGION_NAME`: Región AWS donde se despliega la función.
- **Events**:
  - **helloWorldSAMAPI**:
    - **Type**: Api
    - **Properties**:
      - **Path**: `/hello`
      - **Method**: GET
- **Policies**:
  - **DynamoDBCrudPolicy**:
    - **TableName**: Nombre de la tabla DynamoDB referenciada.

### Table

Este recurso es una tabla DynamoDB con las siguientes propiedades:

- **PrimaryKey**:
  - **Name**: `greeting`
  - **Type**: `String`
- **ProvisionedThroughput**:
  - **ReadCapacityUnits**: 1
  - **WriteCapacityUnits**: 1

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de directorios y archivos:

- **src/app.py**: Contiene el código fuente de la función Lambda.
- **template.yaml**: Plantilla AWS SAM que define los recursos de la aplicación.

## Despliegue

Para desplegar esta aplicación utilizando AWS SAM, siga los siguientes pasos:

1. **Compilar la aplicación**:

   ```bash
   # crear un bucket S3
   aws s3 mb s3://my-bucket-sam-maxpo
   ```

2. **Desplegar la aplicación**:

   ```bash
    # Package Cloudformation

    aws cloudformation package --template-file template.yaml --s3-bucket my-bucket-sam-maxpo --output-template-file gen/template-generate.yaml

   ```

3. **Desplegar la aplicación**:

   ```bash
      #Deploy
      aws cloudformation deploy --template-file gen/template-generate.yaml --stack-name sam-app --capabilities CAPABILITY_IAM

   ```

   Siga las indicaciones para completar el despliegue.

## Uso

Una vez desplegada la aplicación, puede invocar la función Lambda accediendo a la URL proporcionada por el endpoint API Gateway. Por defecto, la función responde a solicitudes GET en la ruta `/hello`.

## Licencia

Este proyecto está bajo la licencia MIT. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.

```

```
