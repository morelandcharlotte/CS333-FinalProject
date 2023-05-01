# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory into the container
COPY . /app

# Install any required packages
RUN pip install -r requirements.txt

# Set the command to run when the container starts
CMD ["python", "main.py"]
