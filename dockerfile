# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy your requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app files
COPY . .

# Expose the port your app listens on
EXPOSE 81

# Run your app
CMD ["python", "main.py"]
