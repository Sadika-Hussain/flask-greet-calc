from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    """Handle a request to perform addition"""
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    result = operations.add(a,b)

    return str(result)

@app.route('/sub')
def sub():
    """Handle a request to perform subtraction"""
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    result = operations.sub(a,b)

    return str(result)

@app.route('/mult')
def mult():
    """Handle a request to perform multiplication"""
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    result = operations.mult(a,b)

    return str(result)

@app.route('/div')
def div():
    """Handle a request to perform division"""
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    result = operations.div(a,b)

    return str(result)



@app.route('/math/<operation>')
def do_math(operation):
    """
    Handle a request to perform a mathematical operation based on the URL path

    URL path should specify the operation as one of:
    - "add"
    - "sub"
    - "mult"
    - "div"
    """
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))

    operations_dict = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div
    }

    result = operations_dict[operation](a,b)

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)




