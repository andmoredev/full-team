from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent(model="us.amazon.nova-premier-v1:0")

@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    try:
        user_message = payload.get("prompt", "Hello")
        result = agent(user_message)

        # Extract text from the agent response
        # The response structure is: result.data.content (list of content blocks)
        response_text = ""
        if hasattr(result, 'data') and hasattr(result.data, 'content'):
            for content_block in result.data.content:
                if hasattr(content_block, 'text'):
                    response_text += content_block.text
        else:
            response_text = str(result)

        return {"status": "success", "result": response_text}
    except Exception as e:
        app.logger.error(f"Error processing request: {e}", exc_info=True)
        return {"status": "error", "error": str(e)}

if __name__ == "__main__":
    app.run()