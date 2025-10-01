"""
AWS Penetration Testing Lab Setup
Script untuk membuat vulnerable AWS environment untuk pembelajaran
"""

import json
import os

def create_vulnerable_s3_scenarios():
    """Membuat berbagai scenario S3 yang vulnerable"""
    scenarios = {
        "public_bucket_with_secrets": {
            "bucket_name": "company-secrets-public",
            "files": {
                "config/database.yml": """
production:
  host: db.internal.company.com
  username: root
  password: SuperSecret123!
  database: production_db
                """,
                "keys/api-keys.json": json.dumps({
                    "aws_access_key": "AKIAIOSFODNN7EXAMPLE",
                    "aws_secret_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                    "stripe_key": "sk_test_1234567890abcdef",
                    "sendgrid_key": "SG.1234567890.abcdef"
                }, indent=2),
                "backup/users.sql": """
INSERT INTO users (id, username, password_hash, email, role) VALUES
(1, 'admin', '$2b$12$xyz123', 'admin@company.com', 'administrator'),
(2, 'dbadmin', '$2b$12$abc456', 'db@company.com', 'database_admin'),
(3, 'johndoe', '$2b$12$def789', 'john@company.com', 'user');
                """,
                "logs/access.log": """
2024-01-15 10:30:15 - admin login successful from 192.168.1.100
2024-01-15 10:31:22 - admin accessed /admin/users
2024-01-15 10:32:45 - admin downloaded user_database.csv
2024-01-15 11:15:30 - root login successful from 10.0.0.5
2024-01-15 11:16:12 - root executed: SELECT * FROM credit_cards
                """
            },
            "policy": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "PublicReadGetObject",
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": "s3:GetObject",
                        "Resource": "arn:aws:s3:::company-secrets-public/*"
                    }
                ]
            }
        },
        
        "misconfigured_website_bucket": {
            "bucket_name": "company-website-backup",
            "files": {
                "index.html": """
<!DOCTYPE html>
<html>
<head><title>Company Internal Portal</title></head>
<body>
    <h1>Internal Company Portal</h1>
    <p>This should not be public!</p>
    <!-- TODO: Remove before going live -->
    <!-- Admin credentials: admin/TempPass123 -->
    <script>
        const API_KEY = 'sk-live-1234567890abcdef';
        const API_ENDPOINT = 'https://api.internal.company.com';
    </script>
</body>
</html>
                """,
                "wp-config.php": """
<?php
define('DB_NAME', 'company_wp');
define('DB_USER', 'wp_admin');
define('DB_PASSWORD', 'wp_SuperSecret456!');
define('DB_HOST', 'localhost');

define('AUTH_KEY',         'put your unique phrase here');
define('SECURE_AUTH_KEY',  'put your unique phrase here');
define('LOGGED_IN_KEY',    'put your unique phrase here');
define('NONCE_KEY',        'put your unique phrase here');

$table_prefix = 'wp_';
define('WP_DEBUG', true);
?>
                """,
                ".env": """
NODE_ENV=production
DATABASE_URL=postgresql://admin:secret123@db.company.com:5432/myapp
JWT_SECRET=my-super-secret-jwt-key-123456
STRIPE_SECRET_KEY=sk_live_abcdef1234567890
SENDGRID_API_KEY=SG.xyz123.abcdef456
                """
            }
        }
    }
    return scenarios

def create_vulnerable_iam_scenarios():
    """Membuat scenario IAM yang vulnerable"""
    scenarios = {
        "overprivileged_user": {
            "username": "intern-developer",
            "policies": [
                {
                    "PolicyName": "DeveloperAccess",
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": "*",
                                "Resource": "*"
                            }
                        ]
                    }
                }
            ]
        },
        
        "privilege_escalation_path": {
            "username": "limited-user",
            "policies": [
                {
                    "PolicyName": "LimitedButDangerous",
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": [
                                    "iam:CreateRole",
                                    "iam:AttachRolePolicy",
                                    "sts:AssumeRole",
                                    "iam:PassRole"
                                ],
                                "Resource": "*"
                            }
                        ]
                    }
                }
            ]
        },
        
        "cross_account_trust": {
            "rolename": "CrossAccountRole",
            "assume_role_policy": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": "*"
                        },
                        "Action": "sts:AssumeRole"
                    }
                ]
            }
        }
    }
    return scenarios

def create_vulnerable_lambda_functions():
    """Membuat Lambda functions yang vulnerable"""
    functions = {
        "command_injection_function": {
            "function_name": "vulnerable-cmd-executor",
            "runtime": "python3.9",
            "code": '''
import json
import subprocess
import os

def lambda_handler(event, context):
    """
    VULNERABLE FUNCTION - Multiple security issues:
    1. Command injection
    2. Information disclosure
    3. No input validation
    """
    
    # VULNERABILITY 1: Direct command execution
    command = event.get('cmd', 'whoami')
    
    try:
        # DANGEROUS: Shell=True allows command injection
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        
        # VULNERABILITY 2: Information disclosure
        response_data = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode,
            'environment_vars': dict(os.environ),  # Leaking all env vars
            'current_dir': os.getcwd(),
            'process_id': os.getpid()
        }
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # VULNERABILITY 3: CORS misconfiguration
                'Access-Control-Allow-Headers': '*'
            },
            'body': json.dumps(response_data, indent=2)
        }
        
    except subprocess.TimeoutExpired:
        return {
            'statusCode': 408,
            'body': json.dumps({'error': 'Command timeout'})
        }
    except Exception as e:
        # VULNERABILITY 4: Error information disclosure
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'error_type': type(e).__name__,
                'locals': str(locals())  # Leaking local variables
            })
        }
            ''',
            "environment_variables": {
                "DATABASE_PASSWORD": "SuperSecret123!",
                "API_KEY": "sk-vulnerable-api-key-12345",
                "JWT_SECRET": "jwt-secret-should-not-be-here",
                "ADMIN_PASSWORD": "admin123",
                "ENCRYPTION_KEY": "my-encryption-key-123"
            }
        },
        
        "ssrf_function": {
            "function_name": "vulnerable-url-fetcher",
            "runtime": "python3.9",
            "code": '''
import json
import urllib.request
import urllib.parse

def lambda_handler(event, context):
    """
    VULNERABLE FUNCTION - SSRF vulnerability
    Allows attackers to make requests to internal services
    """
    
    url = event.get('url', 'http://httpbin.org/get')
    
    try:
        # VULNERABILITY: No URL validation - allows SSRF
        with urllib.request.urlopen(url, timeout=10) as response:
            content = response.read().decode('utf-8')
            headers = dict(response.headers)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'url': url,
                'status_code': response.status,
                'headers': headers,
                'content': content[:1000]  # Limit content size
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'attempted_url': url
            })
        }
            '''
        },
        
        "deserialization_function": {
            "function_name": "vulnerable-data-processor",
            "runtime": "python3.9",
            "code": '''
import json
import pickle
import base64

def lambda_handler(event, context):
    """
    VULNERABLE FUNCTION - Insecure deserialization
    """
    
    data = event.get('data', '')
    format_type = event.get('format', 'json')
    
    try:
        if format_type == 'json':
            parsed_data = json.loads(data)
        elif format_type == 'pickle':
            # VULNERABILITY: Insecure deserialization
            decoded_data = base64.b64decode(data)
            parsed_data = pickle.loads(decoded_data)
        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Unsupported format'})
            }
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'parsed_data': str(parsed_data),
                'type': str(type(parsed_data))
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
            '''
        }
    }
    return functions

def create_vulnerable_dynamodb_scenarios():
    """Membuat DynamoDB scenarios yang vulnerable"""
    scenarios = {
        "users_table_with_secrets": {
            "table_name": "company-users",
            "key_schema": [
                {"AttributeName": "user_id", "KeyType": "HASH"}
            ],
            "attribute_definitions": [
                {"AttributeName": "user_id", "AttributeType": "S"}
            ],
            "sample_data": [
                {
                    "user_id": {"S": "admin"},
                    "username": {"S": "administrator"},
                    "password": {"S": "admin123"},  # Plain text password!
                    "role": {"S": "admin"},
                    "api_key": {"S": "sk-admin-key-vulnerable-123"},
                    "credit_card": {"S": "4532-1234-5678-9012"},
                    "ssn": {"S": "123-45-6789"}
                },
                {
                    "user_id": {"S": "john_doe"},
                    "username": {"S": "johndoe"},
                    "password": {"S": "password123"},
                    "role": {"S": "user"},
                    "personal_info": {"S": "Born 1985-03-15, Lives at 123 Main St"},
                    "salary": {"N": "75000"}
                },
                {
                    "user_id": {"S": "service_account"},
                    "username": {"S": "service"},
                    "password": {"S": "service_pass_2024"},
                    "role": {"S": "service"},
                    "database_connection": {"S": "postgresql://service:secret@db.internal:5432/prod"},
                    "encryption_keys": {"S": "aes_key:abc123def456, rsa_key:xyz789"}
                }
            ]
        },
        
        "sessions_table": {
            "table_name": "user-sessions",
            "key_schema": [
                {"AttributeName": "session_id", "KeyType": "HASH"}
            ],
            "attribute_definitions": [
                {"AttributeName": "session_id", "AttributeType": "S"}
            ],
            "sample_data": [
                {
                    "session_id": {"S": "sess_admin_123456"},
                    "user_id": {"S": "admin"},
                    "jwt_token": {"S": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ.signature"},
                    "permissions": {"SS": ["read", "write", "delete", "admin"]},
                    "last_activity": {"S": "2024-01-15T10:30:00Z"},
                    "ip_address": {"S": "192.168.1.100"}
                }
            ]
        }
    }
    return scenarios

def create_api_gateway_scenarios():
    """Membuat API Gateway scenarios yang vulnerable"""
    scenarios = {
        "insecure_api_endpoints": [
            {
                "path": "/api/users",
                "method": "GET",
                "vulnerability": "No authentication required",
                "description": "Returns all user data including sensitive information"
            },
            {
                "path": "/api/admin/users/{id}",
                "method": "DELETE",
                "vulnerability": "No authorization check",
                "description": "Any authenticated user can delete any user"
            },
            {
                "path": "/api/file/upload",
                "method": "POST",
                "vulnerability": "No file type validation",
                "description": "Allows upload of any file type including executables"
            },
            {
                "path": "/api/search",
                "method": "GET",
                "vulnerability": "SQL injection in query parameter",
                "description": "Search parameter is directly concatenated to SQL query"
            }
        ],
        
        "cors_misconfiguration": {
            "allowed_origins": ["*"],
            "allowed_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allowed_headers": ["*"],
            "vulnerability": "Wildcard CORS allows any domain to make requests"
        }
    }
    return scenarios

def generate_pentest_checklist():
    """Generate comprehensive penetration testing checklist"""
    checklist = {
        "reconnaissance": [
            "[ ] Enumerate all AWS services in scope",
            "[ ] Identify service versions and configurations",
            "[ ] Map out IAM users, roles, and policies",
            "[ ] Document resource relationships",
            "[ ] Check for publicly accessible resources"
        ],
        
        "s3_testing": [
            "[ ] Test for public read/write permissions",
            "[ ] Enumerate bucket names using wordlists",
            "[ ] Check for sensitive files in buckets",
            "[ ] Test bucket policy bypasses",
            "[ ] Verify encryption settings",
            "[ ] Check access logging configuration"
        ],
        
        "iam_testing": [
            "[ ] Map privilege escalation paths",
            "[ ] Test for overprivileged roles/users",
            "[ ] Check for wildcard permissions",
            "[ ] Test cross-account trust relationships",
            "[ ] Verify MFA requirements",
            "[ ] Check for unused/stale credentials"
        ],
        
        "lambda_testing": [
            "[ ] Review function code for vulnerabilities",
            "[ ] Test for command injection",
            "[ ] Check environment variables for secrets",
            "[ ] Test function triggers and permissions",
            "[ ] Verify network access restrictions",
            "[ ] Check for insecure dependencies"
        ],
        
        "dynamodb_testing": [
            "[ ] Test for NoSQL injection",
            "[ ] Check for over-broad read permissions",
            "[ ] Verify encryption at rest/transit",
            "[ ] Test backup and restore access",
            "[ ] Check for sensitive data in tables",
            "[ ] Verify access patterns"
        ],
        
        "api_gateway_testing": [
            "[ ] Test authentication bypass",
            "[ ] Check for CORS misconfigurations",
            "[ ] Test rate limiting bypass",
            "[ ] Verify input validation",
            "[ ] Test for path traversal",
            "[ ] Check error message disclosure"
        ],
        
        "documentation": [
            "[ ] Document all findings with evidence",
            "[ ] Classify vulnerabilities by severity",
            "[ ] Provide remediation recommendations",
            "[ ] Create executive summary",
            "[ ] Include technical details for developers",
            "[ ] Provide compliance gap analysis"
        ]
    }
    return checklist

def main():
    print("🔧 AWS Penetration Testing Lab Setup")
    print("====================================")
    
    scenarios = {
        "S3 Vulnerable Scenarios": create_vulnerable_s3_scenarios(),
        "IAM Vulnerable Scenarios": create_vulnerable_iam_scenarios(),
        "Lambda Vulnerable Functions": create_vulnerable_lambda_functions(),
        "DynamoDB Vulnerable Scenarios": create_vulnerable_dynamodb_scenarios(),
        "API Gateway Scenarios": create_api_gateway_scenarios(),
        "Penetration Testing Checklist": generate_pentest_checklist()
    }
    
    for category, data in scenarios.items():
        print(f"\n📋 {category}")
        if isinstance(data, dict):
            for key in data.keys():
                print(f"  - {key}")
        elif isinstance(data, list):
            print(f"  - {len(data)} items configured")
    
    print("\n✅ Lab scenarios ready!")
    print("⚠️  Remember: These are intentionally vulnerable for learning purposes!")
    print("🎯 Use with aws_pentest_toolkit.py to practice exploitation")

if __name__ == "__main__":
    main()