FROM public.ecr.aws/docker/library/python:3.11-slim
WORKDIR /app

# Copy dependency specification (expect requirements.txt tracked in repo)
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && \
	pip install aws-opentelemetry-distro>=0.10.1

# Create non-root user
RUN useradd -m -u 1000 bedrock_agentcore
USER bedrock_agentcore

# Ports (HTTP + optional secondary)
EXPOSE 8080
EXPOSE 8000

# Copy remaining application files
COPY . .

# Launch agent (expects a my_agent.py module providing entrypoint)
CMD ["opentelemetry-instrument", "python", "-m", "agent"]

