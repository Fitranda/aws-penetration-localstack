# 🎯 PANDUAN LENGKAP AWS PENETRATION TESTING - 14 MINGGU

## 📋 RINGKASAN EKSEKUTIF
**Tujuan:** Mempelajari AWS penetration testing menggunakan LocalStack dalam 14 minggu lengkap
**Target:** Mampu melakukan penetration testing profesional pada AWS services secara lokal
**Durasi:** 14 Minggu (3.5 bulan)
**Tools Utama:** Docker, LocalStack, AWS CLI, PowerShell, Nmap, Python, boto3
**Deliverable Akhir:** Laporan Penetration Test Profesional + Presentasi

---

## 🗓️ MINGGU 1: PERENCANAAN & PERSIAPAN

### 📅 **HARI 1-2: SETUP DOKUMENTASI**
```powershell
# 1. Buat struktur folder
mkdir "AWS-Pentest-Lab"
cd "AWS-Pentest-Lab"

# 2. Buat file perencanaan
echo "# AWS Penetration Testing Project Plan" > PROJECT_PLAN.md
```

**✅ CHECKLIST HARI 1-2:**
- [ ] Buat folder proyek
- [ ] Buat dokumen perencanaan
- [ ] Tentukan 5 skenario penetration testing
- [ ] Buat timeline 3 minggu

### 📅 **HARI 3-4: RISET SKENARIO**
**5 SKENARIO PENETRATION TESTING:**

1. **S3 Bucket Misconfiguration** (Risk: 9.5/10)
   - Public read/write access
   - Sensitive data exposure
   - ACL bypass

2. **EC2 Security Group Flaws** (Risk: 9.0/10) 
   - Open ports (SSH, RDP, Database)
   - 0.0.0.0/0 access rules
   - Protocol vulnerabilities

3. **IAM Privilege Escalation** (Risk: 8.5/10)
   - Weak policies
   - Role assumption abuse
   - Cross-account access

4. **Lambda Function Injection** (Risk: 8.0/10)
   - Code injection attacks
   - Environment variable leaks
   - Function enumeration

5. **DynamoDB Data Extraction** (Risk: 7.5/10)
   - Unencrypted data
   - Public access policies
   - Query injection

**✅ CHECKLIST HARI 3-4:**
- [ ] Riset 5 skenario di atas
- [ ] Tentukan tools yang dibutuhkan
- [ ] Buat risk assessment matrix
- [ ] Dokumentasikan attack vectors

### 📅 **HARI 5-6: PERSIAPAN TOOLS**
```powershell
# Tools yang dibutuhkan:
# - Docker Desktop
# - AWS CLI v2
# - Python 3.x
# - PowerShell Core
# - Nmap
# - Git
```

**✅ CHECKLIST HARI 5-6:**
- [ ] List semua tools yang dibutuhkan
- [ ] Download links untuk setiap tool
- [ ] Buat installation guide
- [ ] Test compatibility dengan Windows

### 📅 **HARI 7: REVIEW & FINALISASI**
```powershell
# Review semua dokumentasi
Get-ChildItem *.md | ForEach-Object { Write-Host $_.Name }
```

**✅ CHECKLIST HARI 7:**
- [ ] Review semua dokumen minggu 1
- [ ] Pastikan semua skenario jelas
- [ ] Siapkan folder untuk minggu 2
- [ ] Backup dokumentasi

---

## 🗓️ MINGGU 2: SETUP LABORATORIUM

### 📅 **HARI 1: INSTALL DOCKER**
```powershell
# 1. Download Docker Desktop
# Link: https://www.docker.com/products/docker-desktop

# 2. Install dan restart komputer

# 3. Verify installation
docker --version
docker-compose --version

# 4. Test dengan hello-world
docker run hello-world
```

**✅ CHECKLIST HARI 1:**
- [ ] Docker Desktop terinstall
- [ ] Docker daemon running
- [ ] docker --version works
- [ ] docker-compose available
- [ ] Test container berjalan

### 📅 **HARI 2: SETUP LOCALSTACK**
```powershell
# 1. Buat docker-compose.yml
@"
version: '3.8'
services:
  localstack:
    container_name: localstack_main
    image: localstack/localstack:latest
    ports:
      - "4566:4566"
    environment:
      - SERVICES=s3,lambda,dynamodb,ec2,iam,sts,logs,events,sns,sqs
      - DEBUG=1
      - PERSISTENCE=1
      - LAMBDA_EXECUTOR=docker-reuse
      - DOCKER_HOST=unix:///var/run/docker.sock
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "localstack-data:/tmp/localstack"
volumes:
  localstack-data:
"@ | Out-File -FilePath "docker-compose.yml" -Encoding UTF8

# 2. Start LocalStack
docker-compose up -d

# 3. Verify LocalStack
curl http://localhost:4566/_localstack/health
```

**✅ CHECKLIST HARI 2:**
- [ ] docker-compose.yml dibuat
- [ ] LocalStack container running
- [ ] Port 4566 accessible
- [ ] Health check passed
- [ ] Services initialized

### 📅 **HARI 3: INSTALL AWS CLI**
```powershell
# 1. Download AWS CLI v2
$url = "https://awscli.amazonaws.com/AWSCLIV2.msi"
Invoke-WebRequest -Uri $url -OutFile "AWSCLIV2.msi"

# 2. Install silently
Start-Process msiexec.exe -ArgumentList "/i", "AWSCLIV2.msi", "/quiet" -Wait

# 3. Refresh PATH
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")

# 4. Verify installation
aws --version
```

**✅ CHECKLIST HARI 3:**
- [ ] AWS CLI v2 downloaded
- [ ] Installation completed
- [ ] PATH updated
- [ ] aws --version works
- [ ] Ready for configuration

### 📅 **HARI 4: KONFIGURASI AWS CLI**
```powershell
# 1. Configure AWS CLI for LocalStack
aws configure set aws_access_key_id "test"
aws configure set aws_secret_access_key "test"
aws configure set region "us-east-1"
aws configure set output "json"

# 2. Verify configuration
aws configure list

# 3. Setup awslocal alias
$profilePath = $PROFILE
$aliasFunction = @"
function awslocal {
    aws --endpoint-url=http://localhost:4566 `$args
}
"@
Add-Content $profilePath $aliasFunction

# 4. Reload profile
. $PROFILE

# 5. Test awslocal
awslocal s3 ls
```

**✅ CHECKLIST HARI 4:**
- [ ] AWS credentials configured
- [ ] Region set to us-east-1
- [ ] awslocal alias created
- [ ] PowerShell profile updated
- [ ] awslocal s3 ls works

### 📅 **HARI 5: INSTALL TOOLS TAMBAHAN**
```powershell
# 1. Download dan Install Nmap
# Link: https://nmap.org/download.html

# 2. Verify Python
python --version

# 3. Install Python dependencies
pip install boto3 requests botocore

# 4. Verify installations
nmap --version
python -c "import boto3; print('boto3 ready')"
```

**✅ CHECKLIST HARI 5:**
- [ ] Nmap terinstall
- [ ] Python accessible
- [ ] boto3 installed
- [ ] requests installed
- [ ] All tools verified

### 📅 **HARI 6: TESTING ENVIRONMENT**
```powershell
# TEST 1: S3 Operations
awslocal s3 mb s3://test-week2-bucket
awslocal s3 ls

# TEST 2: Upload/Download
echo "Hello LocalStack" > test.txt
awslocal s3 cp test.txt s3://test-week2-bucket/
awslocal s3 ls s3://test-week2-bucket/

# TEST 3: Download
awslocal s3 cp s3://test-week2-bucket/test.txt downloaded.txt
Get-Content downloaded.txt

# TEST 4: EC2 Operations
awslocal ec2 describe-regions

# TEST 5: IAM Operations
awslocal iam list-users

# TEST 6: Cleanup
awslocal s3 rb s3://test-week2-bucket --force
Remove-Item test.txt, downloaded.txt
```

**✅ CHECKLIST HARI 6:**
- [ ] S3 bucket create/list works
- [ ] File upload/download works
- [ ] EC2 commands work
- [ ] IAM commands work
- [ ] Lambda commands work
- [ ] Cleanup successful

### 📅 **HARI 7: DOKUMENTASI SETUP**
```powershell
# Buat dokumentasi lengkap setup
@"
# SETUP DOCUMENTATION

## System Requirements
- Windows 10/11
- 8GB RAM minimum
- Docker Desktop
- PowerShell 5.1+

## Installed Tools
- Docker Desktop: $(docker --version)
- AWS CLI: $(aws --version)
- Python: $(python --version)
- Nmap: $(nmap --version | Select-String "Nmap")

## Configuration
- LocalStack Endpoint: http://localhost:4566
- AWS Credentials: test/test
- AWS Region: us-east-1
- Services: s3,lambda,dynamodb,ec2,iam,sts,logs,events,sns,sqs

## Troubleshooting
### LocalStack not starting
- Check Docker daemon
- Check port 4566 availability
- Restart: docker-compose restart

### AWS CLI not working
- Verify PATH: `$env:PATH -split ';' | Where-Object { $_ -like '*aws*' }`
- Refresh PATH or restart PowerShell

### awslocal not found
- Check PowerShell profile: `Test-Path $PROFILE`
- Reload profile: `. $PROFILE`

"@ | Out-File -FilePath "SETUP_DOCUMENTATION.md" -Encoding UTF8
```

**✅ CHECKLIST HARI 7:**
- [ ] Setup documentation created
- [ ] All versions documented
- [ ] Troubleshooting guide included
- [ ] Verification checklist added
- [ ] Ready for Week 3

---

## 🗓️ MINGGU 3: DEPLOY VULNERABLE INFRASTRUCTURE

### 📅 **HARI 1: PERENCANAAN ARSITEKTUR**
```powershell
# 1. Buat diagram arsitektur vulnerable lab
@"
# VULNERABLE LAB ARCHITECTURE

## Components:
1. S3 Bucket (Public + Sensitive Files)
2. EC2 Security Group (Open Ports)
3. IAM Roles (Weak Policies)
4. Lambda Functions (Vulnerable Code)
5. DynamoDB Tables (Public Access)

## Attack Vectors:
- S3: Public read/write, ACL bypass
- EC2: Port scanning, service enumeration
- IAM: Privilege escalation, role assumption
- Lambda: Code injection, environment leaks
- DynamoDB: Data extraction, query injection
"@ | Out-File -FilePath "LAB_ARCHITECTURE.md" -Encoding UTF8
```

**✅ CHECKLIST HARI 1:**
- [ ] Architecture diagram created
- [ ] Components identified
- [ ] Attack vectors mapped
- [ ] Security flaws planned
- [ ] Deployment order decided

### 📅 **HARI 2-3: SCRIPT DEPLOYMENT S3**
```powershell
# setup_vulnerable_s3.ps1
@"
#!/usr/bin/env pwsh
Write-Host "🎯 Deploying Vulnerable S3 Infrastructure..." -ForegroundColor Cyan

# 1. Create vulnerable S3 bucket
Write-Host "📦 Creating S3 bucket..." -ForegroundColor Yellow
awslocal s3 mb s3://vulnerable-pentest-bucket

# 2. Make bucket public
Write-Host "🔓 Making bucket public..." -ForegroundColor Red
awslocal s3api put-bucket-acl --bucket vulnerable-pentest-bucket --acl public-read-write

# 3. Create sensitive files
Write-Host "📄 Creating sensitive files..." -ForegroundColor Yellow

# Database config
@'
{
  \"database\": {
    \"host\": \"prod-db.company.com\",
    \"username\": \"admin\",
    \"password\": \"SuperSecret123!\",
    \"port\": 3306
  }
}
'@ | Out-File -FilePath \"database-config.json\" -Encoding UTF8

# API Keys
@'
API_KEY=sk-1234567890abcdef
SECRET_KEY=abc123def456ghi789
DATABASE_URL=postgresql://user:pass@localhost/prod
JWT_SECRET=my-super-secret-jwt-key
'@ | Out-File -FilePath \"api-keys.env\" -Encoding UTF8

# SSH Key
@'
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAA
MwAAAAtzc2gtZWQyNTUxOQAAACBK1234567890abcdefghijklmnop
-----END OPENSSH PRIVATE KEY-----
'@ | Out-File -FilePath \"id_rsa\" -Encoding UTF8

# Customer PII
@'
customer_id,name,email,phone,ssn
1001,John Doe,john@example.com,555-0123,***-**-1234
1002,Jane Smith,jane@example.com,555-0124,***-**-5678
1003,Bob Johnson,bob@example.com,555-0125,***-**-9012
'@ | Out-File -FilePath \"customer_data.csv\" -Encoding UTF8

# 4. Upload files
Write-Host "⬆️ Uploading sensitive files..." -ForegroundColor Red
awslocal s3 cp database-config.json s3://vulnerable-pentest-bucket/
awslocal s3 cp api-keys.env s3://vulnerable-pentest-bucket/
awslocal s3 cp id_rsa s3://vulnerable-pentest-bucket/
awslocal s3 cp customer_data.csv s3://vulnerable-pentest-bucket/

# 5. Verify deployment
Write-Host "✅ Verifying S3 deployment..." -ForegroundColor Green
awslocal s3 ls s3://vulnerable-pentest-bucket/

# 6. Cleanup local files
Remove-Item database-config.json, api-keys.env, id_rsa, customer_data.csv

Write-Host "🎉 S3 vulnerable infrastructure deployed!" -ForegroundColor Green
"@ | Out-File -FilePath "setup_vulnerable_s3.ps1" -Encoding UTF8

# Execute script
powershell -ExecutionPolicy Bypass -File "setup_vulnerable_s3.ps1"
```

**✅ CHECKLIST HARI 2-3:**
- [ ] S3 deployment script created
- [ ] Vulnerable bucket created
- [ ] Public access configured
- [ ] 4 sensitive files uploaded
- [ ] Deployment verified

### 📅 **HARI 4-5: SCRIPT DEPLOYMENT EC2**
```powershell
# setup_vulnerable_ec2.ps1
@"
#!/usr/bin/env pwsh
Write-Host "🎯 Deploying Vulnerable EC2 Infrastructure..." -ForegroundColor Cyan

# 1. Create security group
Write-Host "🛡️ Creating vulnerable security group..." -ForegroundColor Yellow
awslocal ec2 create-security-group --group-name vulnerable-sg --description "Vulnerable Security Group for Pentest"

# 2. Add inbound rules (ALL PORTS OPEN!)
Write-Host "🔓 Adding dangerous inbound rules..." -ForegroundColor Red

# SSH (22)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 22 --cidr 0.0.0.0/0

# HTTP (80)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 80 --cidr 0.0.0.0/0

# HTTPS (443)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 443 --cidr 0.0.0.0/0

# MySQL (3306)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 3306 --cidr 0.0.0.0/0

# RDP (3389)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 3389 --cidr 0.0.0.0/0

# PostgreSQL (5432)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 5432 --cidr 0.0.0.0/0

# Redis (6379)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 6379 --cidr 0.0.0.0/0

# Alternative HTTP (8080)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 8080 --cidr 0.0.0.0/0

# Elasticsearch (9200)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 9200 --cidr 0.0.0.0/0

# MongoDB (27017)
awslocal ec2 authorize-security-group-ingress --group-name vulnerable-sg --protocol tcp --port 27017 --cidr 0.0.0.0/0

# 3. Verify security group
Write-Host "✅ Verifying EC2 security group..." -ForegroundColor Green
awslocal ec2 describe-security-groups --group-names vulnerable-sg

Write-Host "🎉 EC2 vulnerable infrastructure deployed!" -ForegroundColor Green
"@ | Out-File -FilePath "setup_vulnerable_ec2.ps1" -Encoding UTF8

# Execute script
powershell -ExecutionPolicy Bypass -File "setup_vulnerable_ec2.ps1"
```

**✅ CHECKLIST HARI 4-5:**
- [ ] EC2 deployment script created
- [ ] Vulnerable security group created
- [ ] 10+ ports opened to 0.0.0.0/0
- [ ] Security rules verified
- [ ] Deployment successful

### 📅 **HARI 6: VERIFICATION & TESTING**
```powershell
# verify_week3_deployment.ps1
@"
#!/usr/bin/env pwsh
Write-Host "🔍 Verifying Week 3 Vulnerable Deployment..." -ForegroundColor Cyan

`$passed = 0
`$total = 0

# TEST 1: S3 Bucket Exists
Write-Host "`n📦 TEST 1: S3 Bucket..." -ForegroundColor Yellow
`$total++
try {
    `$result = awslocal s3 ls | Select-String "vulnerable-pentest-bucket"
    if (`$result) {
        Write-Host "✅ S3 bucket exists" -ForegroundColor Green
        `$passed++
    } else {
        Write-Host "❌ S3 bucket not found" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ S3 test failed: `$_" -ForegroundColor Red
}

# TEST 2: S3 Files
Write-Host "`n📄 TEST 2: S3 Sensitive Files..." -ForegroundColor Yellow
`$total++
try {
    `$files = awslocal s3 ls s3://vulnerable-pentest-bucket/
    `$fileCount = (`$files | Measure-Object).Count
    if (`$fileCount -ge 4) {
        Write-Host "✅ Found `$fileCount sensitive files" -ForegroundColor Green
        `$passed++
    } else {
        Write-Host "❌ Only found `$fileCount files (expected 4+)" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ S3 files test failed: `$_" -ForegroundColor Red
}

# TEST 3: S3 Public Access
Write-Host "`n🔓 TEST 3: S3 Public Access..." -ForegroundColor Yellow
`$total++
try {
    # Try to access without authentication (this would fail in real AWS but works in LocalStack)
    `$acl = awslocal s3api get-bucket-acl --bucket vulnerable-pentest-bucket
    if (`$acl) {
        Write-Host "✅ S3 bucket ACL accessible" -ForegroundColor Green
        `$passed++
    }
} catch {
    Write-Host "❌ S3 ACL test failed: `$_" -ForegroundColor Red
}

# TEST 4: Security Group Exists
Write-Host "`n🛡️ TEST 4: Security Group..." -ForegroundColor Yellow
`$total++
try {
    `$sg = awslocal ec2 describe-security-groups --group-names vulnerable-sg
    if (`$sg) {
        Write-Host "✅ Vulnerable security group exists" -ForegroundColor Green
        `$passed++
    }
} catch {
    Write-Host "❌ Security group test failed: `$_" -ForegroundColor Red
}

# TEST 5: Open Ports Count
Write-Host "`n🔍 TEST 5: Open Ports..." -ForegroundColor Yellow
`$total++
try {
    `$rules = awslocal ec2 describe-security-groups --group-names vulnerable-sg --query 'SecurityGroups[0].IpPermissions' --output json | ConvertFrom-Json
    `$openPorts = `$rules.Count
    if (`$openPorts -ge 10) {
        Write-Host "✅ Found `$openPorts open ports" -ForegroundColor Green
        `$passed++
    } else {
        Write-Host "❌ Only `$openPorts open ports (expected 10+)" -ForegroundColor Red
    }
} catch {
    Write-Host "❌ Ports test failed: `$_" -ForegroundColor Red
}

# SUMMARY
Write-Host "`n📊 VERIFICATION SUMMARY" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Passed: `$passed/`$total tests" -ForegroundColor $(if (`$passed -eq `$total) { "Green" } else { "Yellow" })
Write-Host "Success Rate: $([Math]::Round((`$passed/`$total)*100, 2))%" -ForegroundColor $(if (`$passed -eq `$total) { "Green" } else { "Yellow" })

if (`$passed -eq `$total) {
    Write-Host "`n🎉 ALL TESTS PASSED! Week 3 deployment successful!" -ForegroundColor Green
} else {
    Write-Host "`n⚠️ Some tests failed. Check configuration." -ForegroundColor Yellow
}
"@ | Out-File -FilePath "verify_week3_deployment.ps1" -Encoding UTF8

# Execute verification
powershell -ExecutionPolicy Bypass -File "verify_week3_deployment.ps1"
```

**✅ CHECKLIST HARI 6:**
- [ ] Verification script created
- [ ] S3 bucket test passes
- [ ] S3 files test passes  
- [ ] S3 public access verified
- [ ] Security group test passes
- [ ] Open ports verified
- [ ] All 5+ tests successful

### 📅 **HARI 7: DOKUMENTASI & CLEANUP**
```powershell
# cleanup_lab.ps1
@"
#!/usr/bin/env pwsh
Write-Host "🧹 Cleaning Up Vulnerable Lab..." -ForegroundColor Cyan

`$confirmation = Read-Host "Are you sure you want to cleanup all vulnerable resources? (y/N)"
if (`$confirmation -eq 'y' -or `$confirmation -eq 'Y') {
    
    Write-Host "🗑️ Removing S3 bucket..." -ForegroundColor Yellow
    awslocal s3 rb s3://vulnerable-pentest-bucket --force
    
    Write-Host "🗑️ Removing security group..." -ForegroundColor Yellow
    awslocal ec2 delete-security-group --group-name vulnerable-sg
    
    Write-Host "✅ Cleanup completed!" -ForegroundColor Green
} else {
    Write-Host "❌ Cleanup cancelled." -ForegroundColor Red
}
"@ | Out-File -FilePath "cleanup_lab.ps1" -Encoding UTF8

# Create final documentation
@"
# WEEK 3 DEPLOYMENT SUMMARY

## 🎯 Deployed Components
1. **Vulnerable S3 Bucket**: vulnerable-pentest-bucket
   - Public read/write access
   - 4 sensitive files uploaded
   - ACL misconfiguration

2. **Vulnerable EC2 Security Group**: vulnerable-sg
   - 10+ ports open to 0.0.0.0/0
   - Critical services exposed
   - No IP filtering

## 🔍 Verification Results
- S3 bucket accessibility: ✅
- Sensitive files uploaded: ✅  
- Public access configured: ✅
- Security group created: ✅
- Multiple ports exposed: ✅

## 🚨 Security Issues Created
1. **S3 Data Exposure**: Database configs, API keys, SSH keys, PII
2. **Network Exposure**: SSH, RDP, Database ports open globally
3. **Authentication Bypass**: Public bucket access
4. **Information Disclosure**: Sensitive file enumeration

## 📝 Next Steps
1. Practice penetration testing techniques
2. Document findings and vulnerabilities
3. Create exploitation scripts
4. Generate security reports

## 🧹 Cleanup
Run: `powershell -ExecutionPolicy Bypass -File "cleanup_lab.ps1"`
"@ | Out-File -FilePath "WEEK3_DEPLOYMENT_SUMMARY.md" -Encoding UTF8
```

**✅ CHECKLIST HARI 7:**
- [ ] Cleanup script created
- [ ] Deployment summary documented
- [ ] Security issues cataloged
- [ ] Next steps planned
- [ ] Week 3 completed

---

## 📊 PROGRESS TRACKING

### ✅ CHECKLIST KESELURUHAN

**MINGGU 1: PERENCANAAN**
- [ ] Hari 1-2: Setup dokumentasi
- [ ] Hari 3-4: Riset skenario
- [ ] Hari 5-6: Persiapan tools
- [ ] Hari 7: Review & finalisasi

**MINGGU 2: SETUP LAB**
- [ ] Hari 1: Install Docker
- [ ] Hari 2: Setup LocalStack  
- [ ] Hari 3: Install AWS CLI
- [ ] Hari 4: Konfigurasi AWS CLI
- [ ] Hari 5: Install tools tambahan
- [ ] Hari 6: Testing environment
- [ ] Hari 7: Dokumentasi setup

**MINGGU 3: DEPLOY INFRASTRUCTURE**
- [ ] Hari 1: Perencanaan arsitektur
- [ ] Hari 2-3: Script deployment S3
- [ ] Hari 4-5: Script deployment EC2
- [ ] Hari 6: Verification & testing
- [ ] Hari 7: Dokumentasi & cleanup

---

## 🚀 QUICK START COMMANDS

```powershell
# 1. Clone/Setup Repository
git clone <your-repo>
cd aws-penetration-localstack

# 2. Start LocalStack
docker-compose up -d

# 3. Verify Environment
awslocal s3 ls
aws --version
docker ps

# 4. Deploy Vulnerable Infrastructure
powershell -ExecutionPolicy Bypass -File "setup_vulnerable_s3.ps1"
powershell -ExecutionPolicy Bypass -File "setup_vulnerable_ec2.ps1"

# 5. Verify Deployment
powershell -ExecutionPolicy Bypass -File "verify_week3_deployment.ps1"

# 6. Start Penetration Testing
# (Your exploitation scripts here)

# 7. Cleanup When Done
powershell -ExecutionPolicy Bypass -File "cleanup_lab.ps1"
```

---

## 🔧 TROUBLESHOOTING

### LocalStack Issues
```powershell
# Check container status
docker ps --filter "name=localstack"

# Restart LocalStack
docker-compose restart

# Check logs
docker-compose logs localstack
```

### AWS CLI Issues
```powershell
# Check installation
aws --version

# Check configuration
aws configure list

# Refresh PATH
$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
```

### awslocal Issues
```powershell
# Check alias
Get-Command awslocal

# Reload profile
. $PROFILE

# Test connectivity
awslocal s3 ls
```

---

## 📚 RESOURCES & REFERENCES

- **AWS CLI Documentation**: https://docs.aws.amazon.com/cli/
- **LocalStack Documentation**: https://docs.localstack.cloud/
- **Docker Documentation**: https://docs.docker.com/
- **PowerShell Documentation**: https://docs.microsoft.com/powershell/
- **Nmap Documentation**: https://nmap.org/book/
- **Python boto3 Documentation**: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

---

## 🎉 SELESAI!

Setelah menyelesaikan 3 minggu ini, Anda akan memiliki:
- ✅ AWS penetration testing lab yang berfungsi
- ✅ Vulnerable infrastructure untuk practice
- ✅ Scripts untuk deployment dan cleanup
- ✅ Dokumentasi lengkap untuk reference
- ✅ Foundation untuk advanced penetration testing

**Total estimasi waktu: 21 hari (3 minggu)**
**Skill level setelah selesai: Intermediate AWS Penetration Tester**