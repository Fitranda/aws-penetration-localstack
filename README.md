# 🛡️ AWS Penetration Testing Project
## LocalStack Environment - Week 1-3 Implementation

> **Project**: AWS Cloud Security Penetration Testing  
> **Duration**: 14 Weeks (Currently: Week 1-3)  
> **Environment**: LocalStack (AWS Simulation)  
> **Status**: Week 1-3 Ready ✅

---

## 📋 Quick Overview

Proyek ini adalah implementasi **AWS Penetration Testing** menggunakan **LocalStack** sebagai environment simulasi yang aman. Proyek dibagi menjadi 14 minggu, dan repository ini fokus pada **3 minggu pertama** (Persiapan & Deployment).

### **Week 1**: 📝 Perencanaan Proyek
- Definisi scope & objectives
- 5 skenario penetration testing
- Tools identification

### **Week 2**: 🛠️ Persiapan Laboratorium
- Docker & LocalStack setup
- AWS CLI & awslocal configuration
- Environment testing

### **Week 3**: 🏗️ Pembangunan Arsitektur Dasar
- Vulnerable S3 buckets deployment
- Vulnerable EC2 instances deployment
- Security testing infrastructure

---

## 🚀 Quick Start (5 Menit)

### **1. Prerequisites**
```powershell
# Check Docker
docker --version
docker-compose --version

# Check Python
python --version
pip --version

# Check AWS CLI
aws --version
```

### **2. Start LocalStack**
```powershell
# Clone & navigate
cd "D:\Tugass\Semester 7 Kuliah\Cyber Security"

# Start LocalStack
docker-compose up -d

# Verify
docker ps
```

### **3. Deploy Vulnerable Lab**
```powershell
# Run master deployment script
.\deploy_vulnerable_lab.ps1

# Expected: ✅ S3 Infrastructure deployed
#           ✅ EC2 Infrastructure deployed
```

### **4. Verify Deployment**
```powershell
# Run verification tests
.\verify_week3_deployment.ps1

# Expected: Pass rate 80%+ (all tests green)
```

---

## 📁 File Structure

```
aws-penetration-localstack/
│
├── 📋 PLANNING (Week 1)
│   ├── jadwal.txt                          # Original 14-week schedule
│   ├── JADWAL_3_MINGGU_PERTAMA.md         # Week 1-3 detailed plan
│   ├── Dokumen_Perencanaan_Proyek.md      # Professional project plan
│   └── CHECKLIST_3_MINGGU.md              # Interactive progress tracker
│
├── 🛠️ SETUP (Week 2)
│   ├── docker-compose.yml                  # LocalStack configuration
│   ├── .env                                # Environment variables
│   └── requirements.txt                    # Python dependencies
│
├── 🏗️ DEPLOYMENT SCRIPTS (Week 3)
│   ├── deploy_vulnerable_lab.ps1          # Master deployment script
│   ├── setup_vulnerable_s3.ps1            # S3 infrastructure setup
│   ├── setup_vulnerable_ec2.ps1           # EC2 infrastructure setup
│   ├── verify_week3_deployment.ps1        # Verification tests
│   └── cleanup_lab.ps1                    # Cleanup script
│
└── 📦 DATA
    └── localstack_data/                    # LocalStack persistent storage
```

---

## 🎯 5 Target Scenarios (Week 4+)

| # | Scenario | Risk | Week |
|---|----------|------|------|
| 1️⃣ | **Public S3 Bucket** | 🔴 9.5/10 | Week 4 |
| 2️⃣ | **Open Security Groups** | 🔴 9.0/10 | Week 5 |
| 3️⃣ | **IAM Privilege Escalation** | 🔴 8.5/10 | Week 7 |
| 4️⃣ | **SSRF on EC2 Metadata** | 🟠 8.0/10 | Week 8 |
| 5️⃣ | **Lateral Movement in VPC** | 🟠 7.5/10 | Week 10 |

---

## 💻 Common Commands

### **LocalStack Management**
```powershell
# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker logs localstack_main --tail 50

# Restart
docker-compose restart
```

### **AWS Operations (using awslocal)**
```powershell
# List S3 buckets
awslocal s3 ls

# List bucket contents
awslocal s3 ls s3://vulnerable-company-backup/ --recursive

# Download file
awslocal s3 cp s3://vulnerable-company-backup/config/database-config.txt .

# List EC2 instances
awslocal ec2 describe-instances

# List security groups
awslocal ec2 describe-security-groups
```

### **Lab Management**
```powershell
# Deploy entire lab
.\deploy_vulnerable_lab.ps1

# Deploy S3 only
.\setup_vulnerable_s3.ps1

# Deploy EC2 only
.\setup_vulnerable_ec2.ps1

# Verify deployment
.\verify_week3_deployment.ps1

# Cleanup everything
.\cleanup_lab.ps1
```

---

## 📊 Week 1-3 Checklist

### **✅ Week 1: Planning**
- [x] Project scope defined
- [x] 5 scenarios identified with risk ratings
- [x] Tools list finalized
- [x] Documentation created

### **✅ Week 2: Lab Setup**
- [ ] Docker Desktop installed
- [ ] LocalStack running
- [ ] AWS CLI configured
- [ ] awslocal alias working
- [ ] Environment tests passed

### **✅ Week 3: Infrastructure**
- [ ] S3 bucket deployed (vulnerable-company-backup)
- [ ] 4 sensitive files uploaded
- [ ] Public policy applied
- [ ] Security group created (vulnerable-web-sg)
- [ ] 10+ ports opened to 0.0.0.0/0
- [ ] EC2 instance launched
- [ ] Verification tests passed (80%+)

📝 **Detailed checklist**: See `CHECKLIST_3_MINGGU.md`

---

## 🔧 Deployed Vulnerable Resources

### **S3 Infrastructure** 🪣
- **Bucket**: `vulnerable-company-backup`
- **Policy**: PUBLIC (Principal: *)
- **Sensitive Files**:
  - `config/database-config.txt` - Database credentials
  - `secrets/api-keys.env` - API keys (AWS, Stripe, OpenAI)
  - `keys/production-server.pem` - SSH private key
  - `data/customer-data.csv` - Customer PII data

### **EC2 Infrastructure** 🖥️
- **Security Group**: `vulnerable-web-sg`
- **Instance**: `Vulnerable-Web-Server`
- **Open Ports** (0.0.0.0/0):
  - 22 (SSH)
  - 80 (HTTP)
  - 443 (HTTPS)
  - 3306 (MySQL)
  - 3389 (RDP)
  - 5432 (PostgreSQL)
  - 6379 (Redis)
  - 8080 (HTTP-Alt)
  - 9200 (Elasticsearch)
  - 27017 (MongoDB)

⚠️ **WARNING**: These are INTENTIONALLY VULNERABLE configurations for learning purposes!

---

## 📚 Documentation

- **`JADWAL_3_MINGGU_PERTAMA.md`** - Detailed day-by-day implementation guide
- **`Dokumen_Perencanaan_Proyek.md`** - Professional project planning document
- **`CHECKLIST_3_MINGGU.md`** - Interactive checklist for progress tracking
- **`jadwal.txt`** - Original 14-week project schedule

---

## 🔒 Security & Ethics

### **⚠️ IMPORTANT**
This project is for **EDUCATIONAL PURPOSES ONLY**:
- ✅ Use ONLY with LocalStack (simulated AWS environment)
- ❌ NEVER test on real AWS accounts without authorization
- ❌ NEVER deploy these configurations to production
- ✅ Always follow responsible disclosure practices

### **Legal Compliance**
- This is an authorized educational project
- All testing in isolated environment
- No real user data involved
- Compliant with computer misuse regulations

---

## 🛠️ Troubleshooting

### **LocalStack not starting**
```powershell
# Check if port 4566 is in use
netstat -ano | findstr :4566

# Force restart
docker-compose down
docker-compose up -d --force-recreate
```

### **awslocal command not found**
```powershell
# Reload PowerShell profile
. $PROFILE

# Or use full command
aws --endpoint-url=http://localhost:4566 s3 ls
```

### **Cannot connect to LocalStack**
```powershell
# Check container status
docker ps

# Check logs for errors
docker logs localstack_main --tail 100

# Verify network
ping localhost
```

---

## 🎓 Learning Resources

- **AWS Security Best Practices**: https://aws.amazon.com/security/best-practices/
- **LocalStack Documentation**: https://docs.localstack.cloud/
- **OWASP Cloud Security**: https://owasp.org/www-project-cloud-security/
- **AWS CLI Reference**: https://awscli.amazonaws.com/v2/documentation/api/latest/index.html

---

## 📈 Project Timeline

```
CURRENT: Week 1-3 (Persiapan) ← YOU ARE HERE
├── Week 1: ✅ Planning
├── Week 2: ⏳ Lab Setup
└── Week 3: ⏳ Infrastructure Deployment

UPCOMING: Week 4-14 (Eksekusi & Reporting)
├── Week 4-5:   Basic Exploitation (S3, Security Groups)
├── Week 6-8:   Advanced Exploitation (IAM, SSRF)
├── Week 9-10:  Network Security (VPC, Lateral Movement)
├── Week 11-12: Validation & Remediation
└── Week 13-14: Documentation & Presentation
```

---

## 👤 Author

**Semester 7 - Cyber Security Project**  
**Institution**: [Your University]  
**Course**: Cloud Security & Penetration Testing  
**Date**: October 2025

---

## 📞 Support

Jika mengalami masalah:
1. Check troubleshooting section di atas
2. Review `CHECKLIST_3_MINGGU.md` untuk verification steps
3. Check LocalStack logs: `docker logs localstack_main`
4. Consult documentation files

---

## 🎯 Next Steps

1. ✅ Complete Week 1-3 checklist
2. 📖 Read `JADWAL_3_MINGGU_PERTAMA.md` thoroughly
3. 🚀 Deploy lab: `.\deploy_vulnerable_lab.ps1`
4. ✔️ Verify: `.\verify_week3_deployment.ps1`
5. 🎊 Ready for Week 4 exploitation scenarios!

---

**⚡ Ready to start? Run:** `.\deploy_vulnerable_lab.ps1`

**📋 Track progress:** Open `CHECKLIST_3_MINGGU.md`

**🎓 Good luck with your AWS Penetration Testing journey!** 🛡️🔥
