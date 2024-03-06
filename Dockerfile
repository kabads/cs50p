# Set base image
FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src dir to the working directory
COPY src/ .
