import boto3
import base64

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket_name']
    nombre_directorio = event['body']['directory_name']
    nombre_archivo = event['body']['file_name']
    archivo_contenido = base64.b64decode(event['body']['file_content'])  # Suponiendo que el archivo está en base64
    
    # Crear la ruta completa (directorio/archivo)
    ruta_archivo = f"{nombre_directorio}/{nombre_archivo}"
    
    # Subir el archivo al bucket
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=ruta_archivo, Body=archivo_contenido)
    
    # Respuesta
    return {
        'statusCode': 200,
        'message': f"Archivo '{nombre_archivo}' subido a '{ruta_archivo}' en el bucket '{nombre_bucket}'"
    }
