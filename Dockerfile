
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /workspace

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the app
CMD ["python", "app.py"]
