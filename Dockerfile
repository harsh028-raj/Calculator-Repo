# Use an official python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the Python script into container
COPY calc.py .

RUN pip install flask

# Run the Python script when the container starts
CMD ["python", "calc.py"]
