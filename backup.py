import os
import boto3
import subprocess
from datetime import datetime

# Konfiguration
DATABASE_URL = os.environ.get('DATABASE_URL')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET', 'panpanparts-backup')
AWS_REGION = os.environ.get('AWS_REGION', 'eu-north-1')

def backup():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    filename = f'backup_{timestamp}.sql'
    
    print(f'Starter backup: {filename}')
    
    # Dump PostgreSQL
    result = subprocess.run(
        ['pg_dump', DATABASE_URL, '-f', filename],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        print('Fejl ved pg_dump:', result.stderr)
        return
    
    print('Database dumped!')
    
    # Upload til S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    
    s3.upload_file(filename, AWS_S3_BUCKET, f'backups/{filename}')
    print(f'Uploaded til S3: backups/{filename}')
    
    # Slet lokal fil
    os.remove(filename)
    print('Færdig!')

if __name__ == '__main__':
    backup()
