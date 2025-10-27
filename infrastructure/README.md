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

### Data Storage Configuration

Deploy DynamoDB tables and S3 buckets:

```bash
cd infrastructure/aws/config
python data_storage_config.py --environment dev --region us-east-1
```

This creates:
- DynamoDB tables for transactions, decisions, user profiles, and fraud patterns
- S3 buckets for audit logs, decision trails, and model artifacts
- Encryption, lifecycle policies, and retention rules

### Streaming Infrastructure Configuration

Deploy Kinesis streams, Lambda functions, and EventBridge rules:

```bash
cd infrastructure/aws/config
python streaming_config.py --environment dev --region us-east-1 --lambda-role-arn <ROLE_ARN>
```

This creates:
- Kinesis Data Streams for transaction ingestion and fraud events
- Lambda functions for stream processing and alert handling
- EventBridge rules for event-driven responses
- Dead letter queues for failed processing

### Monitoring Configuration

Set up CloudWatch dashboards, alarms, and X-Ray tracing:

```bash
cd infrastructure/aws/config
python monitoring_config.py --environment dev --region us-east-1
```

This creates:
- CloudWatch alarms for Lambda, Kinesis, and DynamoDB
- Custom dashboards for fraud detection metrics
- SNS topics for alarm notifications
- X-Ray tracing for distributed system visibility
- Log metric filters for custom metrics

## Configuration

### Configuration Directory (`aws/config/`)

The `aws/config/` directory contains infrastructure configuration modules that can be used independently or as part of the full deployment:

**`data_storage_config.py`**
- Configures DynamoDB tables with encryption, streams, and TTL
- Sets up S3 buckets with versioning, lifecycle policies, and encryption
- Provides `DataStorageConfigurator` class for programmatic access
- Can be run standalone or imported by deployment scripts

**`streaming_config.py`**
- Configures Kinesis Data Streams with encryption and retention
- Sets up Lambda functions for stream processing
- Configures EventBridge rules for event-driven architecture
- Creates dead letter queues for error handling
- Provides `StreamingInfrastructureConfigurator` class

**`monitoring_config.py`**
- Creates CloudWatch alarms for all infrastructure components
- Sets up custom dashboards for fraud detection metrics
- Configures SNS topics for alarm notifications
- Enables X-Ray tracing for Lambda functions
- Creates log metric filters for custom metrics
- Provides `MonitoringConfigurator` class

**Usage in Code:**

```python
from infrastructure.aws.config.data_storage_config import DataStorageConfigurator
from infrastructure.aws.config.streaming_config import StreamingInfrastructureConfigurator
from infrastructure.aws.config.monitoring_config import MonitoringConfigurator

# Initialize configurators
storage = DataStorageConfigurator(region_name='us-east-1', environment='dev')
streaming = StreamingInfrastructureConfigurator(region_name='us-east-1', environment='dev')
monitoring = MonitoringConfigurator(region_name='us-east-1', environment='dev')

# Deploy components
storage_resources = storage.setup_all_storage()
streaming_resources = streaming.setup_all_streaming_infrastructure(lambda_role_arn)
monitoring_resources = monitoring.setup_all_monitoring(lambda_functions, kinesis_streams, dynamodb_tables)
```

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
