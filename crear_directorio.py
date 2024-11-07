import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket_name']
    nombre_directorio = event['body']['directory_name']
    
    # Crear un "directorio" en S3 (en realidad, un prefijo vacío)
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=(nombre_directorio + '/'))
    
    # Respuesta
    return {
        'statusCode': 200,
        'message': f"Directorio '{nombre_directorio}' creado en el bucket '{nombre_bucket}'"
    }
