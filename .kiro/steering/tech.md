# Technology Stack

## Core Technologies

- Programming Languages: Node.js 22.x (ESM modules)
- AI/ML Platform: Amazon Bedrock AgentCore (Runtime, Identity, Memory, Gateway, Observability)
- Agent Framework: AWS Strands SDK (open-source agent development framework)
- Agent Runtime: Amazon Bedrock AgentCore Runtime (for AI agents)
- API Runtime: AWS Lambda (arm64 architecture, for APIs and data processing)
- API: AWS API Gateway with OpenAPI 3.0
- Database: Amazon DynamoDB
- Authentication: AWS Cognito (planned)

## Build System

- Build Tool: SAM (Serverless Application Model)
- Package Manager: npm
- Bundler: ESBuild (optimized for Lambda)
- Infrastructure as Code: SAM Templates

## Development Environment

- Required Tools: AWS CLI, SAM CLI, Node.js 22.x, npm
- Recommended IDE/Editor: VS Code with AWS extensions
- Testing Framework: Vitest
- Linting: ESLint
- Code Coverage: c8

## AI and Agent Technologies

- Amazon Bedrock AgentCore Runtime: Secure, serverless runtime for deploying and scaling AI agents
- Amazon Bedrock AgentCore Identity: Secure agent identity and access management
- Amazon Bedrock AgentCore Memory: Context-aware agents with short-term and long-term memory
- Amazon Bedrock AgentCore Gateway: Secure tool discovery and API transformation
- Amazon Bedrock AgentCore Observability: Tracing, debugging, and monitoring agent performance
- AWS Strands SDK: Open-source framework for building autonomous AI agents with model-first approach
- Lambda Powertools: Observability and structured logging

## Common Commands

### Setup

```bash
# Install dependencies
npm install

# Install SAM CLI (if not already installed)
# macOS: brew install aws-sam-cli
# Other: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
```

### Build

```bash
# Build SAM application
sam build

# Validate SAM template
sam validate

# Lint SAM template
sam validate --lint
```

### Test

```bash
# Run unit tests
npm test

# Run tests with coverage
npm run test:coverage

# Run linting
npm run lint
```

### Deploy

```bash
# Deploy to development
sam deploy --config-env dev

# Deploy to staging
sam deploy --config-env staging

# Deploy to production
sam deploy --config-env prod
```

## Dependencies

- @aws-lambda-powertools/logger: Structured logging
- @aws-lambda-powertools/tracer: Distributed tracing
- @aws-lambda-powertools/metrics: Custom metrics
- @middy/core: Lambda middleware engine
- aws-sdk (v3): AWS service clients
- vitest: Testing framework
- c8: Code coverage

## Version Requirements

- Node.js: 22.x LTS
- AWS CLI: Latest
- SAM CLI: Latest
- npm: 10.x or higher

## Agent-Specific Technologies

### Amazon Bedrock AgentCore Services

- **AgentCore Runtime**: Secure, serverless runtime for deploying and scaling AI agents with extended runtime support, fast cold starts, and session isolation
- **AgentCore Identity**: Secure agent identity and access management with credential providers and just-enough access principles
- **AgentCore Memory**: Context-aware agents with short-term conversation memory and long-term memory shared across agents and sessions
- **AgentCore Gateway**: Secure tool discovery and API transformation, converting Lambda functions and services into agent-compatible tools
- **AgentCore Code Interpreter**: Secure code execution in isolated sandbox environments for data analysis and complex workflows
- **AgentCore Browser**: Cloud-based browser runtime for agents to interact with websites at scale
- **AgentCore Observability**: Unified operational dashboards with OpenTelemetry support for tracing, debugging, and monitoring

### AWS Strands SDK

- Open-source framework with model-first approach for building autonomous AI agents
- Native Model Context Protocol (MCP) integration for standardized context provision
- Support for multiple frameworks: LangGraph, CrewAI, and native Strands agents
- Foundation model flexibility: Claude, Amazon Nova (Premier, Pro, Lite, Micro), OpenAI, and others
- Multimodal capabilities: text, speech, and image processing
- AWS service integration: Amazon Bedrock, Lambda, Step Functions, and more
