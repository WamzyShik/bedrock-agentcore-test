# Infrastructure

This directory contains all infrastructure-as-code and deployment configurations for the fraud detection system.

## Overview

The infrastructure includes:
- **AWS Bedrock Agent**: AI agent with Claude 3 Sonnet model
- **Action Groups**: Tool integrations for identity verification, fraud database, and geolocation
- **Knowledge Base**: Vector database for fraud patterns and rules
- **Data Storage**: DynamoDB tables and S3 buckets
- **Streaming**: Kinesis streams and Lambda processors
- **Monitoring**: CloudWatch dashboards, alarms, and X-Ray tracing
- **IAM Roles**: Proper permissions for all components

## Structure

- `aws/` - AWS-specific infrastructure and deployment
  - `bedrock/` - AWS Bedrock agent configurations and deployment
  - `cloudformation/` - CloudFormation templates
  - `deployment/` - Deployment scripts and guides
  - `config/` - Infrastructure configuration (storage, streaming, monitoring)
  - `iam/` - IAM roles and permissions
- `cdk/` - AWS CDK infrastructure code

## Quick Start

### Deploy Full Infrastructure

Deploy complete infrastructure (recommended):

```bash
python aws/deployment/deploy_full_infrastructure.py --environment dev --region us-east-1
```

This deploys:
- IAM roles and permissions
- DynamoDB tables and S3 buckets
- Kinesis streams and Lambda functions
- AWS Bedrock Agent with action groups
- CloudWatch dashboards and alarms
- X-Ray tracing

### Deploy Bedrock Agent Only

Deploy only Bedrock Agent (requires existing IAM roles):

```bash
python aws/bedrock/deploy_bedrock_agent.py --environment dev --region us-east-1
```

## Prerequisites

1. **AWS Account** with appropriate permissions
2. **AWS CLI** configured with credentials
3. **Python 3.11+** installed
4. **Boto3** library installed:
   ```bash
   pip install boto3
   ```

## Component-Specific Deployment

**Data Storage:**
```bash
python aws/config/data_storage_config.py --environment dev --region us-east-1
```

**Streaming Infrastructure:**
```bash
python aws/config/streaming_config.py --environment dev --region us-east-1 --lambda-role-arn <ROLE_ARN>
```

**Monitoring:**
```bash
python aws/config/monitoring_config.py --environment dev --region us-east-1
```

## Configuration

### Agent Configuration

The agent is configured with:
- **Model**: Claude 3 Sonnet (`anthropic.claude-3-sonnet-20240229-v1:0`)
- **Instruction**: Specialized fraud detection prompt
- **Session TTL**: 600 seconds (10 minutes)

### Action Groups

Three action groups are configured:

1. **Identity Verification** - Verifies user identity and checks for account compromise
2. **Fraud Database** - Queries fraud database for similar cases
3. **Geolocation** - Assesses location risk and verifies travel patterns

### Infrastructure Components

**DynamoDB Tables:**
- `fraud-detection-transactions-{env}`: Transaction history with TTL
- `fraud-detection-decisions-{env}`: Decision context and memory
- `fraud-detection-user-profiles-{env}`: User behavior profiles
- `fraud-detection-patterns-{env}`: Learned fraud patterns

**S3 Buckets:**
- `fraud-detection-audit-logs-{env}-{account}`: Audit logs with lifecycle policies
- `fraud-detection-decision-trails-{env}-{account}`: Decision trails
- `fraud-detection-models-{env}-{account}`: ML model artifacts

**Kinesis Streams:**
- `fraud-detection-transactions-{env}`: Transaction ingestion
- `fraud-detection-events-{env}`: Fraud events

## Monitoring

### CloudWatch Logs

Agent logs are stored in:
```
/aws/bedrock/agent/fraud-detection-{environment}
```

View logs:
```bash
aws logs tail /aws/bedrock/agent/fraud-detection-dev --follow
```

### CloudWatch Metrics

Monitor agent performance:
- Invocation count
- Error rate
- Latency
- Token usage

## Documentation

For detailed deployment instructions, see:
- `aws/deployment/DEPLOYMENT_GUIDE.md` - Comprehensive deployment guide
- `docs/guides/` - User guides and tutorials
- `docs/operations/` - Operations runbooks

## Security Best Practices

1. **Least Privilege**: IAM roles have minimal required permissions
2. **Encryption**: All data encrypted at rest and in transit
3. **VPC**: Deploy Lambda functions in VPC for network isolation
4. **Secrets**: Store API keys in AWS Secrets Manager
5. **Audit**: Enable CloudTrail for all API calls

## Cleanup

### Delete CloudFormation Stack

```bash
aws cloudformation delete-stack \
  --stack-name fraud-detection-bedrock-agent-dev \
  --region us-east-1
```

## Support

For issues or questions:
1. Check CloudWatch logs for error details
2. Review IAM role permissions
3. Verify Bedrock service quotas
4. See `docs/operations/TROUBLESHOOTING.md`

## References

- [AWS Bedrock Agent Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Claude 3 Model Documentation](https://docs.anthropic.com/claude/docs)
- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
