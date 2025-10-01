#!/bin/bash

# Script untuk setup dan testing AWS LocalStack

echo "=== AWS LocalStack Setup Script ==="

# Function untuk check apakah LocalStack sudah running
check_localstack() {
    echo "Checking LocalStack status..."
    if curl -s http://localhost:4566/health > /dev/null; then
        echo "✅ LocalStack is running"
        return 0
    else
        echo "❌ LocalStack is not running"
        return 1
    fi
}

# Function untuk start LocalStack
start_localstack() {
    echo "Starting LocalStack..."
    docker-compose up -d
    
    # Wait for LocalStack to be ready
    echo "Waiting for LocalStack to be ready..."
    for i in {1..30}; do
        if check_localstack; then
            echo "✅ LocalStack is ready!"
            break
        fi
        echo "Waiting... (${i}/30)"
        sleep 2
    done
}

# Function untuk stop LocalStack
stop_localstack() {
    echo "Stopping LocalStack..."
    docker-compose down
}

# Function untuk reset LocalStack data
reset_localstack() {
    echo "Resetting LocalStack data..."
    docker-compose down
    rm -rf localstack_data
    echo "✅ Data reset complete"
}

# Function untuk test S3
test_s3() {
    echo "=== Testing S3 ==="
    
    # Create bucket
    echo "Creating S3 bucket..."
    aws --endpoint-url=http://localhost:4566 s3 mb s3://test-bucket-$(date +%s)
    
    # List buckets
    echo "Listing S3 buckets..."
    aws --endpoint-url=http://localhost:4566 s3 ls
}

# Function untuk test DynamoDB
test_dynamodb() {
    echo "=== Testing DynamoDB ==="
    
    # Create table
    echo "Creating DynamoDB table..."
    aws --endpoint-url=http://localhost:4566 dynamodb create-table \
        --table-name test-table-$(date +%s) \
        --attribute-definitions AttributeName=id,AttributeType=S \
        --key-schema AttributeName=id,KeyType=HASH \
        --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
    
    # List tables
    echo "Listing DynamoDB tables..."
    aws --endpoint-url=http://localhost:4566 dynamodb list-tables
}

# Function untuk test Lambda
test_lambda() {
    echo "=== Testing Lambda ==="
    
    # Create a simple Lambda function
    echo "Creating Lambda function..."
    
    # Create function code
    cat > /tmp/lambda_function.py << 'EOF'
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from LocalStack Lambda!'
    }
EOF
    
    # Zip the function
    cd /tmp && zip lambda_function.zip lambda_function.py
    
    # Create the function
    aws --endpoint-url=http://localhost:4566 lambda create-function \
        --function-name test-function \
        --runtime python3.9 \
        --role arn:aws:iam::123456789012:role/lambda-role \
        --handler lambda_function.lambda_handler \
        --zip-file fileb://lambda_function.zip
    
    # List functions
    echo "Listing Lambda functions..."
    aws --endpoint-url=http://localhost:4566 lambda list-functions
    
    # Cleanup
    rm -f /tmp/lambda_function.py /tmp/lambda_function.zip
}

# Main menu
case "$1" in
    "start")
        start_localstack
        ;;
    "stop")
        stop_localstack
        ;;
    "restart")
        stop_localstack
        start_localstack
        ;;
    "reset")
        reset_localstack
        ;;
    "status")
        check_localstack
        ;;
    "test")
        if check_localstack; then
            test_s3
            test_dynamodb
            test_lambda
        else
            echo "Please start LocalStack first: ./setup.sh start"
        fi
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|reset|status|test}"
        echo ""
        echo "Commands:"
        echo "  start   - Start LocalStack"
        echo "  stop    - Stop LocalStack"
        echo "  restart - Restart LocalStack"
        echo "  reset   - Reset all LocalStack data"
        echo "  status  - Check LocalStack status"
        echo "  test    - Run test commands"
        exit 1
        ;;
esac