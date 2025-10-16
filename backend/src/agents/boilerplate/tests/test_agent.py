"""
Tests for Calculator Agent
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the agent directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from agent import create_calculator_agent, invoke


class TestCalculatorAgent:
    """Test cases for the Calculator Agent"""

    def test_create_calculator_agent_without_memory(self):
        """Test agent creation without memory configuration"""
        agent = create_calculator_agent()

        assert agent is not None
        assert agent.name == "CalculatorAgent"

    @patch('agent.AgentCoreMemorySessionManager')
    def test_create_calculator_agent_with_memory(self, mock_session_manager):
        """Test agent creation with memory configuration"""
        from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig

        memory_config = AgentCoreMemoryConfig(
            memory_id="test-memory-id",
            session_id="test-session",
            actor_id="test-user"
        )

        agent = create_calculator_agent(memory_config)

        assert agent is not None
        assert agent.name == "CalculatorAgent"
        mock_session_manager.assert_called_once()

    @patch('agent.create_calculator_agent')
    def test_invoke_success(self, mock_create_agent):
        """Test successful agent invocation"""
        # Mock agent response
        mock_agent = Mock()
        mock_response = Mock()
        mock_response.message.content = [Mock(text="Your BMI is 22.9, which is healthy.")]
        mock_agent.return_value = mock_response
        mock_create_agent.return_value = mock_agent

        # Mock context
        mock_context = Mock()
        mock_context.session_id = "test-session"
        mock_context.headers = {"X-Amzn-Bedrock-AgentCore-Runtime-Custom-Actor-Id": "test-user"}

        payload = {
            "prompt": "Calculate my BMI",
            "userMetrics": {"height": 175, "weight": 70}
        }

        result = invoke(payload, mock_context)

        assert result["status"] == "success"
        assert "BMI" in result["response"]
        assert result["session_id"] == "test-session"
        assert result["actor_id"] == "test-user"

    @patch('agent.create_calculator_agent')
    def test_invoke_with_minimal_payload(self, mock_create_agent):
        """Test invocation with minimal payload"""
        mock_agent = Mock()
        mock_response = Mock()
        mock_response.message.content = [Mock(text="Please provide your height and weight.")]
        mock_agent.return_value = mock_response
        mock_create_agent.return_value = mock_agent

        mock_context = Mock()
        mock_context.session_id = "default"
        mock_context.headers = {}

        payload = {"prompt": "Calculate BMI"}

        result = invoke(payload, mock_context)

        assert result["status"] == "success"
        assert result["actor_id"] == "user"  # Default value

    @patch('agent.create_calculator_agent')
    def test_invoke_agent_error(self, mock_create_agent):
        """Test handling of agent errors"""
        mock_agent = Mock()
        mock_agent.side_effect = Exception("Agent processing failed")
        mock_create_agent.return_value = mock_agent

        mock_context = Mock()
        mock_context.session_id = "test-session"
        mock_context.headers = {}

        payload = {"prompt": "Calculate BMI"}

        result = invoke(payload, mock_context)

        assert result["status"] == "error"
        assert "Agent processing failed" in result["error"]

    def test_invoke_empty_payload(self):
        """Test invocation with empty payload"""
        mock_context = Mock()
        mock_context.session_id = "default"
        mock_context.headers = {}

        with patch('agent.create_calculator_agent') as mock_create_agent:
            mock_agent = Mock()
            mock_response = Mock()
            mock_response.message.content = [Mock(text="Hello! How can I help you?")]
            mock_agent.return_value = mock_response
            mock_create_agent.return_value = mock_agent

            result = invoke(None, mock_context)

            assert result["status"] == "success"

    @patch.dict(os.environ, {"BEDROCK_AGENTCORE_MEMORY_ID": "test-memory-123"})
    @patch('agent.AgentCoreMemoryConfig')
    @patch('agent.create_calculator_agent')
    def test_invoke_with_memory_configuration(self, mock_create_agent, mock_memory_config):
        """Test invocation with memory configuration from environment"""
        mock_agent = Mock()
        mock_response = Mock()
        mock_response.message.content = [Mock(text="I remember your previous calculations.")]
        mock_agent.return_value = mock_response
        mock_create_agent.return_value = mock_agent

        mock_context = Mock()
        mock_context.session_id = "test-session"
        mock_context.headers = {"X-Amzn-Bedrock-AgentCore-Runtime-Custom-Actor-Id": "test-user"}

        payload = {"prompt": "What was my last BMI?"}

        result = invoke(payload, mock_context)

        assert result["status"] == "success"
        mock_memory_config.assert_called_once()
        mock_create_agent.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__])