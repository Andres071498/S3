import boto3

# Configura tus credenciales de AWS
aws_access_key_id = 'AKIAR55OBMAJV2JBFCM6'
aws_secret_access_key = 'EEEEEEEE'
region_name = 'us-east-1'  # Cambia esto si tu bucket está en otra región

# Nombre del bucket y archivo
bucket_name = 'nombre-de-tu-bucket'
archivo_local = 'ruta/al/archivo.txt'
nombre_en_s3 = 'carpeta/archivo.txt'  # Ruta dentro del bucket

# Crear cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Subir archivo
try:
    s3.upload_file(archivo_local, bucket_name, nombre_en_s3)
    print("Archivo subido exitosamente.")
except Exception as e:
    print(f"Error al subir el archivo: {e}")
