# Product Overview

This repository contains a multi-agent collaboration system for personalized health and weight management, built using AWS serverless technologies including Amazon Bedrock AgentCore and AWS Strands.

## Purpose

Transform weight management from rigid, one-size-fits-all approaches to personalized, adaptive, and engaging AI-powered guidance through a collaborative team of specialized agents.

## Problem Statement

Millions struggle with weight management due to:

- Rigid calorie trackers requiring manual input
- Generic meal plans that don't consider personal preferences or culture
- Low motivation from lack of personalization and engagement
- One-size-fits-all approaches that don't adapt to individual needs

## Solution: An AI Team for Your Health
Instead of one monolithic app, we present a team of AI agents that collaborate to provide comprehensive, personalized health guidance:

### Core Agents

1. **Calculator Agent** → Determines ideal weight, BMI, daily calories based on personal metrics
2. **Nutritionist Agent** → Generates culturally relevant, personalized weekly meal plans
3. **Calorie Calculator Agent** → Estimates calories from photos of meals using computer vision
4. **Meal Prep Coach Agent** → Creates grocery lists and meal preparation schedules
5. **Progress Tracker Agent** → Logs weight, meals, exercise and shows trends with milestone predictions
6. **Motivator Agent** → Celebrates achievements and maintains accountability

### Stretch Goals

- **Exercise Pairing Agent** → Suggests physical activities to balance caloric intake

## Key Features

- **Personalized AI Agents**: Each agent specializes in a specific aspect of health management
- **Cultural Relevance**: Meal plans and recommendations adapted to cultural preferences
- **Visual Calorie Tracking**: Photo-based meal analysis for effortless logging
- **Predictive Analytics**: Trend analysis and milestone predictions
- **Collaborative Intelligence**: Agents work together to provide holistic guidance
- **Serverless Architecture**: Built on AWS with automatic scaling and cost optimization

## Target Users

- Individuals struggling with weight management who want personalized guidance
- People seeking culturally relevant meal planning and nutrition advice
- Users who prefer AI-powered assistance over manual tracking
- Health-conscious individuals looking for comprehensive, adaptive wellness support

## Technical Architecture

- **AWS Serverless**: Lambda, API Gateway, DynamoDB
- **AI/ML Platform**: Amazon Bedrock AgentCore (Runtime, Identity, Memory, Gateway, Observability)
- **Agent Framework**: AWS Strands SDK (open-source framework with model-first approach)
- **Infrastructure**: SAM (Serverless Application Model) for IaC
- **Deployment**: GitHub Actions for CI/CD
- **Runtime**: Node.js 22.x with ESM modules

## Development Strategy

Incremental development approach:

1. Build one agent at a time
2. Establish agent collaboration patterns
3. Integrate agents into a cohesive system
4. Scale and optimize based on usage patterns

## Development Status

- Initial setup phase
- Product vision and architecture defined
- Ready to begin agent-by-agent implementation
- Infrastructure patterns and best practices established
