# Use official Python image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8080

# Start the app
CMD ["python", "run.py"]
