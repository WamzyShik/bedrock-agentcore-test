# Deployment Guide

This guide covers deploying the Fraud Detection System to various environments.

## Quick Links

- **[AWS Infrastructure Deployment](../../infrastructure/aws/deployment/DEPLOYMENT_GUIDE.md)** - Complete AWS deployment guide
- **[Blue-Green Deployment](../../infrastructure/aws/deployment/deploy_blue_green.sh)** - Zero-downtime deployment script

## Deployment Options

### 1. Local Development

For local development and testing:

```bash
# Install dependencies
pip install -e .

# Start the API server
python fraud_detection_api.py

# Run tests
pytest tests/
```

### 2. AWS Production Deployment

For production deployment to AWS, see the comprehensive [AWS Infrastructure Deployment Guide](../../infrastructure/aws/deployment/DEPLOYMENT_GUIDE.md).

**Quick Overview:**

1. **Prerequisites**
   - AWS CLI configured
   - Python 3.11+
   - Boto3 installed
   - Appropriate AWS permissions

2. **Deploy Infrastructure**
   ```bash
   cd infrastructure/aws/deployment
   python deploy_full_infrastructure.py
   ```

3. **Deploy Application**
   ```bash
   # Blue-green deployment (zero downtime)
   ./deploy_blue_green.sh
   ```

### 3. Container Deployment

Deploy using Docker containers:

```bash
# Build image
docker build -t fraud-detection:latest .

# Run container
docker run -p 5000:5000 \
  -e AWS_REGION=us-east-1 \
  -e API_KEY=your_key \
  fraud-detection:latest
```

### 4. Kubernetes Deployment

Deploy to Kubernetes cluster:

```bash
# Apply configurations
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check status
kubectl get pods
kubectl get services
```

## Deployment Checklist

### Pre-Deployment

- [ ] Review and test all changes locally
- [ ] Run full test suite: `pytest tests/`
- [ ] Update version numbers
- [ ] Update CHANGELOG.md
- [ ] Review security configurations
- [ ] Backup production data
- [ ] Notify stakeholders of deployment window

### Deployment

- [ ] Deploy to staging environment first
- [ ] Run smoke tests on staging
- [ ] Monitor staging for 24 hours
- [ ] Deploy to production using blue-green strategy
- [ ] Verify health endpoints
- [ ] Run production smoke tests
- [ ] Monitor error rates and performance

### Post-Deployment

- [ ] Verify all services are healthy
- [ ] Check CloudWatch dashboards
- [ ] Review application logs
- [ ] Test critical user flows
- [ ] Monitor for 1 hour minimum
- [ ] Document any issues encountered
- [ ] Update runbook if needed

## Environment Configuration

### Development

```bash
# .env.development
ENVIRONMENT=development
LOG_LEVEL=DEBUG
API_PORT=5000
AWS_REGION=us-east-1
```

### Staging

```bash
# .env.staging
ENVIRONMENT=staging
LOG_LEVEL=INFO
API_PORT=5000
AWS_REGION=us-east-1
ENABLE_MONITORING=true
```

### Production

```bash
# .env.production
ENVIRONMENT=production
LOG_LEVEL=WARNING
API_PORT=5000
AWS_REGION=us-east-1
ENABLE_MONITORING=true
ENABLE_TRACING=true
RATE_LIMIT_ENABLED=true
```

## Rollback Procedures

### Immediate Rollback

If critical issues are detected:

```bash
# AWS Blue-Green Rollback
cd infrastructure/aws/deployment
./rollback_deployment.sh

# Verify rollback
curl https://api.fraud-detection.example.com/health
```

### Gradual Rollback

For non-critical issues:

1. Stop routing new traffic to new version
2. Monitor existing traffic completion
3. Gradually shift traffic back to old version
4. Investigate and fix issues
5. Redeploy when ready

## Monitoring Deployment

### Health Checks

```bash
# API health
curl https://api.fraud-detection.example.com/api/v1/health

# System metrics
curl https://api.fraud-detection.example.com/api/v1/metrics
```

### CloudWatch Dashboards

Monitor these key metrics:

- **API Response Time**: Should be < 300ms p95
- **Error Rate**: Should be < 0.1%
- **Throughput**: Monitor TPS
- **Lambda Errors**: Should be minimal
- **DynamoDB Throttles**: Should be zero

### Alarms

Key alarms to watch:

- High error rate (> 1%)
- High latency (> 500ms p95)
- Lambda failures
- DynamoDB throttling
- Bedrock API errors

## Troubleshooting

### Deployment Fails

**Issue**: Deployment script fails

**Solutions**:
1. Check AWS credentials: `aws sts get-caller-identity`
2. Verify permissions
3. Check CloudFormation events
4. Review deployment logs

### Health Check Fails

**Issue**: Health endpoint returns unhealthy

**Solutions**:
1. Check application logs
2. Verify database connectivity
3. Check AWS service status
4. Review recent changes

### High Error Rate

**Issue**: Error rate spikes after deployment

**Solutions**:
1. Immediate rollback if > 5% error rate
2. Check application logs for errors
3. Verify configuration changes
4. Check dependency services

## Security Considerations

### Pre-Deployment Security

- [ ] Scan for vulnerabilities: `pip-audit`
- [ ] Review IAM permissions
- [ ] Rotate API keys if needed
- [ ] Update security groups
- [ ] Review encryption settings

### Post-Deployment Security

- [ ] Verify HTTPS is enforced
- [ ] Check authentication is working
- [ ] Test rate limiting
- [ ] Review access logs
- [ ] Verify encryption at rest

## Performance Optimization

### Before Deployment

- Run load tests
- Profile application
- Optimize database queries
- Review caching strategy
- Check resource limits

### After Deployment

- Monitor response times
- Check resource utilization
- Review slow queries
- Optimize if needed
- Scale resources as required

## CI/CD Integration

### GitHub Actions

The deployment is automated via GitHub Actions:

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to AWS
        run: |
          cd infrastructure/aws/deployment
          python deploy_full_infrastructure.py
```

### Manual Deployment

For manual deployments:

```bash
# 1. Pull latest code
git pull origin main

# 2. Run tests
pytest tests/

# 3. Deploy
cd infrastructure/aws/deployment
python deploy_full_infrastructure.py

# 4. Verify
curl https://api.fraud-detection.example.com/health
```

## Support

For deployment issues:

- **Operations Runbook**: [OPERATIONS_RUNBOOK.md](../operations/OPERATIONS_RUNBOOK.md)
- **Troubleshooting Guide**: [TROUBLESHOOTING.md](../operations/TROUBLESHOOTING.md)
- **AWS Deployment Details**: [AWS Deployment Guide](../../infrastructure/aws/deployment/DEPLOYMENT_GUIDE.md)

## Additional Resources

- [Architecture Documentation](../architecture/ARCHITECTURE.md)
- [API Reference](../api/API_REFERENCE.md)
- [Security Policy](../../SECURITY.md)
- [Operations Runbook](../operations/OPERATIONS_RUNBOOK.md)

---

**Last Updated**: 2025-10-21  
**Version**: 1.0.0
