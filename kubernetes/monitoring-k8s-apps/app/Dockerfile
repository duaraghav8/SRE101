FROM python:3.12
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["python3", "app.py"]

# To run a container locally on port 8000, use:
# docker run --rm -p 8000:5000 <image_name>:<image_tag>