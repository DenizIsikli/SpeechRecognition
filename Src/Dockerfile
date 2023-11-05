# Use the official Python image as the base image
FROM python:3.9

# Set the working directory within the container
WORKDIR /app

# Copy the contents of your project into the container
COPY . /app

# Install any Python dependencies using pip
RUN pip install --no-cache-dir -r /app/Dependencies/requirements.txt

# Expose the port if your application runs a web server (e.g., Flask)
# EXPOSE 5000

# Define the command to run your application
CMD ["python", "/app/Tkinter/Tkinter.py"]
