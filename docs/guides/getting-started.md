# Getting Started with Fraud Detection System

Welcome to the Fraud Detection System! This guide will help you get up and running quickly.

## Prerequisites

- Python 3.8 or higher
- AWS account with Bedrock access (for production use)
- pip or uv package manager

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/fraud-detection-system.git
cd fraud-detection-system
```

### 2. Install Dependencies

```bash
# Using pip
pip install -e .

# Or using uv (recommended)
uv pip install -e .
```

### 3. Configure Environment

Create a `.env` file in the project root:

```bash
# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# API Configuration
API_KEY=your_api_key_here
ENVIRONMENT=development
```

## Quick Start Options

### Option 1: Run Basic Fraud Detection

Analyze a single transaction:

```python
from fraud_detection.core import FraudDetectionAgent

agent = FraudDetectionAgent()
result = agent.analyze_transaction({
    'transaction_id': 'tx_123',
    'user_id': 'user_456',
    'amount': 150.00,
    'currency': 'USD',
    'merchant': 'Amazon'
})

print(f"Decision: {result['decision']}")
print(f"Confidence: {result['confidence']}")
```

### Option 2: Start the API Server

Run the REST API server:

```bash
python fraud_detection_api.py
```

The server will start on `http://localhost:5000`

**Get your API key** from the console output:
```
Default API key created: fds_...
```

**Test the API:**
```bash
curl -X POST http://localhost:5000/api/v1/transactions \
  -H "X-API-Key: fds_your_key" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "tx_123",
    "user_id": "user_456",
    "amount": 150.00,
    "currency": "USD"
  }'
```

### Option 3: Run Web Dashboards

#### Admin Dashboard

Monitor infrastructure health and costs:

```bash
python stress_testing/demo_admin_dashboard.py
```

Then open: `http://localhost:8080/admin_dashboard.html`

**Features:**
- Infrastructure health monitoring
- Resource utilization tracking
- Cost management
- Operational controls

#### Agent Dashboard

Monitor AI agent performance:

```bash
python web_interface/dashboard_server.py
```

Then open: `http://localhost:5000/agent_dashboard.html`

**Features:**
- Real-time agent health indicators
- Workload distribution visualization
- Coordination efficiency metrics
- Workflow visualization

#### Analytics Dashboard

View fraud detection analytics:

```bash
cd web_interface
python analytics_server.py
```

Then open: `http://127.0.0.1:5001`

**Features:**
- Real-time metrics
- Performance charts
- Pattern detection heatmaps
- Live updates

### Option 4: Run Stress Tests

Test system performance under load:

```bash
# Complete demo with live dashboard (recommended)
python -m stress_testing.demo

# Dashboard only
python -m stress_testing.cli --dashboard-only

# Specific scenarios
python -m stress_testing.cli --scenario investor
python -m stress_testing.cli --scenario peak-load
```

**What you'll see:**
- Real-time TPS and transaction counts
- Fraud detection statistics
- Money saved calculations
- System performance metrics

## Basic Usage Examples

### Analyze a Transaction

```python
from fraud_detection.core import FraudDetectionAgent

agent = FraudDetectionAgent()

transaction = {
    'transaction_id': 'tx_001',
    'user_id': 'user_123',
    'amount': 1500.00,
    'currency': 'USD',
    'merchant': 'Online Store',
    'location': 'New York, US',
    'device_id': 'device_xyz',
    'timestamp': '2024-01-15T10:30:00Z'
}

result = agent.analyze_transaction(transaction)

print(f"Decision: {result['decision']}")
print(f"Risk Level: {result['risk_level']}")
print(f"Confidence: {result['confidence']}")
print(f"Reasoning: {result['reasoning']}")
```

### Batch Processing

```python
from fraud_detection.core import FraudDetectionAgent

agent = FraudDetectionAgent()

transactions = [
    {'transaction_id': 'tx_001', 'amount': 100.00, 'user_id': 'user_1'},
    {'transaction_id': 'tx_002', 'amount': 250.00, 'user_id': 'user_2'},
    {'transaction_id': 'tx_003', 'amount': 500.00, 'user_id': 'user_3'}
]

results = agent.analyze_batch(transactions)

for result in results:
    print(f"{result['transaction_id']}: {result['decision']}")
```

### Using the API Client

```python
from fraud_detection_sdk import FraudDetectionClient

client = FraudDetectionClient(
    api_key='your_api_key',
    environment='production'
)

result = client.analyze_transaction({
    'transaction_id': 'tx_123',
    'user_id': 'user_abc',
    'amount': 1500.00,
    'currency': 'USD'
})

print(f"Decision: {result.decision}")
print(f"Confidence: {result.confidence}")
```

## Running Tests

### Run All Tests

```bash
pytest tests/
```

### Run Specific Test Categories

```bash
# Unit tests only
pytest tests/unit/

# Integration tests only
pytest tests/integration/

# With coverage
pytest tests/ --cov=src/fraud_detection --cov-report=html
```

### Run Examples

```bash
# Basic examples
python examples/basic/simple_fraud_detection.py

# Agent examples
python examples/agents/agent_communication.py

# Dashboard examples
python examples/dashboards/admin_dashboard.py
```

## Configuration

### Environment Variables

Key environment variables you can configure:

```bash
# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key

# API Configuration
API_KEY=your_api_key
API_PORT=5000
ENVIRONMENT=development

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fraud_detection

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/fraud_detection.log

# Performance
MAX_WORKERS=10
BATCH_SIZE=100
TIMEOUT_SECONDS=30
```

### Configuration Files

- `pyproject.toml` - Project configuration and dependencies
- `.env` - Environment-specific settings (not in git)
- `infrastructure/aws/config/` - AWS service configurations

## Next Steps

### Learn More

- **[API Reference](../api/API_REFERENCE.md)** - Complete API documentation
- **[Architecture](../architecture/ARCHITECTURE.md)** - System architecture details
- **[Deployment Guide](./deployment-guide.md)** - Deploy to production
- **[Operations Runbook](../operations/OPERATIONS_RUNBOOK.md)** - Operational procedures

### Explore Examples

- **[Basic Examples](../../examples/basic/)** - Simple usage examples
- **[Agent Examples](../../examples/agents/)** - Multi-agent coordination
- **[Dashboard Examples](../../examples/dashboards/)** - Web interface demos
- **[Stress Testing](../../examples/stress_testing/)** - Performance testing

### Development

- **[Contributing Guide](../project/CONTRIBUTING.md)** - How to contribute
- **[Code of Conduct](../project/CODE-OF-CONDUCT.md)** - Community guidelines
- **[Security Policy](../SECURITY.md)** - Security practices

## Troubleshooting

### Common Issues

**Issue: Import errors after installation**
```bash
# Solution: Install in editable mode
pip install -e .
```

**Issue: AWS credentials not found**
```bash
# Solution: Configure AWS CLI or set environment variables
aws configure
# Or set in .env file
```

**Issue: API server won't start**
```bash
# Solution: Check if port is already in use
lsof -i :5000
# Kill the process or use a different port
```

**Issue: Tests failing**
```bash
# Solution: Install test dependencies
pip install -e ".[test]"
```

For more troubleshooting help, see [TROUBLESHOOTING.md](../operations/TROUBLESHOOTING.md)

## Support

- **Documentation**: https://docs.fraud-detection.example.com
- **Issues**: https://github.com/your-org/fraud-detection-system/issues
- **Email**: support@fraud-detection.example.com

## Quick Reference

### Key Commands

```bash
# Start API server
python fraud_detection_api.py

# Run tests
pytest tests/

# Run stress test
python -m stress_testing.demo

# Start dashboard
python web_interface/dashboard_server.py

# Check system health
curl http://localhost:5000/api/v1/health
```

### Key Directories

- `src/fraud_detection/` - Core application code
- `tests/` - Test suite
- `examples/` - Usage examples
- `docs/` - Documentation
- `infrastructure/` - Deployment configs
- `scripts/` - Utility scripts

---

**Ready to dive deeper?** Check out the [API Reference](../api/API_REFERENCE.md) or explore the [examples](../../examples/).
