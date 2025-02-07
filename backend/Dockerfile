# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv (modern Python package manager)
RUN pip install uv

# Create a virtual environment using uv
RUN uv venv .venv

# Sync dependencies into the virtual environment
# COPY pyproject.toml .
# RUN uv pip sync

COPY requirements.txt .
RUN uv pip sync requirements.txt

# Copy the application code (not needed if using volumes, but kept for completeness)
# COPY ./app /app/app

# Expose the port
EXPOSE 8000

# Run the app within the virtual environment
CMD [".venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
