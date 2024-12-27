# Use the slim version of Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements to the container (adjust if needed)
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . /app/

# Expose the port for the application
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
