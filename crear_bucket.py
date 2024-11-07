import boto3

def lambda_handler(event, context):
    # Nombre del bucket desde el cuerpo de la solicitud
    nombre_bucket = event['body']['bucket_name']
    
    # Crear el bucket en S3
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)

    # Respuesta
    return {
        'statusCode': 200,
        'message': f"Bucket '{nombre_bucket}' creado exitosamente"
    }
