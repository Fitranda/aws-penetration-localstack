# AWS LocalStack dengan Docker

Proyek ini menyediakan setup untuk menjalankan AWS LocalStack menggunakan Docker untuk development dan testing lokal.

## Prasyarat

- Docker Desktop terinstall dan berjalan
- Docker Compose
- AWS CLI (opsional, untuk testing)

## Cara Menjalankan

1. **Clone atau download project ini**

2. **Jalankan LocalStack**
   ```bash
   docker-compose up -d
   ```

3. **Verifikasi LocalStack berjalan**
   ```bash
   curl http://localhost:4566/health
   ```

4. **Stop LocalStack**
   ```bash
   docker-compose down
   ```

## Konfigurasi

### Environment Variables

Edit file `.env` untuk mengkustomisasi konfigurasi:

- `DEBUG`: Set ke 1 untuk enable debug logging
- `SERVICES`: Daftar layanan AWS yang ingin diaktifkan
- `LOCALSTACK_VOLUME_DIR`: Directory untuk menyimpan data persistent

### Layanan yang Tersedia

LocalStack mendukung berbagai layanan AWS:
- S3 (Simple Storage Service)
- Lambda
- DynamoDB
- API Gateway
- SQS (Simple Queue Service)
- SNS (Simple Notification Service)
- IAM (Identity and Access Management)
- CloudFormation
- EC2
- RDS
- CloudWatch
- Logs

## Testing dengan AWS CLI

1. **Configure AWS CLI untuk LocalStack**
   ```bash
   aws configure set aws_access_key_id test
   aws configure set aws_secret_access_key test
   aws configure set region us-east-1
   aws configure set output json
   ```

2. **Test S3**
   ```bash
   # Buat bucket
   aws --endpoint-url=http://localhost:4566 s3 mb s3://my-test-bucket
   
   # List buckets
   aws --endpoint-url=http://localhost:4566 s3 ls
   
   # Upload file
   aws --endpoint-url=http://localhost:4566 s3 cp test.txt s3://my-test-bucket/
   ```

3. **Test DynamoDB**
   ```bash
   # Buat table
   aws --endpoint-url=http://localhost:4566 dynamodb create-table \
     --table-name my-table \
     --attribute-definitions AttributeName=id,AttributeType=S \
     --key-schema AttributeName=id,KeyType=HASH \
     --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
   
   # List tables
   aws --endpoint-url=http://localhost:4566 dynamodb list-tables
   ```

## Web Interface

LocalStack menyediakan web interface di:
- Main endpoint: http://localhost:4566
- Health check: http://localhost:4566/health

## Troubleshooting

### Port sudah digunakan
Jika port 4566 sudah digunakan, edit `docker-compose.yml` dan ganti port:
```yaml
ports:
  - "127.0.0.1:4567:4566"  # Ganti 4567 dengan port yang tersedia
```

### Permission Issues (Linux/Mac)
Jika ada masalah permission dengan Docker socket:
```bash
sudo chmod 666 /var/run/docker.sock
```

### Data Persistence
Data akan disimpan di directory `./localstack_data`. Untuk reset semua data:
```bash
docker-compose down
rm -rf localstack_data
docker-compose up -d
```

## Contoh Scripts

### Python dengan boto3
```python
import boto3

# Setup client untuk LocalStack
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Buat bucket
s3_client.create_bucket(Bucket='my-python-bucket')

# List buckets
response = s3_client.list_buckets()
print(response['Buckets'])
```

### Node.js dengan AWS SDK
```javascript
const AWS = require('aws-sdk');

// Configure AWS SDK untuk LocalStack
AWS.config.update({
  accessKeyId: 'test',
  secretAccessKey: 'test',
  region: 'us-east-1'
});

const s3 = new AWS.S3({
  endpoint: 'http://localhost:4566',
  s3ForcePathStyle: true
});

// Buat bucket
s3.createBucket({ Bucket: 'my-node-bucket' }, (err, data) => {
  if (err) console.log(err);
  else console.log('Bucket created:', data);
});
```

## Resources

- [LocalStack Documentation](https://docs.localstack.cloud/)
- [LocalStack GitHub](https://github.com/localstack/localstack)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)