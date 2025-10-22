# StarJam Starter Toolkit

A comprehensive fraud detection system built on AWS Bedrock AgentCore, featuring specialized AI agents, advanced memory systems, adaptive reasoning, and real-time transaction processing.

[![CI/CD Pipeline](https://github.com/your-org/bedrock-agentcore-starter-toolkit/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/your-org/bedrock-agentcore-starter-toolkit/actions)
[![codecov](https://codecov.io/gh/your-org/bedrock-agentcore-starter-toolkit/branch/main/graph/badge.svg)](https://codecov.io/gh/your-org/bedrock-agentcore-starter-toolkit)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Documentation](#documentation)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The StarJam Toolkit is an enterprise-grade fraud detection system that leverages AWS Bedrock's AI capabilities to provide:

- **Specialized AI Agents** for transaction analysis, pattern detection, risk assessment, and compliance
- **Advanced Memory Systems** with context-aware decision making and pattern learning
- **Adaptive Reasoning Engine** for explainable AI decisions
- **Real-time Stream Processing** for high-throughput transaction analysis
- **Comprehensive Monitoring** with dashboards and analytics

---

## ✨ Features

### 🤖 Specialized AI Agents

- **Transaction Analyzer**: Real-time transaction validation and anomaly detection
- **Pattern Detector**: Statistical analysis and behavioral pattern recognition
- **Risk Assessor**: Multi-factor risk scoring and geographic analysis
- **Compliance Agent**: Regulatory compliance checking and audit trail generation

### 🧠 Memory & Learning

- **Context-Aware Memory**: Maintains user behavior profiles and transaction history
- **Pattern Learning Engine**: Learns from historical data to improve detection
- **Adaptive Thresholds**: Dynamically adjusts risk thresholds based on patterns

### 🔄 Real-time Processing

- **Stream Processing**: High-throughput transaction stream handling
- **Event Response System**: Automated response to fraud events
- **Scalable Architecture**: Auto-scaling based on load

### 📊 Monitoring & Analytics

- **Admin Dashboard**: System health and performance metrics
- **Agent Dashboard**: Agent-specific analytics and insights
- **Business Metrics**: ROI, cost savings, and fraud prevention statistics

---

## 📁 Project Structure

```
starjam-toolkit/
├── src/
│   └── fraud_detection/          # Main package
│       ├── core/                 # Core fraud detection logic
│       ├── agents/               # Specialized AI agents
│       │   ├── coordination/     # Agent coordination
│       │   ├── specialized/      # Specialized agent implementations
│       │   └── bedrock/          # AWS Bedrock integration
│       ├── memory/               # Memory and learning systems
│       ├── reasoning/            # Reasoning engine
│       ├── streaming/            # Stream processing
│       ├── external/             # External tool integrations
│       └── web/                  # Web interfaces and APIs
│           ├── api/              # REST APIs
│           └── dashboards/       # Dashboard implementations
├── tests/
│   ├── unit/                     # Unit tests
│   ├── integration/              # Integration tests
│   └── fixtures/                 # Test fixtures and utilities
├── infrastructure/
│   └── aws/                      # AWS infrastructure
│       ├── bedrock/              # Bedrock agent configuration
│       ├── cloudformation/       # CloudFormation templates
│       ├── deployment/           # Deployment scripts
│       ├── config/               # Configuration files
│       └── iam/                  # IAM policies
├── examples/
│   ├── basic/                    # Basic usage examples
│   ├── agents/                   # Agent examples
│   ├── reasoning/                # Reasoning examples
│   ├── memory/                   # Memory system examples
│   ├── dashboards/               # Dashboard examples
│   └── stress_testing/           # Stress testing examples
├── docs/
│   ├── architecture/             # Architecture documentation
│   ├── api/                      # API reference
│   ├── guides/                   # User guides
│   ├── operations/               # Operations documentation
│   └── project/                  # Project documentation
├── scripts/
│   ├── security/                 # Security scripts
│   ├── release/                  # Release management
│   ├── development/              # Development utilities
│   └── utilities/                # General utilities
├── .archive/                     # Historical artifacts
├── pyproject.toml                # Project configuration
├── MIGRATION.md                  # Migration guide
└── README.md                     # This file
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-org/bedrock-agentcore-starter-toolkit.git
cd bedrock-agentcore-starter-toolkit
```

2. **Install dependencies:**

```bash
# Using pip
pip install -e .

# Or using uv (recommended)
uv pip install -e .
```

3. **Configure AWS credentials:**

```bash
aws configure
```

4. **Set up environment variables:**

```bash
cp .env.example .env
# Edit .env with your configuration
```

### Verify Installation

```bash
# Run tests
pytest tests/

# Check package installation
python -c "import fraud_detection; print('✅ Installation successful!')"
```

---

## 💡 Usage Examples

### Basic Fraud Detection

```python
from fraud_detection.core.fraud_detection_agent import FraudDetectionAgent
from fraud_detection.memory.models import Transaction, Location, DeviceInfo
from decimal import Decimal

# Initialize the fraud detection agent
agent = FraudDetectionAgent()

# Create a transaction
transaction = Transaction(
    id="tx_12345",
    user_id="user_789",
    amount=Decimal("1500.00"),
    currency="USD",
    merchant_id="merchant_456",
    location=Location(country="US", city="New York"),
    device_info=DeviceInfo(device_id="device_123", ip_address="192.168.1.1"),
    timestamp=datetime.now()
)

# Analyze the transaction
result = agent.analyze_transaction(transaction)

print(f"Fraud Score: {result.fraud_score}")
print(f"Decision: {result.decision}")
print(f"Reasons: {result.reasons}")
```

### Using Specialized Agents

```python
from fraud_detection.agents.specialized.specialized_agents.transaction_analyzer import TransactionAnalyzer
from fraud_detection.agents.specialized.specialized_agents.base_agent import AgentConfiguration

# Configure the agent
config = AgentConfiguration(
    agent_id="transaction_analyzer_001",
    capabilities=["transaction_validation", "anomaly_detection"]
)

# Initialize the agent
analyzer = TransactionAnalyzer(config)

# Process a transaction
result = analyzer.process(transaction)
```

### Memory-Aware Decisions

```python
from fraud_detection.memory.memory_manager import MemoryManager
from fraud_detection.memory.context_manager import ContextManager

# Initialize memory systems
memory_manager = MemoryManager()
context_manager = ContextManager()

# Store transaction history
memory_manager.store_transaction(transaction)

# Get user context for decision making
user_context = context_manager.get_user_context(user_id="user_789")

# Make context-aware decision
decision = agent.analyze_with_context(transaction, user_context)
```

### Real-time Stream Processing

```python
from fraud_detection.streaming.transaction_stream_processor import TransactionStreamProcessor

# Initialize stream processor
processor = TransactionStreamProcessor()

# Process transaction stream
async def process_stream():
    async for transaction in transaction_stream:
        result = await processor.process_transaction(transaction)
        if result.is_fraud:
            await handle_fraud_alert(result)

# Run the processor
await process_stream()
```

For more examples, see the [`examples/`](examples/) directory.

---

## 📚 Documentation

Comprehensive documentation is available in the [`docs/`](docs/) directory:

### Architecture

- [System Architecture](docs/architecture/README.md) - Overall system design and components
- [Component Diagrams](docs/architecture/) - Detailed component relationships
- [Data Flow](docs/architecture/) - Transaction processing pipelines

### API Reference

- [API Documentation](docs/api/API_REFERENCE.md) - Complete API reference
- [Request/Response Formats](docs/api/) - API schemas and examples
- [Authentication](docs/api/) - Authentication and authorization

### Guides

- [Getting Started](docs/guides/getting-started.md) - Detailed setup and configuration
- [Deployment Guide](docs/guides/deployment-guide.md) - Production deployment instructions
- [Best Practices](docs/guides/) - Development and operational best practices

### Operations

- [Operations Runbook](docs/operations/) - Day-to-day operations
- [Troubleshooting](docs/operations/) - Common issues and solutions
- [Monitoring](docs/operations/) - Monitoring and alerting setup

---

## 🛠️ Development

### Setting Up Development Environment

```bash
# Install development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run linting
ruff check .

# Run type checking
mypy src/
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src/fraud_detection --cov-report=html

# Run specific test categories
pytest tests/unit/          # Unit tests only
pytest tests/integration/   # Integration tests only

# Run with verbose output
pytest tests/ -v
```

### Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
ruff check src/ tests/

# Type check
mypy src/
```

---

## 🧪 Testing

The project includes comprehensive test coverage:

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **End-to-End Tests**: Test complete workflows

### Test Structure

```
tests/
├── unit/
│   ├── agents/           # Agent tests
│   ├── memory/           # Memory system tests
│   ├── reasoning/        # Reasoning engine tests
│   └── streaming/        # Stream processing tests
├── integration/
│   ├── cli/              # CLI integration tests
│   ├── gateway/          # API gateway tests
│   └── memory/           # Memory integration tests
└── fixtures/
    ├── data/             # Test data
    └── utils/            # Test utilities
```

---

## 🚢 Deployment

### AWS Deployment

```bash
# Deploy infrastructure
cd infrastructure/aws
python deployment/deploy_full_infrastructure.py --environment prod --region us-east-1

# Deploy with blue-green strategy
./deployment/deploy_blue_green.sh production
```

### Docker Deployment

```bash
# Build Docker image
docker build -t fraud-detection:latest .

# Run container
docker run -p 8000:8000 fraud-detection:latest
```

### CI/CD

The project uses GitHub Actions for continuous integration and deployment:

- **Lint & Test**: Runs on every push and PR
- **Security Scan**: Automated security scanning
- **Deploy to Dev**: Automatic deployment to development
- **Deploy to Staging**: Automatic deployment to staging (main branch)
- **Deploy to Production**: Manual approval required

See [`.github/workflows/ci-cd.yml`](.github/workflows/ci-cd.yml) for details.

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/project/CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest tests/`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code of Conduct

Please read our [Code of Conduct](docs/project/CODE-OF-CONDUCT.md) before contributing.

---

## 📝 Migration Guide

If you're upgrading from a previous version, please see the [Migration Guide](MIGRATION.md) for detailed instructions on updating your code and configuration.

---

## 🔒 Security

Security is a top priority. Please see our [Security Policy](SECURITY.md) for:

- Reporting security vulnerabilities
- Security best practices
- Compliance information

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

---

## 🙏 Acknowledgments

- Built with [AWS Bedrock](https://aws.amazon.com/bedrock/)
- Powered by [Bedrock AgentCore SDK](https://github.com/awslabs/bedrock-agentcore)
- Inspired by industry best practices in fraud detection

---

## 📞 Support

- **Documentation**: [docs/](docs/)
- **Examples**: [examples/](examples/)
- **Issues**: [GitHub Issues](https://github.com/your-org/bedrock-agentcore-starter-toolkit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/bedrock-agentcore-starter-toolkit/discussions)

---

## 🗺️ Roadmap

- [ ] Enhanced ML model integration
- [ ] Additional specialized agents
- [ ] Multi-region deployment support
- [ ] Advanced analytics dashboard
- [ ] Mobile app integration

See the [open issues](https://github.com/your-org/bedrock-agentcore-starter-toolkit/issues) for a full list of proposed features and known issues.

---

**Made with ❤️ by the StarJam Team**
