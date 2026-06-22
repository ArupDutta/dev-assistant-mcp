FROM python:3.11-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure logs appear immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Copy dependency files first for better layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies into the system Python
RUN uv sync --system --frozen --no-dev

# Copy application code
COPY . .

# Expose MCP port if using HTTP transport
EXPOSE 8000

# Start the MCP server
CMD ["python", "main.py"]