# Use official Python 3.11 lightweight image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
# All commands after this will run inside /app
WORKDIR /app

# Copy all files from current project folder (host machine)
# into the /app directory inside the container
COPY . .

# Install required Python libraries for the application
# flask -> web framework
# mysql-connector-python -> connect Flask app with MySQL database
RUN pip install flask mysql-connector-python

# Expose port 5001 so the container can accept traffic on this port
# This is the port where the Flask app will run
EXPOSE 5001

# Command to start the Flask application when container starts
# It runs the Python file named aap.py
CMD ["python", "app.py"]
