from flask import Flask, Blueprint, request
import resource_user as eater

app = Flask(__name__)

res_bp = Blueprint("resource_user", __name__, url_prefix="/resource_user")


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
# Setup z24x7 APM - https://www.site24x7.com/help/apm/python-agent/add-python-agent-in-kubernetes.html?src=cross-links&pg=help
# Specify cpu+memory resources allocated to each pod
