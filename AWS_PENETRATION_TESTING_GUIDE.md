# 🎯 AWS Penetration Testing: Complete Guide

## 📖 Apa itu AWS Penetration Testing?

AWS Penetration Testing adalah proses sistematis untuk menguji keamanan infrastruktur cloud AWS dengan cara mensimulasikan serangan cyber yang dilakukan oleh attacker. Tujuannya adalah mengidentifikasi vulnerability sebelum attacker sungguhan menemukannya.

---

## 🔍 Bagaimana AWS Penetration Testing Bekerja?

### **1. Target Environment**
AWS Penetration Testing fokus pada layanan cloud seperti:
- **S3 (Simple Storage Service)** - Object storage
- **EC2 (Elastic Compute Cloud)** - Virtual machines
- **Lambda** - Serverless functions
- **IAM (Identity and Access Management)** - User/role management
- **RDS** - Managed databases
- **API Gateway** - REST API management
- **CloudFormation** - Infrastructure as Code

### **2. Attack Surface**
Yang menjadi target serangan:
- **Configuration errors** - Misconfigured services
- **Access controls** - Weak IAM policies
- **Network security** - Security group misconfigurations
- **Data exposure** - Unencrypted sensitive data
- **Code vulnerabilities** - Insecure application code

---

## 🚀 Methodology: 5-Phase Approach

### **Phase 1: Reconnaissance (Information Gathering)**
**Tujuan**: Mengumpulkan informasi tentang target tanpa interaksi langsung

**Teknik yang digunakan**:
```python
# 1. Service Discovery
aws_services = ['s3', 'ec2', 'lambda', 'rds', 'iam']
for service in aws_services:
    enumerate_service(service)

# 2. Domain/Subdomain enumeration
find_aws_resources("company.com")

# 3. Public information gathering
search_github_repos("company-name")
search_pastebin("company aws keys")
```

**Tools**:
- **DNS enumeration** (dig, nslookup)
- **Google dorking** (`site:amazonaws.com company`)
- **GitHub searching** (exposed AWS keys)
- **Shodan** (cloud service discovery)

**Output**: List of discovered services, endpoints, potential entry points

---

### **Phase 2: Enumeration (Active Scanning)**
**Tujuan**: Mengidentifikasi services yang aktif dan konfigurasinya

**S3 Enumeration**:
```python
def enumerate_s3_buckets():
    # 1. Bucket name guessing
    common_patterns = [
        "company-backup", "company-logs", "company-data",
        "prod-backups", "staging-assets", "dev-configs"
    ]
    
    # 2. Check bucket access
    for bucket in potential_buckets:
        test_bucket_access(bucket)
        check_bucket_policy(bucket)
        list_bucket_objects(bucket)
```

**IAM Enumeration**:
```python
def enumerate_iam():
    # 1. List users and roles
    list_users()
    list_roles()
    
    # 2. Check permissions
    for user in users:
        get_user_policies(user)
        check_privilege_escalation_paths(user)
```

**Lambda Enumeration**:
```python
def enumerate_lambda():
    # 1. Discover functions
    list_functions()
    
    # 2. Analyze function configuration
    for function in functions:
        get_function_code(function)
        check_environment_variables(function)
        analyze_execution_role(function)
```

---

### **Phase 3: Vulnerability Assessment**
**Tujuan**: Mengidentifikasi kelemahan keamanan yang dapat dieksploitasi

**Common AWS Vulnerabilities**:

1. **S3 Misconfigurations**:
   ```json
   // Vulnerable bucket policy
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Principal": "*",  // ❌ Public access!
       "Action": "s3:GetObject",
       "Resource": "arn:aws:s3:::company-secrets/*"
     }]
   }
   ```

2. **IAM Over-privileges**:
   ```json
   // Dangerous IAM policy
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Effect": "Allow",
       "Action": "*",  // ❌ Full access!
       "Resource": "*"
     }]
   }
   ```

3. **Lambda Vulnerabilities**:
   ```python
   # Vulnerable Lambda code
   def lambda_handler(event, context):
       command = event['command']
       # ❌ Command injection vulnerability!
       result = subprocess.run(command, shell=True)
       return result.stdout
   ```

---

### **Phase 4: Exploitation**
**Tujuan**: Membuktikan dampak vulnerability dengan mengeksploitasinya

**S3 Exploitation Example**:
```python
def exploit_s3_bucket():
    # 1. Discover public bucket
    bucket = "company-sensitive-data"
    
    # 2. List contents
    objects = s3.list_objects_v2(Bucket=bucket)
    
    # 3. Download sensitive files
    for obj in objects['Contents']:
        if 'secret' in obj['Key'].lower():
            print(f"🚨 Found: {obj['Key']}")
            download_file(bucket, obj['Key'])
    
    # 4. Demonstrate impact
    analyze_downloaded_files()
```

**IAM Privilege Escalation**:
```python
def privilege_escalation():
    # 1. Current limited permissions
    current_perms = get_current_permissions()
    
    # 2. Find escalation path
    if can_create_role() and can_attach_policy():
        # 3. Create admin role
        create_role("EscalatedRole", admin_trust_policy)
        attach_policy("EscalatedRole", "AdminAccess")
        
        # 4. Assume new role
        assume_role("EscalatedRole")
        print("🚨 Privilege escalation successful!")
```

**Lambda Code Injection**:
```python
def exploit_lambda():
    # 1. Identify vulnerable function
    function_name = "vulnerable-processor"
    
    # 2. Craft injection payload
    payload = {
        "command": "cat /proc/version; whoami; env"
    }
    
    # 3. Execute payload
    response = lambda_client.invoke(
        FunctionName=function_name,
        Payload=json.dumps(payload)
    )
    
    # 4. Extract sensitive information
    result = json.loads(response['Payload'].read())
    extract_secrets(result)
```

---

### **Phase 5: Post-Exploitation & Reporting**
**Tujuan**: Menilai dampak lengkap dan membuat laporan profesional

**Impact Assessment**:
```python
def assess_impact():
    findings = {
        'data_exposure': count_exposed_records(),
        'system_access': check_system_compromise(),
        'financial_risk': calculate_breach_cost(),
        'compliance_impact': check_regulatory_violations()
    }
    return findings
```

**Evidence Collection**:
- Screenshots of successful exploits
- Log files showing unauthorized access
- Downloaded sensitive data samples
- Command execution outputs

---

## 🛠️ Essential Tools & Techniques

### **Automated Tools**
```python
# Professional AWS security tools
tools = {
    'scout_suite': 'Comprehensive AWS security auditing',
    'prowler': 'AWS security best practices checker',
    'pacu': 'AWS exploitation framework',
    'cloud_mapper': 'AWS environment visualization',
    'nimbostratus': 'AWS fingerprinting toolkit'
}
```

### **Custom Scripts**
```python
# Our penetration testing toolkit
class AWSPentestSuite:
    def __init__(self):
        self.aws_client = setup_aws_client()
    
    def full_assessment(self):
        # 1. Service discovery
        services = self.discover_services()
        
        # 2. Vulnerability scanning
        vulns = self.scan_vulnerabilities(services)
        
        # 3. Exploitation
        exploits = self.attempt_exploitation(vulns)
        
        # 4. Reporting
        self.generate_report(exploits)
```

### **Manual Testing Techniques**
1. **Configuration Review**
   - Analyze IAM policies manually
   - Review security group rules
   - Check encryption settings

2. **Code Analysis**
   - Lambda function source code review
   - CloudFormation template analysis
   - API Gateway configuration check

3. **Access Testing**
   - Test different user contexts
   - Verify resource isolation
   - Check cross-account access

---

## 🎯 Attack Scenarios & Examples

### **Scenario 1: Data Breach via S3**
```
🎯 Target: Company with public S3 bucket

📋 Attack Flow:
1. Reconnaissance → Find bucket "company-backups"
2. Enumeration → Discover public read access
3. Exploitation → Download customer database
4. Impact → 100,000 customer records exposed

💰 Business Impact: $4.5M breach cost + compliance fines
```

### **Scenario 2: Privilege Escalation**
```
🎯 Target: Limited IAM user account

📋 Attack Flow:
1. Current Access → Read-only developer permissions
2. Discovery → User can create IAM roles
3. Exploitation → Create admin role + assume it
4. Impact → Full AWS account takeover

💰 Business Impact: Complete infrastructure compromise
```

### **Scenario 3: Lambda RCE**
```
🎯 Target: Vulnerable serverless function

📋 Attack Flow:
1. Function Discovery → Find API endpoint
2. Code Analysis → Identify command injection
3. Exploitation → Execute system commands
4. Data Extraction → Steal environment secrets

💰 Business Impact: API keys leaked + system access
```

---

## 🔐 Defense Mechanisms

### **What Defenders Should Implement**
```python
security_controls = {
    'preventive': [
        'Least privilege IAM policies',
        'S3 bucket policies',
        'Network ACLs',
        'Security groups',
        'Encryption at rest/transit'
    ],
    'detective': [
        'CloudTrail logging',
        'GuardDuty threat detection',
        'Config compliance monitoring',
        'VPC Flow Logs',
        'Access logging'
    ],
    'responsive': [
        'Automated remediation',
        'Incident response procedures',
        'Backup and recovery',
        'Forensic capabilities'
    ]
}
```

### **Monitoring & Detection**
- **CloudTrail** - API call logging
- **GuardDuty** - Threat intelligence
- **Security Hub** - Centralized findings
- **Config** - Configuration compliance
- **CloudWatch** - Metrics and alerts

---

## 📊 Professional Reporting

### **Executive Summary Format**
```markdown
## Executive Summary
- X critical vulnerabilities found
- Potential for complete data breach
- Estimated cost: $X.XM
- Immediate action required

## Technical Findings
1. Public S3 bucket (CRITICAL)
2. IAM privilege escalation (HIGH)
3. Lambda code injection (HIGH)

## Business Impact
- Customer data exposure
- Regulatory compliance violations
- Reputational damage
- Financial losses

## Recommendations
- Immediate: Fix critical issues
- Short-term: Implement monitoring
- Long-term: Security governance
```

---

## ⚖️ Legal & Ethical Considerations

### **Authorization Requirements**
- **Written permission** from asset owner
- **Scope definition** (what can be tested)
- **Time boundaries** (when testing occurs)
- **Contact information** for emergencies
- **Data handling** agreements

### **AWS Terms of Service**
- Some testing requires AWS notification
- Certain activities are prohibited
- Use AWS-approved testing methods
- Follow responsible disclosure

### **Best Practices**
- Only test authorized systems
- Use isolated test environments (like LocalStack)
- Document everything
- Report findings responsibly
- Respect data privacy

---

## 🎓 Skills Development Path

### **Beginner Level**
1. AWS fundamentals (S3, EC2, IAM basics)
2. Basic security concepts
3. Command line tools (AWS CLI)
4. Simple vulnerability identification

### **Intermediate Level**
1. Advanced AWS services (Lambda, API Gateway, DynamoDB)
2. Exploitation techniques
3. Custom script development
4. Professional reporting

### **Advanced Level**
1. Complex attack chains
2. Custom tool development
3. Red team operations
4. Security architecture design

### **Expert Level**
1. Zero-day discovery
2. Advanced persistent threats (APT)
3. Threat modeling
4. Security research & publishing

---

## 🚀 Practical Exercise

Try this hands-on challenge:

```python
# Challenge: Complete AWS Pentest
def challenge():
    print("🎯 Your Mission:")
    print("1. Discover all AWS services")
    print("2. Find 3+ vulnerabilities")
    print("3. Successfully exploit them")
    print("4. Write professional report")
    print("5. Propose remediation plan")
    
    return "Ready to become AWS Security Expert?"
```

---

**Remember**: AWS Penetration Testing is both an art and a science. It requires technical skills, business understanding, and ethical responsibility. Master these concepts, and you'll be ready for real-world cloud security challenges! 🔐✨