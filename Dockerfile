# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /main

# Copy the contents of the current directory into the container
COPY . /main

# Install any required packages
RUN pip install -r requirements.txt
RUN python -it main.py
# Set the command to run when the container starts
CMD ["python", "main.py"]
