from flask import Flask, Blueprint, request
import fib

app = Flask(__name__)

fib_bp = Blueprint("fibonacci", __name__, url_prefix="/fib")


@fib_bp.route('/recursive')
def fib_recursive():
    n = request.args.get("n", type=int, default=1)
    result = fib.recursive(n)
    return {"n": n, "result": result}

@fib_bp.route('/iterative')
def fib_iterative():
    n = request.args.get("n", type=int, default=1)
    result = fib.iterative(n)
    return {"n": n, "result": result}


app.register_blueprint(fib_bp)


if __name__ == '__main__':
    app.run(debug=True)
