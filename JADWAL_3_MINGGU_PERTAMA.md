# 📅 AWS Penetration Testing - Jadwal 3 Minggu Pertama

## 🎯 Overview 3 Minggu Pertama

```
MINGGU 1: Perencanaan Proyek
MINGGU 2: Persiapan Laboratorium  
MINGGU 3: Pembangunan Arsitektur Dasar
```

---

## 📋 MINGGU KE-1: PERENCANAAN PROYEK

### **Tujuan Utama**
Mendefinisikan ruang lingkup, tujuan, dan jadwal penetration testing serta mengidentifikasi tools yang akan digunakan.

### **Aktivitas Detail**

#### **Hari 1-2: Definisi Proyek**
```markdown
✅ TASKS:
1. Buat dokumen ruang lingkup proyek
2. Definisikan 5 skenario target penetration test
3. Tentukan kriteria sukses untuk setiap skenario
4. Identifikasi stakeholder dan audience laporan

📝 OUTPUT:
- Project Scope Document (1-2 halaman)
```

#### **Hari 3-4: Identifikasi Tools**
```markdown
✅ TOOLS YANG AKAN DIGUNAKAN:

🔧 Infrastructure:
- Docker & Docker Compose (Container environment)
- LocalStack (AWS simulation)

⚙️ AWS Tools:
- AWS CLI (Command line interface)
- boto3 (Python AWS SDK)

🔍 Security Tools:
- Nmap (Network scanner)
- Python scripts (Custom automation)
- Burp Suite Community (Web testing - optional)

📝 OUTPUT:
- Daftar tools dengan versi dan link instalasi
```

#### **Hari 5-6: Perencanaan Skenario**
```markdown
✅ 5 SKENARIO TARGET:

1. 🪣 S3 Bucket Publik
   - Vulnerability: Public read/write access
   - Impact: Data exposure & data tampering
   
2. 🔓 Security Group Terbuka  
   - Vulnerability: Open management ports
   - Impact: Unauthorized system access
   
3. 👤 IAM Privilege Escalation
   - Vulnerability: Weak IAM permissions
   - Impact: Admin access from limited user
   
4. 🌐 SSRF pada EC2
   - Vulnerability: Server-Side Request Forgery
   - Impact: Credential theft via metadata service
   
5. 🚶 Lateral Movement
   - Vulnerability: Network segmentation bypass
   - Impact: Access to private resources

📝 OUTPUT:
- Skenario matrix dengan risk rating
```

#### **Hari 7: Finalisasi Dokumen**
```markdown
✅ DELIVERABLES:

📄 Dokumen Perencanaan Proyek harus berisi:
- Executive Summary
- Project Objectives
- Scope & Limitations  
- 5 Target Scenarios (detailed)
- Tools & Technologies
- Timeline (14 weeks overview)
- Success Criteria
- Risk Assessment

📝 FORMAT:
- PDF professional format
- 1-2 halaman (concise)
```

### **Target Minggu 1**
```
✅ Dokumen Perencanaan Proyek (1-2 halaman)
✅ 5 Skenario penetration test terdefinisi dengan jelas
✅ Daftar tools lengkap dengan alasan pemilihan
✅ Timeline high-level 14 minggu
```

---

## 🛠️ MINGGU KE-2: PERSIAPAN LABORATORIUM

### **Tujuan Utama**
Setup dan konfigurasi complete testing environment dengan LocalStack dan tools pendukung.

### **Aktivitas Detail**

#### **Hari 1: Instalasi Docker**
```powershell
# Windows PowerShell Commands

# 1. Download Docker Desktop
# Link: https://www.docker.com/products/docker-desktop

# 2. Install Docker Desktop
# Follow installation wizard

# 3. Verify Installation
docker --version
docker-compose --version

# 4. Test Docker
docker run hello-world

# ✅ Expected Output: "Hello from Docker!"
```

```markdown
📝 CHECKLIST:
✅ Docker Desktop installed
✅ Docker version 20.10+
✅ Docker Compose version 2.0+
✅ WSL2 enabled (for Windows)
✅ Hello-world container runs successfully
```

#### **Hari 2: Instalasi LocalStack**
```powershell
# Sudah ada di project kita!
# File: docker-compose.yml

# 1. Navigate to project directory
cd "D:\Tugass\Semester 7 Kuliah\Cyber Security"

# 2. Start LocalStack
docker-compose up -d

# 3. Verify LocalStack is running
docker ps
# Should show: localstack_main container

# 4. Check LocalStack health
docker logs localstack_main --tail 20

# ✅ Expected: No errors, services started
```

```markdown
📝 VERIFICATION:
✅ LocalStack container running
✅ Port 4566 accessible
✅ Services initialized (S3, EC2, IAM, etc.)
```

#### **Hari 3: Instalasi AWS CLI**
```powershell
# Windows Installation

# 1. Download AWS CLI v2
# Link: https://awscli.amazonaws.com/AWSCLIV2.msi

# 2. Install dengan wizard

# 3. Verify Installation
aws --version
# Expected: aws-cli/2.x.x

# 4. Configure AWS CLI untuk LocalStack
aws configure
# AWS Access Key ID: test
# AWS Secret Access Key: test  
# Default region name: us-east-1
# Default output format: json
```

```markdown
📝 CHECKLIST:
✅ AWS CLI v2 installed
✅ AWS configured with test credentials
✅ Can execute: aws --version
```

#### **Hari 4: Setup awslocal Alias**
```powershell
# Create PowerShell Profile if not exists
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}

# Add awslocal function to profile
Add-Content $PROFILE @"

# LocalStack AWS Alias
function awslocal {
    aws --endpoint-url=http://localhost:4566 `$args
}
"@

# Reload profile
. $PROFILE

# Test awslocal
awslocal s3 ls
# Should return empty or existing buckets
```

```markdown
📝 VERIFICATION:
✅ awslocal command works
✅ Can list S3 buckets: awslocal s3 ls
✅ No authentication errors
```

#### **Hari 5: Instalasi Tools Tambahan**
```powershell
# 1. Install Nmap
# Download dari: https://nmap.org/download.html
# Install with default options

# Verify
nmap --version

# 2. Verify Python & pip (should already installed)
python --version  # Should be 3.12.0
pip --version

# 3. Install Python dependencies (sudah ada!)
pip install boto3 requests

# 4. Install optional tools
pip install awscli-local  # Alternative to alias
```

```markdown
📝 CHECKLIST:
✅ Nmap installed (version 7.9+)
✅ Python 3.7+ available
✅ boto3 and requests installed
✅ All tools accessible from command line
```

#### **Hari 6: Testing Environment**
```powershell
# Test 1: Create S3 Bucket
awslocal s3 mb s3://test-week2-bucket

# Test 2: List Buckets
awslocal s3 ls
# Should show: test-week2-bucket

# Test 3: Upload File
echo "Hello LocalStack" > test.txt
awslocal s3 cp test.txt s3://test-week2-bucket/

# Test 4: List Objects
awslocal s3 ls s3://test-week2-bucket/
# Should show: test.txt

# Test 5: Download File
awslocal s3 cp s3://test-week2-bucket/test.txt downloaded.txt

# Test 6: Delete Resources (cleanup)
awslocal s3 rb s3://test-week2-bucket --force
```

```markdown
📝 VERIFICATION TESTS:
✅ Can create S3 bucket
✅ Can upload files to S3
✅ Can list S3 objects
✅ Can download from S3
✅ Can delete S3 resources
```

#### **Hari 7: Dokumentasi Setup**
```markdown
📝 CREATE: SETUP_DOCUMENTATION.md

Content should include:
1. System Requirements
   - OS: Windows 10/11
   - RAM: 8GB minimum
   - Disk: 20GB free space
   
2. Installed Tools & Versions
   - Docker Desktop: X.X.X
   - LocalStack: latest
   - AWS CLI: 2.X.X
   - Nmap: 7.X
   - Python: 3.12.0
   
3. Configuration Details
   - LocalStack endpoint: http://localhost:4566
   - AWS credentials: test/test
   - Region: us-east-1
   
4. Troubleshooting Guide
   - Common errors and solutions
   - How to restart LocalStack
   - How to clean up resources
   
5. Verification Checklist
   - All tests from Day 6 documented
```

### **Target Minggu 2**
```
✅ LocalStack environment fully functional
✅ All tools installed and configured
✅ awslocal alias working
✅ Successful test: Create & delete S3 bucket
✅ Documentation complete with troubleshooting guide
```

---

## 🏗️ MINGGU KE-3: PEMBANGUNAN ARSITEKTUR DASAR

### **Tujuan Utama**
Deploy arsitektur dasar AWS (S3 dan EC2) dengan konfigurasi yang **sengaja dibuat rentan** untuk penetration testing.

### **Aktivitas Detail**

#### **Hari 1: Perencanaan Arsitektur**
```markdown
📐 ARCHITECTURE DESIGN:

1. S3 Infrastructure:
   ├── Public Bucket (vulnerable)
   │   ├── Sensitive files
   │   └── Public read/write policy
   └── Private Bucket (secure - for comparison)

2. EC2 Infrastructure:
   ├── Web Server Instance
   │   ├── Security Group: 0.0.0.0/0 (vulnerable)
   │   ├── Open ports: 22, 80, 443, 3389
   │   └── SSH keys accessible
   └── Database Server Instance (for week 9-10)

📝 OUTPUT:
- Architecture diagram (draw.io or ASCII)
- Infrastructure as Code plan
```

#### **Hari 2-3: Setup Vulnerable S3**
```powershell
# File: setup_vulnerable_s3.ps1

# 1. Create vulnerable S3 bucket
awslocal s3 mb s3://vulnerable-company-backup

# 2. Upload sensitive test files
@"
username: admin
password: Admin123!
database: production_db
host: db.internal.company.com
"@ | Out-File -FilePath database-config.txt -Encoding UTF8

awslocal s3 cp database-config.txt s3://vulnerable-company-backup/config/

@"
API_KEY=sk-live-123456789abcdef
SECRET_KEY=secret_xyz789abc
AWS_ACCESS_KEY=AKIAIOSFODNN7EXAMPLE
"@ | Out-File -FilePath api-keys.env -Encoding UTF8

awslocal s3 cp api-keys.env s3://vulnerable-company-backup/secrets/

# 3. Create public bucket policy
$publicPolicy = @"
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::vulnerable-company-backup",
        "arn:aws:s3:::vulnerable-company-backup/*"
      ]
    }
  ]
}
"@

$publicPolicy | Out-File -FilePath public-policy.json -Encoding UTF8
awslocal s3api put-bucket-policy --bucket vulnerable-company-backup --policy file://public-policy.json

# 4. Verify vulnerability
awslocal s3 ls s3://vulnerable-company-backup/ --recursive
# Should show all files

# 5. Test anonymous access (simulate attacker)
awslocal s3 ls s3://vulnerable-company-backup/ --no-sign-request
# Should still work! (This is the vulnerability)
```

```markdown
📝 VERIFICATION:
✅ Bucket created: vulnerable-company-backup
✅ Sensitive files uploaded
✅ Public policy applied
✅ Anonymous access confirmed working
```

#### **Hari 4-5: Setup Vulnerable EC2**
```powershell
# File: setup_vulnerable_ec2.ps1

# 1. Create vulnerable Security Group
awslocal ec2 create-security-group `
    --group-name vulnerable-web-sg `
    --description "Intentionally vulnerable security group for testing"

# 2. Add overly permissive rules
# Allow SSH from anywhere
awslocal ec2 authorize-security-group-ingress `
    --group-name vulnerable-web-sg `
    --protocol tcp `
    --port 22 `
    --cidr 0.0.0.0/0

# Allow HTTP from anywhere
awslocal ec2 authorize-security-group-ingress `
    --group-name vulnerable-web-sg `
    --protocol tcp `
    --port 80 `
    --cidr 0.0.0.0/0

# Allow HTTPS from anywhere  
awslocal ec2 authorize-security-group-ingress `
    --group-name vulnerable-web-sg `
    --protocol tcp `
    --port 443 `
    --cidr 0.0.0.0/0

# Allow RDP from anywhere (Windows)
awslocal ec2 authorize-security-group-ingress `
    --group-name vulnerable-web-sg `
    --protocol tcp `
    --port 3389 `
    --cidr 0.0.0.0/0

# Allow MySQL from anywhere
awslocal ec2 authorize-security-group-ingress `
    --group-name vulnerable-web-sg `
    --protocol tcp `
    --port 3306 `
    --cidr 0.0.0.0/0

# 3. Create EC2 key pair
awslocal ec2 create-key-pair `
    --key-name vulnerable-web-key `
    --query 'KeyMaterial' `
    --output text | Out-File -FilePath vulnerable-web-key.pem

# 4. Launch EC2 instance
awslocal ec2 run-instances `
    --image-id ami-12345678 `
    --instance-type t2.micro `
    --key-name vulnerable-web-key `
    --security-groups vulnerable-web-sg `
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Vulnerable-Web-Server}]'

# 5. Get instance details
awslocal ec2 describe-instances `
    --filters "Name=tag:Name,Values=Vulnerable-Web-Server" `
    --query 'Reservations[0].Instances[0].{ID:InstanceId,IP:PrivateIpAddress,State:State.Name}'
```

```markdown
📝 VERIFICATION:
✅ Security group created with open rules
✅ All dangerous ports open (22, 80, 443, 3306, 3389)
✅ Rules allow 0.0.0.0/0 (anywhere)
✅ EC2 instance launched
✅ SSH key generated and saved
```

#### **Hari 6: Create Automation Scripts**
```powershell
# File: deploy_vulnerable_lab.ps1

<#
.SYNOPSIS
Deploy complete vulnerable AWS environment for penetration testing

.DESCRIPTION
This script deploys:
1. Vulnerable S3 buckets with sensitive data
2. EC2 instances with open security groups
3. Test data for exploitation scenarios

.EXAMPLE
.\deploy_vulnerable_lab.ps1
#>

Write-Host "🚀 Deploying Vulnerable AWS Lab Environment..." -ForegroundColor Cyan

# Check LocalStack is running
Write-Host "📋 Checking LocalStack status..."
$localstackRunning = docker ps --filter "name=localstack_main" --format "{{.Status}}"
if (-not $localstackRunning) {
    Write-Host "❌ LocalStack is not running. Starting..." -ForegroundColor Red
    docker-compose up -d
    Start-Sleep -Seconds 10
}
Write-Host "✅ LocalStack is running" -ForegroundColor Green

# Deploy S3 vulnerable infrastructure
Write-Host "`n📦 Deploying S3 Infrastructure..."
& "$PSScriptRoot\setup_vulnerable_s3.ps1"
Write-Host "✅ S3 buckets deployed" -ForegroundColor Green

# Deploy EC2 vulnerable infrastructure  
Write-Host "`n🖥️  Deploying EC2 Infrastructure..."
& "$PSScriptRoot\setup_vulnerable_ec2.ps1"
Write-Host "✅ EC2 instances deployed" -ForegroundColor Green

# Summary
Write-Host "`n" + "="*50 -ForegroundColor Cyan
Write-Host "🎉 Vulnerable Lab Deployment Complete!" -ForegroundColor Green
Write-Host "="*50 -ForegroundColor Cyan

Write-Host "`n📊 Deployed Resources:"
Write-Host "  🪣 S3 Buckets:" -ForegroundColor Yellow
awslocal s3 ls

Write-Host "`n  🔓 Security Groups:" -ForegroundColor Yellow  
awslocal ec2 describe-security-groups --query 'SecurityGroups[*].[GroupName,GroupId]' --output table

Write-Host "`n  🖥️  EC2 Instances:" -ForegroundColor Yellow
awslocal ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,Tags[?Key==`Name`].Value|[0]]' --output table

Write-Host "`n⚠️  REMEMBER: This is an intentionally vulnerable environment!" -ForegroundColor Red
Write-Host "   Use only for authorized penetration testing learning." -ForegroundColor Red
```

```powershell
# File: cleanup_lab.ps1

<#
.SYNOPSIS
Clean up all vulnerable lab resources

.DESCRIPTION
Removes all S3 buckets, EC2 instances, and security groups created for the lab
#>

Write-Host "🧹 Cleaning up Vulnerable Lab Environment..." -ForegroundColor Cyan

# Terminate EC2 instances
Write-Host "`n🖥️  Terminating EC2 instances..."
$instances = awslocal ec2 describe-instances --query 'Reservations[*].Instances[*].InstanceId' --output text
if ($instances) {
    awslocal ec2 terminate-instances --instance-ids $instances
    Write-Host "✅ EC2 instances terminated" -ForegroundColor Green
}

# Delete S3 buckets
Write-Host "`n📦 Deleting S3 buckets..."
$buckets = awslocal s3 ls | ForEach-Object { $_.Split()[2] }
foreach ($bucket in $buckets) {
    awslocal s3 rb s3://$bucket --force
    Write-Host "  ✅ Deleted: $bucket" -ForegroundColor Green
}

# Delete Security Groups
Write-Host "`n🔓 Deleting Security Groups..."
Start-Sleep -Seconds 5  # Wait for instances to terminate
$groups = awslocal ec2 describe-security-groups --query 'SecurityGroups[?GroupName!=`default`].GroupId' --output text
foreach ($group in $groups) {
    awslocal ec2 delete-security-group --group-id $group
    Write-Host "  ✅ Deleted: $group" -ForegroundColor Green
}

Write-Host "`n✨ Cleanup complete!" -ForegroundColor Green
```

#### **Hari 7: Testing & Documentation**
```powershell
# File: verify_week3_deployment.ps1

Write-Host "🔍 Week 3 Deployment Verification" -ForegroundColor Cyan
Write-Host "="*50

# Test 1: S3 Bucket Vulnerability
Write-Host "`n📋 Test 1: S3 Public Access"
try {
    $s3Objects = awslocal s3 ls s3://vulnerable-company-backup/ --recursive
    Write-Host "✅ PASS: Can list bucket contents" -ForegroundColor Green
    Write-Host "  Found objects:"
    $s3Objects | ForEach-Object { Write-Host "    - $_" }
} catch {
    Write-Host "❌ FAIL: Cannot access bucket" -ForegroundColor Red
}

# Test 2: Download Sensitive File
Write-Host "`n📋 Test 2: Download Sensitive Data"
try {
    awslocal s3 cp s3://vulnerable-company-backup/config/database-config.txt . 2>&1 | Out-Null
    if (Test-Path "database-config.txt") {
        Write-Host "✅ PASS: Downloaded sensitive file" -ForegroundColor Green
        Write-Host "  Content preview:"
        Get-Content "database-config.txt" | Select-Object -First 3 | ForEach-Object { Write-Host "    $_" }
        Remove-Item "database-config.txt"
    }
} catch {
    Write-Host "❌ FAIL: Cannot download file" -ForegroundColor Red
}

# Test 3: Security Group Open Ports
Write-Host "`n📋 Test 3: Security Group Configuration"
$sgRules = awslocal ec2 describe-security-groups --group-names vulnerable-web-sg --query 'SecurityGroups[0].IpPermissions'
$openPorts = @()
$sgRules | ConvertFrom-Json | ForEach-Object {
    if ($_.IpRanges -contains "0.0.0.0/0" -or ($_.IpRanges | Where-Object { $_.CidrIp -eq "0.0.0.0/0" })) {
        $openPorts += $_.FromPort
    }
}

if ($openPorts.Count -ge 5) {
    Write-Host "✅ PASS: Multiple ports open to 0.0.0.0/0" -ForegroundColor Green
    Write-Host "  Open ports: $($openPorts -join ', ')"
} else {
    Write-Host "❌ FAIL: Not enough vulnerable ports" -ForegroundColor Red
}

# Test 4: EC2 Instance State
Write-Host "`n📋 Test 4: EC2 Instance Status"
$instanceState = awslocal ec2 describe-instances --filters "Name=tag:Name,Values=Vulnerable-Web-Server" --query 'Reservations[0].Instances[0].State.Name' --output text
if ($instanceState -eq "running") {
    Write-Host "✅ PASS: EC2 instance is running" -ForegroundColor Green
} else {
    Write-Host "⚠️  WARNING: EC2 instance state: $instanceState" -ForegroundColor Yellow
}

# Summary
Write-Host "`n" + "="*50
Write-Host "✅ Week 3 Deployment Verification Complete!" -ForegroundColor Green
Write-Host "="*50
```

```markdown
📝 CREATE: WEEK3_ARCHITECTURE_DOCUMENTATION.md

Content:
1. Architecture Overview
   - Diagram of deployed infrastructure
   - Component descriptions
   
2. Vulnerable Configurations
   - S3 bucket policy (JSON)
   - Security group rules (table)
   - List of sensitive files
   
3. Exploitation Paths
   - How S3 can be exploited
   - How EC2 can be exploited
   - Expected findings
   
4. Deployment Instructions
   - Step-by-step deployment
   - Verification steps
   - Cleanup procedures
   
5. Screenshots
   - S3 bucket contents
   - Security group rules
   - EC2 instance details
```

### **Target Minggu 3**
```
✅ Arsitektur dasar ter-deploy di LocalStack
✅ S3 bucket dengan konfigurasi publik (vulnerable)
✅ EC2 dengan Security Group terbuka (vulnerable)
✅ Sensitive files di S3 untuk testing
✅ Automation scripts (deploy & cleanup)
✅ Verification script confirms all vulnerabilities
✅ Complete documentation dengan screenshots
```

---

## 📊 Progress Tracking Template

### **Week 1 Checklist**
```markdown
📋 MINGGU 1: PERENCANAAN PROYEK

Day 1-2: ☐ Definisi Proyek
  ☐ Project scope document created
  ☐ 5 scenarios defined
  ☐ Success criteria documented

Day 3-4: ☐ Identifikasi Tools
  ☐ Tools list completed
  ☐ Installation links documented
  ☐ Version requirements specified

Day 5-6: ☐ Perencanaan Skenario
  ☐ Scenario matrix created
  ☐ Risk ratings assigned
  ☐ Expected outcomes defined

Day 7: ☐ Finalisasi Dokumen
  ☐ Complete project plan document
  ☐ Peer review completed
  ☐ Final version saved

✅ DELIVERABLE: Dokumen Perencanaan Proyek
```

### **Week 2 Checklist**
```markdown
📋 MINGGU 2: PERSIAPAN LABORATORIUM

Day 1: ☐ Docker Installation
  ☐ Docker Desktop installed
  ☐ Docker version verified
  ☐ Hello-world test passed

Day 2: ☐ LocalStack Setup
  ☐ docker-compose.yml configured
  ☐ LocalStack container running
  ☐ Health check passed

Day 3: ☐ AWS CLI Installation
  ☐ AWS CLI v2 installed
  ☐ Configured with test credentials
  ☐ Basic commands work

Day 4: ☐ awslocal Setup
  ☐ PowerShell profile configured
  ☐ awslocal function works
  ☐ S3 commands successful

Day 5: ☐ Additional Tools
  ☐ Nmap installed
  ☐ Python dependencies installed
  ☐ All tools verified

Day 6: ☐ Environment Testing
  ☐ Create S3 bucket test: PASS
  ☐ Upload file test: PASS
  ☐ Download file test: PASS
  ☐ Delete resources test: PASS

Day 7: ☐ Documentation
  ☐ Setup guide created
  ☐ Troubleshooting documented
  ☐ Configuration recorded

✅ DELIVERABLE: Functional LocalStack Environment
```

### **Week 3 Checklist**
```markdown
📋 MINGGU 3: PEMBANGUNAN ARSITEKTUR DASAR

Day 1: ☐ Architecture Planning
  ☐ Architecture diagram created
  ☐ Components defined
  ☐ IaC plan documented

Day 2-3: ☐ S3 Setup
  ☐ Vulnerable bucket created
  ☐ Sensitive files uploaded
  ☐ Public policy applied
  ☐ Anonymous access verified

Day 4-5: ☐ EC2 Setup
  ☐ Security group created
  ☐ Vulnerable rules added
  ☐ SSH key generated
  ☐ EC2 instance launched

Day 6: ☐ Automation Scripts
  ☐ deploy_vulnerable_lab.ps1 created
  ☐ cleanup_lab.ps1 created
  ☐ Scripts tested successfully

Day 7: ☐ Testing & Documentation
  ☐ Verification script created
  ☐ All tests passed
  ☐ Screenshots captured
  ☐ Architecture documented

✅ DELIVERABLE: Vulnerable Architecture Deployed
```

---

## 🎯 Success Criteria

### **Minggu 1 Success Metrics**
- ✅ Project plan approved by instructor/mentor
- ✅ All 5 scenarios clearly defined with risk ratings
- ✅ Tools list complete with justifications
- ✅ Timeline realistic and achievable

### **Minggu 2 Success Metrics**
- ✅ LocalStack responds to health checks
- ✅ Can create and delete S3 bucket without errors
- ✅ awslocal command works for all AWS services
- ✅ All team members have working environments

### **Minggu 3 Success Metrics**
- ✅ Can list S3 bucket contents anonymously
- ✅ Can download sensitive files from S3
- ✅ Security group allows access from 0.0.0.0/0
- ✅ Deployment script runs end-to-end successfully
- ✅ Cleanup script removes all resources

---

## 📝 Tips & Best Practices

### **General Tips**
```markdown
💡 DO:
- Commit code changes daily to Git
- Document every configuration change
- Take screenshots of each major step
- Test scripts before marking tasks complete
- Ask for help when stuck > 30 minutes

❌ DON'T:
- Skip documentation "for later"
- Deploy to real AWS (use LocalStack only!)
- Share sensitive files outside team
- Work without version control
- Rush through verification steps
```

### **Time Management**
```markdown
⏰ RECOMMENDED SCHEDULE:

Week 1:
- 1-2 hours/day for planning and documentation
- Focus on quality over speed
- Get feedback early

Week 2:
- 2-3 hours/day for setup and configuration
- Document issues immediately
- Test thoroughly before moving on

Week 3:
- 3-4 hours/day for deployment and testing
- Automate everything
- Verify each vulnerability works
```

---

## 🎊 Kesimpulan 3 Minggu Pertama

Setelah menyelesaikan 3 minggu ini, Anda akan memiliki:

✅ **Dokumen perencanaan profesional** untuk seluruh proyek
✅ **Testing environment yang fully functional** dengan LocalStack
✅ **Vulnerable AWS infrastructure** siap untuk penetration testing
✅ **Automation scripts** untuk deploy dan cleanup
✅ **Complete documentation** untuk reference dan reporting

**Anda siap untuk MINGGU KE-4: Eksekusi Skenario #1!** 🚀

---

*Next: Minggu 4-14 akan difokuskan pada eksekusi skenario, exploitation, mitigasi, dan reporting.*