# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set environment variables from .env file (if needed)
# Use the environment variable in your app configuration
# ENV <VAR_NAME> <VALUE>

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Run run.py when the container launches
CMD ["python", "run.py"]