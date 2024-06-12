import os
import requests
from flask import Flask, jsonify
import redis
import logging

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

app.logger.setLevel(logging.INFO)


@app.route('/complex_request', methods=['GET'])
def talk_to_service_b():
    app.logger.info("Sending request to Redis")
    foo_value = redis_client.get("foo")

    app.logger.info("Sending request to service B")
    response = requests.get('http://service-b:5001/data')

    app.logger.info("Reading environment variable 'HOST'")
    env_host = os.getenv("HOST", "ENV_HOST_NOT_FOUND")

    app.logger.info("Reading data from local file '/data/data.txt'")
    with open("/data/data.txt", "r") as datafile:
        datafile_contents = datafile.read()

    return jsonify({
        "redis_foo_response": foo_value,
        "service_b_response": response.json(),
        "env_var_HOST": env_host,
        "datafile_contents": datafile_contents
    })


if __name__ == '__main__':
    # Initialize redis with fake data, so it can
    # be returned when the api controller asks for it
    redis_client.set("foo", "bar")

    app.run(host='0.0.0.0', port=5000)
