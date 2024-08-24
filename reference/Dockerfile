# Use the official Python 3.12 image as the base image
FROM python:3.12

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . ./src
ENV PATH "$PATH:/src/scripts"
RUN useradd -m -d /src -s /bin/bash app && chown -R app:app /src/* && chmod +x /src/scripts/*

# Set the working directory in the container
WORKDIR /src
USER app

# Start the FastAPI application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
