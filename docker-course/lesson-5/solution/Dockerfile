# Base Image
FROM python:3.12

# Set process working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Setup Code
COPY app.py ./app.py

# Setup runtime environment
ENV APP_ENV=dev

# Run the application
CMD [ "python3", "./app.py" ]
