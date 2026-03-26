import os
import boto3
import psycopg2
import gzip
from datetime import datetime

DATABASE_URL = os.environ.get('DATABASE_URL')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET', 'panpanparts-backup')
AWS_REGION = os.environ.get('AWS_REGION', 'eu-north-1')

def backup():
    if not DATABASE_URL:
        print('FEJL: DATABASE_URL mangler!')
        return

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    filename = f'backup_{timestamp}.sql.gz'

    print(f'Starter backup: {filename}')
    print(f'Database URL fundet: {DATABASE_URL[:30]}...')

    # Dump via psycopg2
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    tables = ['user', 'claimed_aircraft', 'aircraft_listing', 'part']
    
    with gzip.open(filename, 'wt') as f:
        for table in tables:
            try:
                cur.execute(f'SELECT * FROM "{table}"')
                rows = cur.fetchall()
                colnames = [desc[0] for desc in cur.description]
                f.write(f'-- Table: {table}\n')
                f.write(f'-- Columns: {colnames}\n')
                for row in rows:
                    f.write(str(row) + '\n')
                f.write(f'-- Rows: {len(rows)}\n\n')
                print(f'{table}: {len(rows)} rækker')
            except Exception as e:
                print(f'Fejl i {table}: {e}')

    cur.close()
    conn.close()

    # Upload til S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    s3.upload_file(filename, AWS_S3_BUCKET, f'backups/{filename}')
    print(f'Uploaded til S3: backups/{filename}')

    os.remove(filename)
    print('Færdig!')

if __name__ == '__main__':
    backup()
