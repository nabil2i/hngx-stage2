# Use a Python 3.11 base image
FROM python:3.11-alpine AS builder

# Set environment variables
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Add a non-root user
RUN addgroup app && adduser -S -G app app

# Install build dependencies
RUN apk add --no-cache mariadb-connector-c-dev build-base

# Create a virtual environment and install dependencies
RUN python -m venv /venv
COPY Pipfile Pipfile.lock /app/
RUN /venv/bin/pip install pipenv && /venv/bin/pipenv install --deploy --ignore-pipfile

# ---- Final Image ----
FROM python:3.11-alpine

# Copy the virtual environment from the builder stage
COPY --from=builder /venv /venv

# Set environment variables
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Add a non-root user
RUN addgroup app && adduser -S -G app app

# Install runtime dependencies
RUN apk add --no-cache mariadb-connector-c-dev

# Copy your application code
COPY . /app/

# Change permissions
RUN chmod +x /app/docker-entrypoint.sh && chown -R app:app /app

# Switch to the non-root user
USER app

# Expose the port your application will run on
EXPOSE 8000

# Start your application
#CMD ["/app/docker-entrypoint.sh"]
