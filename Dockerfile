# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /workspace

# Copy dependency file
COPY requirements.txt

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application code
COPY

# Expose Flask default port
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

# Run the Flask application
CMD ["python", "app.py"]
