FROM python:3.10-slim 

# Set working directory 
WORKDIR /workspace

# Copy the dependencies file 
COPY requirements.txt

Install dependencies 
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the code
COPY . . 
Expose port 5000 for Flask EXPOSE 5000 
Run the Flask application CMD ["python", "app.py"]
