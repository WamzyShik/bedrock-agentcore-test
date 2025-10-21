# Fraud Detection API Reference

## Overview

The Fraud Detection System provides a production-ready REST API and WebSocket interface for real-time fraud detection. It includes authentication, rate limiting, comprehensive error handling, and client SDKs.

## Base URL

```
Production: https://api.fraud-detection.example.com/v1
Staging: https://staging-api.fraud-detection.example.com/v1
Development: http://localhost:5000
```

## Quick Start

### Installation

```bash
pip install flask flask-cors flask-limiter flask-socketio
```

### Running the Server

```bash
python fraud_detection_api.py
```

The server will start on `http://localhost:5000`

### Getting Your API Key

On first startup, a default API key is automatically generated and logged to the console. Look for:

```
Default API key created: fds_...
```

You can also create additional API keys using the `/api/v1/keys` endpoint (requires admin permission).

## Authentication

All API endpoints require authentication using API keys or JWT tokens.

### API Key Authentication

**Header Format:**
```
X-API-Key: fds_your_api_key_here
```

**Permissions:**
- `read`: Access to GET endpoints (statistics, status)
- `write`: Access to POST endpoints (transaction submission)
- `admin`: Access to administrative endpoints (key creation)

### JWT Authentication

```http
Authorization: Bearer <jwt_token>
```

### Obtaining Tokens

```http
POST /auth/token
Content-Type: application/json

{
  "username": "user@example.com",
  "password": "secure_password"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600
}
```

## Rate Limiting

Default rate limits:
- **Standard endpoints**: 100 requests per minute
- **Transaction submission**: 60 requests per minute
- **Batch processing**: 10 requests per minute

Rate limits are enforced per API key. Exceeding limits returns a `429 Too Many Requests` error.

**Rate Limit Tiers:**
- **Free Tier**: 100 requests/minute
- **Standard Tier**: 1,000 requests/minute
- **Premium Tier**: 10,000 requests/minute

**Headers:**
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 950
X-RateLimit-Reset: 1642248600
```

## REST API Endpoints

### 1. Submit Transaction

Submit a single transaction for fraud detection.

**Endpoint:** `POST /api/v1/transactions`

**Alternative:** `POST /transactions/analyze`

**Authentication:** Required (write permission)

**Rate Limit:** 60 per minute

**Request Body:**
```json
{
  "id": "txn_123",
  "user_id": "user_456",
  "amount": 150.00,
  "currency": "USD",
  "merchant": "Amazon",
  "category": "retail",
  "timestamp": "2024-01-01T12:00:00Z",
  "location": {
    "country": "US",
    "city": "New York",
    "latitude": 40.7128,
    "longitude": -74.0060
  },
  "card_type": "credit",
  "device_info": {
    "device_id": "dev_001",
    "device_type": "mobile",
    "os": "iOS"
  },
  "ip_address": "192.168.1.1",
  "metadata": {
    "payment_method": "credit_card",
    "card_last_four": "1234"
  }
}
```

**Response (200 OK - Approved):**
```json
{
  "transaction_id": "txn_123",
  "decision": "APPROVE",
  "is_fraud": false,
  "confidence_score": 0.95,
  "confidence": 0.92,
  "risk_level": "LOW",
  "risk_score": 0.15,
  "reasoning": [
    "Transaction appears legitimate based on user history and patterns",
    "Amount within normal range for user",
    "Location matches user profile",
    "Device recognized"
  ],
  "explanation": "This transaction appears legitimate based on the user's historical behavior and current risk factors.",
  "evidence": [
    "Amount within normal range for user",
    "Location matches user profile",
    "Device recognized"
  ],
  "recommendations": [
    "Approve transaction"
  ],
  "factors": [
    {
      "factor": "amount_analysis",
      "score": 0.1,
      "description": "Amount is consistent with user history"
    },
    {
      "factor": "location_risk",
      "score": 0.05,
      "description": "Location is within user's typical area"
    },
    {
      "factor": "device_trust",
      "score": 0.0,
      "description": "Device is recognized and trusted"
    }
  ],
  "agent_results": [
    {
      "agent_type": "transaction_analyzer",
      "decision": "APPROVE",
      "confidence": 0.95,
      "reasoning": "Normal transaction pattern"
    },
    {
      "agent_type": "pattern_detector",
      "decision": "APPROVE",
      "confidence": 0.90,
      "reasoning": "No anomalies detected"
    },
    {
      "agent_type": "risk_assessor",
      "decision": "APPROVE",
      "confidence": 0.91,
      "reasoning": "Low risk indicators"
    }
  ],
  "processing_time_ms": 150.5,
  "timestamp": "2024-01-01T12:00:01Z"
}
```

**Response (200 OK - Fraud Detected):**
```json
{
  "transaction_id": "tx_987654321",
  "decision": "DECLINE",
  "is_fraud": true,
  "confidence": 0.88,
  "risk_level": "HIGH",
  "risk_score": 0.85,
  "reasoning": [
    "Transaction amount significantly exceeds user's average",
    "Location is in a high-risk country",
    "Device not recognized",
    "Multiple transactions in short time period"
  ],
  "explanation": "This transaction shows multiple fraud indicators including unusual location, unrecognized device, and velocity anomalies.",
  "factors": [
    {
      "factor": "amount_analysis",
      "score": 0.7,
      "description": "Amount is 10x higher than user average"
    },
    {
      "factor": "location_risk",
      "score": 0.9,
      "description": "High-risk country with no prior history"
    },
    {
      "factor": "device_trust",
      "score": 0.8,
      "description": "Unknown device, never seen before"
    },
    {
      "factor": "velocity_check",
      "score": 0.85,
      "description": "5 transactions in last 10 minutes"
    }
  ],
  "recommended_actions": [
    "Block transaction",
    "Contact user for verification",
    "Flag account for review"
  ],
  "processing_time_ms": 312,
  "timestamp": "2024-01-15T10:35:00.312Z"
}
```

**Decision Values:**
- `APPROVE`: Transaction is legitimate, approve
- `DECLINE`: Transaction is fraudulent, decline
- `FLAG`: Transaction is suspicious, flag for review
- `REVIEW`: Manual review required
- `BLOCK`: Block transaction immediately

**Risk Levels:**
- `LOW`: Low risk transaction
- `MEDIUM`: Medium risk, monitor
- `HIGH`: High risk, requires attention
- `CRITICAL`: Critical risk, immediate action needed

### 2. Batch Transaction Analysis

Analyze multiple transactions in a single request.

**Endpoint:** `POST /api/v1/transactions/batch`

**Alternative:** `POST /transactions/analyze/batch`

**Authentication:** Required (write permission)

**Rate Limit:** 10 per minute

**Request Body:**
```json
{
  "transactions": [
    {
      "transaction_id": "tx_001",
      "user_id": "user_123",
      "amount": 100.00,
      "currency": "USD",
      "merchant": "Store A"
    },
    {
      "transaction_id": "tx_002",
      "user_id": "user_456",
      "amount": 250.00,
      "currency": "USD",
      "merchant": "Store B"
    }
  ]
}
```

**Response (200 OK):**
```json
{
  "results": [
    {
      "transaction_id": "tx_001",
      "decision": "APPROVE",
      "confidence": 0.95,
      "risk_level": "LOW",
      "is_fraud": false
    },
    {
      "transaction_id": "tx_002",
      "decision": "FLAG",
      "confidence": 0.65,
      "risk_level": "MEDIUM",
      "is_fraud": false
    }
  ],
  "summary": {
    "total": 2,
    "approved": 1,
    "declined": 0,
    "flagged": 1,
    "processing_time_ms": 450
  }
}
```

### 3. Get Transaction History

Retrieve historical transaction analysis results.

**Endpoint:** `GET /api/v1/transactions/{transaction_id}`

**Alternative:** `GET /transactions/{transaction_id}`

**Authentication:** Required (read permission)

**Response (200 OK):**
```json
{
  "transaction_id": "tx_123456789",
  "user_id": "user_abc123",
  "amount": 1500.00,
  "currency": "USD",
  "decision": "APPROVE",
  "confidence": 0.92,
  "risk_level": "LOW",
  "timestamp": "2024-01-15T10:30:00Z",
  "reasoning": ["Transaction appears legitimate"],
  "factors": [
    {
      "factor": "amount_analysis",
      "score": 0.1,
      "description": "Amount is consistent with user history"
    }
  ]
}
```

### 4. Get User Risk Profile

Retrieve a user's risk profile and behavior patterns.

**Endpoint:** `GET /api/v1/users/{user_id}/profile`

**Alternative:** `GET /users/{user_id}/profile`

**Authentication:** Required (read permission)

**Response (200 OK):**
```json
{
  "user_id": "user_abc123",
  "risk_score": 0.15,
  "risk_level": "LOW",
  "account_age_days": 365,
  "total_transactions": 1250,
  "fraud_incidents": 0,
  "average_transaction_amount": 125.50,
  "typical_locations": ["New York, US", "Boston, US"],
  "typical_merchants": ["Grocery Store", "Gas Station", "Online Store"],
  "typical_devices": ["device_xyz789"],
  "behavior_patterns": {
    "transaction_frequency": "daily",
    "preferred_time": "business_hours",
    "spending_pattern": "consistent"
  },
  "last_updated": "2024-01-15T10:30:00Z"
}
```

### 5. Update User Profile

Update user profile information.

**Endpoint:** `PUT /api/v1/users/{user_id}/profile`

**Alternative:** `PUT /users/{user_id}/profile`

**Authentication:** Required (write permission)

**Request Body:**
```json
{
  "typical_locations": ["New York, US", "Boston, US", "San Francisco, US"],
  "notification_preferences": {
    "email": true,
    "sms": true,
    "push": false
  }
}
```

**Response (200 OK):**
```json
{
  "user_id": "user_abc123",
  "updated": true,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### 6. Get System Health

Check system health and status.

**Endpoint:** `GET /api/v1/health`

**Alternative:** `GET /health`

**Authentication:** Not required

**Response (200 OK):**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00Z",
  "components": {
    "api": "healthy",
    "database": "healthy",
    "agents": "healthy",
    "bedrock": "healthy",
    "streaming": "healthy"
  },
  "metrics": {
    "requests_per_second": 850,
    "average_response_time_ms": 245,
    "error_rate": 0.001
  }
}
```

### 7. Get System Metrics

Retrieve system performance metrics.

**Endpoint:** `GET /api/v1/metrics`

**Alternative:** `GET /metrics`

**Authentication:** Required (read permission)

**Response (200 OK):**
```json
{
  "period": "last_hour",
  "metrics": {
    "total_transactions": 50000,
    "approved": 45000,
    "declined": 3000,
    "flagged": 2000,
    "average_response_time_ms": 245,
    "p95_response_time_ms": 450,
    "p99_response_time_ms": 850,
    "throughput_tps": 850,
    "error_rate": 0.001,
    "decision_accuracy": 0.92,
    "false_positive_rate": 0.05,
    "false_negative_rate": 0.02
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### 8. Get System Statistics

Retrieve overall system statistics.

**Endpoint:** `GET /api/v1/statistics`

**Authentication:** Required (read permission)

**Response (200 OK):**
```json
{
  "total_transactions_processed": 1000000,
  "fraud_detected": 50000,
  "fraud_rate": 0.05,
  "average_confidence": 0.87,
  "uptime_percentage": 99.9,
  "last_updated": "2024-01-15T10:30:00Z"
}
```

## WebSocket API

### Real-Time Transaction Monitoring

Connect to WebSocket for real-time transaction updates.

**Endpoint:** `wss://api.fraud-detection.example.com/ws/transactions`

**Alternative:** `ws://localhost:5000/socket.io/`

**Authentication:** Required via initial message

```javascript
const ws = new WebSocket('wss://api.fraud-detection.example.com/ws/transactions');

// Authentication
ws.onopen = () => {
  ws.send(JSON.stringify({
    type: 'auth',
    token: 'your_jwt_token'
  }));
};

// Subscribe to user transactions
ws.send(JSON.stringify({
  type: 'subscribe',
  user_id: 'user_abc123'
}));

// Receive updates
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Transaction update:', data);
};
```

**Message Format:**
```json
{
  "type": "transaction_update",
  "transaction_id": "tx_123456789",
  "user_id": "user_abc123",
  "decision": "APPROVE",
  "confidence": 0.92,
  "risk_level": "LOW",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## Error Responses

All error responses follow a consistent format:

```json
{
  "error": "error_code",
  "message": "Human-readable error message",
  "details": {},
  "request_id": "req_abc123"
}
```

### Error Codes

| Code | Status | Description |
|------|--------|-------------|
| `validation_error` | 400 | Invalid input data |
| `unauthorized` | 401 | Invalid or missing authentication |
| `forbidden` | 403 | Insufficient permissions |
| `not_found` | 404 | Resource doesn't exist |
| `rate_limit_exceeded` | 429 | Rate limit exceeded |
| `internal_error` | 500 | Internal server error |
| `service_unavailable` | 503 | Temporary service outage |

### Example Error Responses

**400 Bad Request:**
```json
{
  "error": "validation_error",
  "message": "Invalid transaction data",
  "details": {
    "amount": "Must be a positive number",
    "currency": "Must be a valid ISO currency code"
  }
}
```

**401 Unauthorized:**
```json
{
  "error": "unauthorized",
  "message": "Invalid or expired token"
}
```

**429 Too Many Requests:**
```json
{
  "error": "rate_limit_exceeded",
  "message": "Rate limit exceeded. Try again in 60 seconds.",
  "retry_after": 60
}
```

**500 Internal Server Error:**
```json
{
  "error": "internal_error",
  "message": "An unexpected error occurred",
  "request_id": "req_abc123"
}
```

## SDKs and Client Libraries

### Python SDK

```python
from fraud_detection_sdk import FraudDetectionClient

client = FraudDetectionClient(
    api_key='your_api_key',
    environment='production'
)

# Analyze transaction
result = client.analyze_transaction({
    'transaction_id': 'tx_123',
    'user_id': 'user_abc',
    'amount': 1500.00,
    'currency': 'USD'
})

print(f"Decision: {result.decision}")
print(f"Confidence: {result.confidence}")
```

### JavaScript SDK

```javascript
import { FraudDetectionClient } from '@fraud-detection/sdk';

const client = new FraudDetectionClient({
  apiKey: 'your_api_key',
  environment: 'production'
});

// Analyze transaction
const result = await client.analyzeTransaction({
  transaction_id: 'tx_123',
  user_id: 'user_abc',
  amount: 1500.00,
  currency: 'USD'
});

console.log(`Decision: ${result.decision}`);
console.log(`Confidence: ${result.confidence}`);
```

## Webhooks

Configure webhooks to receive notifications for fraud events.

### Webhook Configuration

**Endpoint:** `POST /api/v1/webhooks`

**Authentication:** Required (admin permission)

**Request Body:**
```json
{
  "url": "https://your-app.com/webhooks/fraud",
  "events": ["fraud_detected", "high_risk_transaction"],
  "secret": "your_webhook_secret"
}
```

**Response (201 Created):**
```json
{
  "webhook_id": "wh_abc123",
  "url": "https://your-app.com/webhooks/fraud",
  "events": ["fraud_detected", "high_risk_transaction"],
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Webhook Payload

```json
{
  "event": "fraud_detected",
  "transaction_id": "tx_987654321",
  "user_id": "user_xyz789",
  "decision": "DECLINE",
  "confidence": 0.88,
  "risk_level": "HIGH",
  "timestamp": "2024-01-15T10:35:00Z",
  "signature": "sha256=..."
}
```

### Verifying Webhook Signatures

```python
import hmac
import hashlib

def verify_webhook(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)
```

## Best Practices

### 1. Error Handling

Always handle errors gracefully:

```python
try:
    result = client.analyze_transaction(transaction)
except RateLimitError as e:
    # Wait and retry
    time.sleep(e.retry_after)
    result = client.analyze_transaction(transaction)
except ValidationError as e:
    # Fix input and retry
    print(f"Invalid input: {e.details}")
except APIError as e:
    # Log and alert
    logger.error(f"API error: {e.message}")
```

### 2. Caching

Cache user profiles to reduce API calls:

```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def get_user_profile(user_id):
    return client.get_user_profile(user_id)
```

### 3. Batch Processing

Use batch endpoints for multiple transactions:

```python
# Instead of multiple calls
for tx in transactions:
    result = client.analyze_transaction(tx)

# Use batch endpoint
results = client.analyze_batch(transactions)
```

### 4. Async Processing

Use async for better performance:

```python
import asyncio

async def analyze_transactions(transactions):
    tasks = [
        client.analyze_transaction_async(tx)
        for tx in transactions
    ]
    return await asyncio.gather(*tasks)
```

### 5. Retry Logic

Implement exponential backoff for retries:

```python
import time
from random import random

def retry_with_backoff(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError as e:
            if attempt == max_retries - 1:
                raise
            wait_time = (2 ** attempt) + random()
            time.sleep(wait_time)
```

### 6. Connection Pooling

Use connection pooling for better performance:

```python
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.3)
adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=20)
session.mount('https://', adapter)
```

## Performance Considerations

### Response Times

- **Average**: 150-250ms
- **P95**: 400-500ms
- **P99**: 800-1000ms

### Throughput

- **Standard**: 850 transactions/second
- **Peak**: 2000 transactions/second
- **Batch**: 5000 transactions/second

### Optimization Tips

1. Use batch endpoints for multiple transactions
2. Cache user profiles and risk data
3. Use async/await for concurrent requests
4. Implement connection pooling
5. Use WebSocket for real-time updates
6. Enable compression for large payloads

## Support and Resources

### Documentation
- API Reference: https://docs.fraud-detection.example.com/api
- User Guides: https://docs.fraud-detection.example.com/guides
- Architecture: https://docs.fraud-detection.example.com/architecture

### Support Channels
- Email: api-support@fraud-detection.example.com
- Status Page: https://status.fraud-detection.example.com
- GitHub Issues: https://github.com/fraud-detection/issues

### Additional Resources
- Postman Collection: [Download](https://docs.fraud-detection.example.com/postman)
- OpenAPI Spec: [Download](https://docs.fraud-detection.example.com/openapi.yaml)
- Code Examples: https://github.com/fraud-detection/examples
