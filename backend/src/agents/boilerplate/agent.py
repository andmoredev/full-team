"""
Calculator Agent - BMI and calorie calculations
Built with Strands SDK and AgentCore Runtime following production best practices
"""
import os
import logging
from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig, RetrievalConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = BedrockAgentCoreApp()

# Environment variables
MEMORY_ID = os.getenv("BEDROCK_AGENTCORE_MEMORY_ID")
REGION = os.getenv("AWS_REGION", "us-east-1")
MODEL_ID = os.getenv("MODEL_ID", "us.anthropic.claude-3-7-sonnet-20250219-v1:0")

def create_agent(memory_config=None) -> Agent:
    """Create a specialized calculator agent with production configuration"""

    system_prompt = """You are a specialized health calculator agent. You help users calculate:

- BMI (Body Mass Index) based on height and weight
- Daily calorie needs based on age, gender, activity level, height, weight
- Target weight ranges for healthy BMI (18.5-24.9)
- Calorie deficits needed for weight loss goals (typically 500-1000 cal/day for 1-2 lbs/week)

Always provide accurate calculations and explain the methodology.
Ask for clarification if needed parameters are missing.
Use metric units (kg, cm) but accept imperial and convert as needed.

For BMI calculation: BMI = weight(kg) / (height(m))²
For calorie calculation, use Harris-Benedict equation with activity multipliers:
- Sedentary: BMR × 1.2
- Light activity: BMR × 1.375
- Moderate activity: BMR × 1.55
- Very active: BMR × 1.725
- Extremely active: BMR × 1.9"""

    # Production model configuration
    model_config = {
        "model_id": MODEL_ID,
        "temperature": 0.1,  # Low temperature for consistent calculations
        "max_tokens": 2000,
        "top_p": 0.9
    }

    # Conversation management for production
    conversation_manager = SlidingWindowConversationManager(
        window_size=10  # Limit history to prevent context overflow
    )

    agent_kwargs = {
        "system_prompt": system_prompt,
        "name": "CalculatorAgent",
        "model": model_config,
        "conversation_manager": conversation_manager,
        "tools": []  # Explicit empty list for production
    }

    # Add memory if configured
    if memory_config:
        agent_kwargs["session_manager"] = AgentCoreMemorySessionManager(memory_config, REGION)

    return Agent(**agent_kwargs)

@app.entrypoint
def invoke(payload, context):
    """Main entrypoint for the calculator agent"""
    try:
        logger.info("Calculator agent invoked", extra={"payload_keys": list(payload.keys()) if payload else []})

        # Extract request data
        prompt = payload.get("prompt", "") if payload else ""
        user_metrics = payload.get("userMetrics", {}) if payload else {}

        # Extract session and actor information from context
        session_id = getattr(context, 'session_id', 'default')
        actor_id = context.headers.get('X-Amzn-Bedrock-AgentCore-Runtime-Custom-Actor-Id', 'user') if hasattr(context, 'headers') else 'user'

        # Configure memory if available
        memory_config = None
        if MEMORY_ID:
            memory_config = AgentCoreMemoryConfig(
                memory_id=MEMORY_ID,
                session_id=session_id,
                actor_id=actor_id,
                retrieval_config={
                    f"/users/{actor_id}/health_metrics": RetrievalConfig(top_k=3, relevance_score=0.5),
                    f"/users/{actor_id}/preferences": RetrievalConfig(top_k=3, relevance_score=0.5)
                }
            )

        # Create agent instance
        agent = create_agent(memory_config)

        # Enhance prompt with user metrics if provided
        enhanced_prompt = prompt
        if user_metrics:
            metrics_str = ", ".join([f"{k}: {v}" for k, v in user_metrics.items()])
            enhanced_prompt = f"{prompt}\n\nUser metrics: {metrics_str}"

        # Process the request
        logger.info("Processing calculation request", extra={"session_id": session_id, "actor_id": actor_id})
        response = agent(enhanced_prompt)

        result = {
            "status": "success",
            "response": response.message.content[0].text,
            "session_id": session_id,
            "actor_id": actor_id,
            "timestamp": context.timestamp if hasattr(context, 'timestamp') else None
        }

        logger.info("Calculator agent completed successfully")
        return result

    except Exception as e:
        logger.error("Calculator agent error", extra={"error": str(e)}, exc_info=True)
        return {
            "status": "error",
            "error": str(e),
            "timestamp": getattr(context, 'timestamp', None) if context else None
        }

if __name__ == "__main__":
    app.run()