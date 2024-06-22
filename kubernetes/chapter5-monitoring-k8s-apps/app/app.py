import random

from flask import Flask, Blueprint, request
import resource_user as eater

app = Flask(__name__)

res_bp = Blueprint("resource_user", __name__, url_prefix="/resource_user")


@app.route("/random_client_side_error")
def rcse():
    return {"status": "client_failure"}, random.randrange(400, 418)


@app.route("/random_server_side_error")
def rsse():
    return {"status": "server_failure"}, random.randrange(500, 508)


@app.route("/unhandled_exception")
def ue():
    raise Exception("Unhandled exception!")


@res_bp.route("/high_cpu_low_mem")
def hclm():
    n = request.args.get("n", type=int, default=1)
    result = eater.high_cpu_low_mem(n)
    return {"n": n, "result": result}


@res_bp.route("/high_cpu_high_mem")
def hchm():
    n = request.args.get("n", type=int, default=1)
    result = eater.high_cpu_high_mem(n)
    return {"n": n, "result": result}


@res_bp.route("/low_cpu_low_mem")
def lclm():
    n = request.args.get("n", type=int, default=1)
    result = eater.low_cpu_low_mem(n)
    return {"n": n, "result": result}


@res_bp.route("/med_cpu_high_mem")
def mchm():
    n = request.args.get("n", type=int, default=1)
    result = eater.med_cpu_high_mem(n)
    return {"n": n, "result": result}


app.register_blueprint(res_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# TODO
# create load-testing mechanism/script
# Create endpoints to return error codes (server side + client side), throw unhandled exceptions, intentionally have high latency
# Specify cpu+memory resources allocated to each pod
# Add README and describe exact process of how to run this app and see metrics in Site24x7
