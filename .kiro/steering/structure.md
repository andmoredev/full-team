# AWS Serverless Project Structure Standards

## Overview

This document outlines the folder structure and organizational standards for AWS serverless applications. These standards follow AWS Serverless Best Practices and implement a clean separation between frontend and backend concerns, enabling consistency across multiple projects.

## Root Directory Structure

```
project-name/
├── backend/                 # Node.js serverless backend
├── frontend/               # React.js frontend application
├── infrastructure/         # IaC resources
├── docs/                   # Project documentation
├── scripts/                # Build and deployment scripts
├── .github/                # GitHub Actions workflows
├── package.json            # Root package.json for workspace management
├── .gitignore              # Git ignore patterns
└── README.md               # Project documentation
```

## Backend Structure Standards

The backend follows AWS Serverless Best Practices with a focus on maintainability and scalability:

```
backend/
├── src/
│   ├── functions/          # Lambda function implementations
├── docs/                   # Documentation and images
├── portman/                # API testing configuration
├── coverage/               # Test coverage reports
├── tmp/                    # Temporary build artifacts
├── package.json            # Backend dependencies and scripts
├── openapi.yaml            # OpenAPI 3.0 specification
└── eslint.config.mjs       # ESLint configuration
```

### Lambda Function Organization

Lambda functions are organized by domain/resource type following single-responsibility principle:

```
src/functions/
├── [domain-1]/              # Business domain grouping (e.g., users, orders, products)
│   ├── create-[resource]/
│   │   ├── index.mjs        # Main Lambda handler
│   │   └── tests/           # Unit tests for this function
│   ├── get-[resource]/
│   ├── get-[resources]/     # List/search endpoints
│   ├── update-[resource]/
│   ├── delete-[resource]/
│   └── [custom-operation]/  # Domain-specific operations
├── [domain-2]/
│   ├── create-[resource]/
│   ├── get-[resource]/
│   └── [custom-operations]/
└── shared/                  # Cross-domain shared utilities
```

**Example Implementation:**

```
src/functions/
├── users/
│   ├── create-user/
│   ├── get-user/
│   ├── get-users/
│   ├── update-user/
│   ├── delete-user/
│   └── reset-password/
├── orders/
│   ├── create-order/
│   ├── get-order/
│   ├── get-orders/
│   ├── update-order/
│   ├── cancel-order/
│   └── process-payment/
└── shared/
```

### Multi-Agent System Organization

For multi-agent systems using Amazon Bedrock AgentCore and AWS Strands SDK:

#### Amazon Bedrock AgentCore Services

- **Runtime**: Secure, serverless runtime for deploying and scaling AI agents
- **Identity**: Secure agent identity and access management with credential providers
- **Memory**: Short-term and long-term memory for context-aware agents
- **Gateway**: Secure tool discovery and API transformation for agent integration
- **Observability**: Tracing, debugging, and monitoring agent performance

#### AWS Strands SDK

- Open-source framework with model-first approach for building autonomous agents
- Native support for Model Context Protocol (MCP)
- Integration with Amazon Bedrock, AWS Lambda, and other AWS services
- Support for multiple foundation models (Claude, Nova, etc.)

```
src/functions/
├── agents/                 # AI agent implementations
│   ├── calculator-agent/
│   │   ├── index.mjs       # Agent Lambda handler
│   │   ├── agent-config.json # Bedrock AgentCore configuration
│   │   └── tests/          # Unit tests
│   ├── nutritionist-agent/
│   │   ├── index.mjs
│   │   ├── agent-config.json
│   │   └── tests/
│   ├── calorie-calculator-agent/
│   ├── meal-prep-coach-agent/
│   ├── progress-tracker-agent/
│   ├── motivator-agent/
│   └── shared-agent-utils/ # Common agent utilities
├── workflows/              # AgentCore Runtime workflow definitions
│   ├── health-assessment-workflow/
│   │   ├── index.mjs       # Workflow orchestration handler
│   │   ├── workflow-definition.json # AgentCore Runtime workflow config
│   │   └── tests/
│   ├── meal-planning-workflow/
│   └── progress-tracking-workflow/
├── api/                    # Traditional API endpoints
│   ├── health-profile/
│   ├── user-preferences/
│   └── system-status/
└── shared/                 # Cross-domain shared utilities
    ├── agent-communication/ # Agent-to-agent communication utilities
    ├── workflow-utils/     # AgentCore Runtime workflow utilities
    ├── agentcore-clients/  # AgentCore service clients
    └── strands-utils/      # AWS Strands SDK utilities
```

### Agent Configuration Structure

Each agent should include standardized configuration:

```
src/functions/agents/[agent-name]/
├── index.mjs               # Lambda handler for agent
├── agent-config.json       # AgentCore Runtime configuration
├── prompts/               # Agent-specific prompts and instructions
│   ├── system-prompt.txt
│   ├── user-interaction-prompts.txt
│   └── error-handling-prompts.txt
├── schemas/               # Input/output schemas for agent
│   ├── input-schema.json
│   └── output-schema.json
└── tests/
    ├── index.test.mjs     # Unit tests
    └── fixtures/          # Test data and mocks
```

### Workflow Organization

AgentCore Runtime workflows should be organized by business process:

```
src/functions/workflows/[workflow-name]/
├── index.mjs              # Workflow orchestration handler
├── workflow-definition.json # AgentCore Runtime workflow configuration
├── steps/                 # Individual workflow steps
│   ├── step-1-validation.mjs
│   ├── step-2-agent-coordination.mjs
│   └── step-3-result-aggregation.mjs
└── tests/
    ├── workflow.test.mjs  # Workflow integration tests
    └── steps/             # Individual step tests
```

### Shared Modules Structure

Shared utilities promote code reuse and consistency:

```
src/shared/
├── apigateway/             # API Gateway response utilities
├── data-access/            # Database access layer
├── dynamodb/               # DynamoDB utilities and configuration
├── lambda-powertools/      # AWS Lambda Powertools setup
├── models/                 # Data models and validation schemas
├── agent-communication/    # Agent-to-agent communication utilities
├── workflow-utils/         # AgentCore Runtime workflow utilities
└── agentcore-clients/      # Amazon Bedrock AgentCore service clients
```

## Frontend Structure Standards

The frontend follows React.js best practices with a component-based architecture:

```
frontend/
├── public/
│   ├── index.html          # Main HTML template
│   ├── favicon.ico         # Application favicon
│   └── [app-assets]/       # Static assets (images, icons)
├── src/
│   ├── components/         # Reusable React components
│   │   ├── [Component].js  # Feature-specific components
│   │   ├── [Component].css # Component styles
│   │   └── common/         # Shared/common components
│   ├── pages/              # Route-based page components
│   │   ├── [PageName].js
│   │   └── [PageName].css
│   ├── services/           # API integration layer
│   │   ├── api.js          # Centralized API client
│   │   └── [domain]Api.js  # Domain-specific API modules
│   ├── hooks/              # Custom React hooks
│   ├── utils/              # Utility functions
│   ├── context/            # React context providers
│   ├── constants/          # Application constants
│   ├── App.js              # Main application component
│   ├── index.js            # Application entry point
│   └── App.css             # Global styles
├── build/                  # Production build artifacts
├── package.json            # Frontend dependencies
└── README.md               # Frontend-specific documentation
```

## File Naming Conventions

### Backend (Node.js/Lambda)

- **Lambda handlers**: `index.mjs` (ESM modules)
- **Test files**: `*.test.mjs` or organized in `tests/` folders
- **Configuration**: `*.yaml` for CloudFormation/SAM, `*.json` for API specs
- **Shared modules**: Descriptive names following camelCase

### Frontend (React)

- **Components**: PascalCase (e.g., `UserForm.js`, `OrderList.js`)
- **Pages**: PascalCase (e.g., `Dashboard.js`, `UserProfile.js`)
- **Services**: camelCase (e.g., `api.js`, `userApi.js`)
- **Hooks**: camelCase with `use` prefix (e.g., `useAuth.js`, `useApi.js`)
- **Utils**: camelCase (e.g., `formatDate.js`, `validation.js`)
- **Styles**: Match component/page name (e.g., `UserForm.css`)
- **Test files**: `*.test.js` or `*.spec.js`

## Configuration Management

### Environment-Specific Configuration

- **Development**: Local configuration files and environment variables
- **Staging/Production**: AWS Systems Manager Parameter Store or AWS Secrets Manager
- **API Configuration**: Centralized in `frontend/src/services/api.js`
- **Environment Files**: `.env.local`, `.env.development`, `.env.production`

### Build Configuration

- **Backend**: SAM template (`template.yaml`) with build specifications
- **Frontend**: React build process with environment-specific builds
- **CI/CD**: GitHub Actions workflows
- **Infrastructure**: SAM templates in `infrastructure/` folder

## Testing Organization

### Backend Testing

```
backend/src/functions/[function-name]/tests/
├── unit.test.mjs           # Unit tests
├── integration.test.mjs    # Integration tests
└── fixtures/               # Test data and mocks
```

### Frontend Testing

```
frontend/src/
├── components/
│   ├── [ComponentName]/
│   │   ├── index.js        # Component implementation
│   │   ├── [ComponentName].test.js
│   │   └── [ComponentName].css
│   └── common/
│       ├── [SharedComponent].js
│       └── [SharedComponent].test.js
├── pages/
│   ├── [PageName].js
│   └── [PageName].test.js
├── services/
│   ├── api.js
│   ├── api.test.js
│   └── [domainApi].test.js
└── hooks/
    ├── [hookName].js
    └── [hookName].test.js
```

## Documentation Standards

### Code Documentation

- **README.md**: Project overview, setup instructions, and usage
- **API Documentation**: Generated from OpenAPI specification
- **Component Documentation**: JSDoc comments for complex components
- **Function Documentation**: Clear function descriptions and parameter documentation
- **Architecture Diagrams**: System architecture and data flow diagrams

### Architecture Documentation

- **Flow Diagrams**: Visual representation of data flow
- **API Specifications**: OpenAPI 3.0 complete documentation
- **Deployment Guides**: Step-by-step deployment instructions
- **Infrastructure Diagrams**: AWS architecture diagrams
- **Decision Records**: Architectural Decision Records (ADRs) for significant decisions

## Dependencies Management

### Backend Dependencies

- **Runtime**: Node.js 22.x with ESM modules
- **AWS SDK**: Latest v3 SDK with specific service clients
- **Testing**: Vitest, c8 for coverage
- **Utilities**: AWS Lambda Powertools for observability

### Frontend Dependencies

- **Framework**: React.js with modern hooks
- **HTTP Client**: Fetch API
- **State Management**: Context API, Redux
- **UI Library**: Tailwind CSS
- **Testing**: React Testing Library, Jest
- **Build Tools**: Create React App, Vite, or custom Webpack configuration

## Security and Compliance

### File Security

- **Secrets**: Never commit secrets; use environment variables
- **API Keys**: Stored in AWS Systems Manager Parameter Store
- **Sensitive Data**: Excluded via `.gitignore` patterns

### Access Control

- **IAM Roles**: Least privilege principle for Lambda execution
- **API Security**: AWS Cognito User Pools, API Keys, or custom authorizers
- **CORS**: Proper configuration for cross-origin requests
- **Resource Policies**: S3 bucket policies, DynamoDB access policies

## Build and Deployment

### Backend Deployment

- **SAM CLI**: For local development and testing
- **SAM**: Infrastructure as Code
- **CI/CD**: GitHub Actions
- **Multi-Environment**: Separate deployments for dev/staging/production

### Frontend Deployment

- **S3 + CloudFront**: Static site hosting with CDN
- **Environment Variables**: Build-time configuration
- **Static Assets**: Optimized for CDN delivery

## Maintenance Standards

### Code Quality

- **Linting**: ESLint for JavaScript/Node.js code and frontend code
- **Formatting**: Consistent code formatting rules
- **Type Safety**: JSDoc comments for type documentation

### Monitoring

- **Logs**: Structured logging with Lambda Powertools
- **Metrics**: Custom CloudWatch metrics
- **Alerts**: CloudWatch alarms for critical issues

### Updates

- **Dependencies**: Regular updates with security audits
- **Runtime**: Keep Lambda runtime updated
- **API Versions**: Semantic versioning for API changes

## Best Practices Summary

1. **Separation of Concerns**: Clear boundaries between frontend and backend
2. **Single Responsibility**: One Lambda function per API endpoint
3. **Code Reusability**: Shared modules for common functionality
4. **Testing**: Comprehensive unit and integration tests
5. **Documentation**: Keep documentation current with code changes
6. **Security**: Follow AWS security best practices
7. **Monitoring**: Implement comprehensive observability
8. **Scalability**: Design for growth and high availability

## Domain-Specific Patterns

### E-commerce Applications

```
src/functions/
├── products/
│   ├── create-product/
│   ├── get-product/
│   ├── search-products/
│   └── update-inventory/
├── orders/
│   ├── create-order/
│   ├── process-payment/
│   └── update-status/
├── users/
│   ├── register-user/
│   ├── authenticate/
│   └── update-profile/
└── analytics/
    ├── track-event/
    └── generate-report/
```

### Content Management Systems

```
src/functions/
├── content/
│   ├── create-article/
│   ├── publish-content/
│   └── moderate-content/
├── media/
│   ├── upload-file/
│   ├── process-image/
│   └── generate-thumbnail/
├── users/
│   ├── manage-permissions/
│   └── audit-actions/
└── notifications/
    ├── send-email/
    └── push-notification/
```

### Data Processing Applications

```
src/functions/
├── ingestion/
│   ├── receive-data/
│   ├── validate-format/
│   └── queue-processing/
├── processing/
│   ├── transform-data/
│   ├── enrich-data/
│   └── aggregate-metrics/
├── storage/
│   ├── save-to-warehouse/
│   └── archive-data/
└── reporting/
    ├── generate-dashboard/
    └── export-report/
```

## Using This Template

### For New Projects

1. **Replace placeholders** with your specific domain terms:

   - `[domain]` → your business domain (e.g., `users`, `products`, `content`)
   - `[resource]` → your resource types (e.g., `user`, `product`, `article`)
   - `[app-assets]` → your application name and assets

2. **Choose your domain pattern** from the examples provided or create your own

3. **Adapt folder structure** to your specific needs while maintaining the core principles

### For Existing Projects

1. **Gradually migrate** to this structure during refactoring cycles
2. **Prioritize high-impact areas** like shared utilities and configuration
3. **Update documentation** to match the new structure
4. **Ensure team alignment** on the new standards

## Multi-Agent System Patterns

### Health Management Agent Examples

For the health management multi-agent system, here are specific domain patterns:

```
src/functions/
├── agents/
│   ├── calculator-agent/           # BMI, calorie calculations
│   │   ├── index.mjs
│   │   ├── agent-config.json
│   │   ├── prompts/
│   │   │   ├── calculation-prompts.txt
│   │   │   └── validation-prompts.txt
│   │   └── tests/
│   ├── nutritionist-agent/         # Meal planning and nutrition advice
│   │   ├── index.mjs
│   │   ├── agent-config.json
│   │   ├── prompts/
│   │   │   ├── meal-planning-prompts.txt
│   │   │   ├── cultural-adaptation-prompts.txt
│   │   │   └── dietary-restriction-prompts.txt
│   │   └── tests/
│   ├── calorie-calculator-agent/   # Photo-based calorie estimation
│   │   ├── index.mjs
│   │   ├── agent-config.json
│   │   ├── prompts/
│   │   │   ├── image-analysis-prompts.txt
│   │   │   └── calorie-estimation-prompts.txt
│   │   └── tests/
│   ├── meal-prep-coach-agent/      # Grocery lists and prep schedules
│   ├── progress-tracker-agent/     # Weight and progress tracking
│   ├── motivator-agent/            # Encouragement and accountability
│   └── shared-agent-utils/
│       ├── agentcore-client.mjs
│       ├── strands-client.mjs
│       ├── agent-communication.mjs
│       └── prompt-templates.mjs
├── workflows/
│   ├── health-assessment-workflow/ # Initial user assessment
│   │   ├── index.mjs
│   │   ├── workflow-definition.json
│   │   └── steps/
│   │       ├── collect-user-data.mjs
│   │       ├── calculate-metrics.mjs
│   │       └── generate-recommendations.mjs
│   ├── meal-planning-workflow/     # Weekly meal planning process
│   │   ├── index.mjs
│   │   ├── workflow-definition.json
│   │   └── steps/
│   │       ├── analyze-preferences.mjs
│   │       ├── generate-meal-plan.mjs
│   │       ├── create-grocery-list.mjs
│   │       └── schedule-prep-tasks.mjs
│   └── progress-tracking-workflow/ # Regular progress assessment
└── api/
    ├── user-profile/
    ├── health-metrics/
    ├── meal-logs/
    └── progress-reports/
```

### Agent Communication Patterns

Agents should follow these communication patterns:

1. **Event-Driven Communication**: Agents communicate through AWS EventBridge or SQS
2. **Workflow Orchestration**: Amazon Bedrock AgentCore Runtime coordinates multi-agent workflows
3. **State Management**: DynamoDB stores agent state and conversation history
4. **Result Sharing**: Agents share results through standardized data contracts

### Configuration Management for Agents

Each agent should have environment-specific configuration:

```
src/functions/agents/[agent-name]/
├── config/
│   ├── dev.json            # Development environment config
│   ├── staging.json        # Staging environment config
│   └── prod.json           # Production environment config
├── prompts/
│   ├── system-prompts/     # Core agent behavior prompts
│   ├── interaction-prompts/ # User interaction prompts
│   └── error-prompts/      # Error handling prompts
└── schemas/
    ├── input-validation.json
    ├── output-format.json
    └── agent-metadata.json
```

This structure ensures that each agent is:

- Independently deployable and testable
- Properly configured for different environments
- Following consistent patterns for maintainability
- Integrated with the overall workflow orchestration system
