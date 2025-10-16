# Base image (multi-arch official Python). We'll install uv manually to avoid exec format issues in CodeBuild x86 builders.
FROM python:3.11-slim

WORKDIR /app

ENV UV_VERSION=0.1.45
RUN pip install --no-cache-dir "uv==${UV_VERSION}"

# Copy project dependency files
COPY pyproject.toml uv.lock ./

# Use uv to resolve & install (fallback to pip if uv.lock not compatible)
RUN uv sync --frozen --no-cache || pip install -r <(uv export --format requirements || echo '')

# Copy agent file
COPY agent.py ./

# Expose port
EXPOSE 8080

# Run application
CMD ["uv", "run", "uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]