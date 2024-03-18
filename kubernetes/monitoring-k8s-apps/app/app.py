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
    app.run(debug=True)



# TODO
# create the right fib algorithm functions
# (optional) print logs to stdout
# Setup z24x7 APM - https://www.site24x7.com/help/apm/python-agent/add-python-agent-in-kubernetes.html?src=cross-links&pg=help
