FROM python:3.12

WORKDIR /app

# The directory where all application data will reside
# Our Volume will be mounted at this directory inside the container.
# This means all data being written inside this directory will actually be
# written to the external volume, so it is preserved even after the container
# exits.
RUN mkdir /data

COPY app.py .

# Force python to print the logs on stdout as soon as they're available
ENV PYTHONUNBUFFERED=1

CMD [ "python3", "./app.py" ]
