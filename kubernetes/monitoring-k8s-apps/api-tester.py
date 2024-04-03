import requests
import random
import time

error_api_endpoints = [
    "/random_client_side_error",
    "/random_server_side_error",
    "/unhandled_exception",
]
resource_api_endpoints = [
    ("/resource_user/high_cpu_low_mem", 25),
    ("/resource_user/high_cpu_high_mem", 25),
    ("/resource_user/low_cpu_low_mem", 10000000),
    ("/resource_user/med_cpu_high_mem", 35000),
]

port = 50264
base_url = f"http://127.0.0.1:{port}"


def make_request(endpoint):
    url = base_url + endpoint
    response = requests.get(url)
    print(f"Request to {url} - Status code: {response.status_code}")


def make_resource_request(endpoint, n):
    make_request(endpoint + f"?n={n}")


def make_requests():
    while True:
        endpoint = random.choice(error_api_endpoints)
        make_request(endpoint)
        time.sleep(random.uniform(0, 1.5))  # Random pause between 0 and 2 seconds

        resource_endpoint, max_n = random.choice(resource_api_endpoints)
        n = random.randint(1, max_n)
        make_resource_request(resource_endpoint, n)
        time.sleep(random.uniform(0, 5))


if __name__ == "__main__":
    make_requests()
