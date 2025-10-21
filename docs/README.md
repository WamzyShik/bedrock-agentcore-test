# Documentation

Welcome to the Fraud Detection System documentation! This directory contains comprehensive documentation covering architecture, APIs, guides, operations, and project information.

## 📚 Quick Navigation

### 🏗️ Architecture
Learn about the system design and technical architecture.

- **[System Architecture](architecture/ARCHITECTURE.md)** - Complete system architecture overview
- **[README](architecture/README.md)** - Architecture documentation index

### 🔌 API Reference
Complete API documentation for developers.

- **[API Reference](api/API_REFERENCE.md)** - REST API and WebSocket documentation
- Endpoints, authentication, rate limiting, and examples
- SDKs and client libraries

### 📖 User Guides
Step-by-step guides to get you started and deploy the system.

- **[Getting Started](guides/getting-started.md)** - Quick start guide for new users
- **[Deployment Guide](guides/deployment-guide.md)** - Deploy to production environments
- Installation, configuration, and basic usage

### ⚙️ Operations
Operational procedures and troubleshooting.

- **[Operations Runbook](operations/OPERATIONS_RUNBOOK.md)** - Day-to-day operations guide
- **[Troubleshooting](operations/TROUBLESHOOTING.md)** - Common issues and solutions
- Monitoring, maintenance, and incident response

### 📋 Project Information
Project policies and contribution guidelines.

- **[Contributing](project/CONTRIBUTING.md)** - How to contribute to the project
- **[Code of Conduct](project/CODE-OF-CONDUCT.md)** - Community guidelines
- **[Changelog](project/CHANGELOG.md)** - Version history and changes
- **[Security Policy](../SECURITY.md)** - Security reporting and policies

### 🔒 Security
Security documentation and best practices.

- **[Security Documentation](SECURITY.md)** - Security architecture and measures
- Authentication, encryption, compliance, and best practices

## 🚀 Getting Started

New to the Fraud Detection System? Start here:

1. **[Getting Started Guide](guides/getting-started.md)** - Installation and basic usage
2. **[API Reference](api/API_REFERENCE.md)** - Learn the API
3. **[Architecture](architecture/ARCHITECTURE.md)** - Understand the system design
4. **[Deployment Guide](guides/deployment-guide.md)** - Deploy to production

## 📊 Key Features

### Real-Time Fraud Detection
- Multi-agent AI system powered by AWS Bedrock
- Real-time transaction analysis
- Adaptive reasoning and pattern learning
- Explainable AI decisions

### Production-Ready API
- REST API with authentication and rate limiting
- WebSocket support for real-time updates
- Comprehensive error handling
- Client SDKs for Python and JavaScript

### Monitoring & Dashboards
- Admin dashboard for infrastructure monitoring
- Agent dashboard for AI agent performance
- Analytics dashboard for fraud metrics
- Real-time metrics streaming

### AWS Integration
- AWS Bedrock for AI agents
- DynamoDB for data storage
- Kinesis for event streaming
- CloudWatch for monitoring

## 🔍 Finding What You Need

### For Developers
- Start with [Getting Started](guides/getting-started.md)
- Review [API Reference](api/API_REFERENCE.md)
- Check [Architecture](architecture/ARCHITECTURE.md) for system design
- See [examples](../examples/) for code samples

### For DevOps Engineers
- Read [Deployment Guide](guides/deployment-guide.md)
- Review [Operations Runbook](operations/OPERATIONS_RUNBOOK.md)
- Check [Troubleshooting](operations/TROUBLESHOOTING.md)
- See [infrastructure](../infrastructure/) for deployment configs

### For Contributors
- Read [Contributing Guidelines](project/CONTRIBUTING.md)
- Follow [Code of Conduct](project/CODE-OF-CONDUCT.md)
- Check [Security Policy](../SECURITY.md) for reporting issues
- Review [Changelog](project/CHANGELOG.md) for recent changes

### For Security Researchers
- Review [Security Documentation](SECURITY.md)
- Report vulnerabilities via [Security Policy](../SECURITY.md)
- Check authentication and authorization docs in [API Reference](api/API_REFERENCE.md)

## 📁 Documentation Structure

```
docs/
├── README.md                    # This file - documentation index
├── SECURITY.md                  # Security architecture and measures
├── architecture/                # System architecture documentation
│   ├── ARCHITECTURE.md         # Complete architecture overview
│   └── README.md               # Architecture index
├── api/                        # API documentation
│   └── API_REFERENCE.md        # Complete API reference
├── guides/                     # User guides
│   ├── getting-started.md      # Quick start guide
│   └── deployment-guide.md     # Deployment instructions
├── operations/                 # Operations documentation
│   ├── OPERATIONS_RUNBOOK.md   # Operations procedures
│   └── TROUBLESHOOTING.md      # Troubleshooting guide
└── project/                    # Project meta-documentation
    ├── CONTRIBUTING.md         # Contribution guidelines
    ├── CODE-OF-CONDUCT.md      # Community guidelines
    └── CHANGELOG.md            # Version history
```

## 🛠️ Building Documentation

This documentation can be built into a static site using MkDocs:

```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Serve locally
mkdocs serve

# Build static site
mkdocs build
```

## 📝 Documentation Standards

When contributing to documentation:

- Use clear, concise language
- Include code examples where appropriate
- Keep documentation up-to-date with code changes
- Follow the existing structure and formatting
- Add links to related documentation

## 🆘 Need Help?

- **Issues**: [GitHub Issues](https://github.com/your-org/fraud-detection-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/fraud-detection-system/discussions)
- **Email**: support@fraud-detection.example.com

## 📄 License

See [LICENSE.txt](../LICENSE.txt) for license information.

---

**Last Updated**: 2025-10-21  
**Documentation Version**: 1.0.0
