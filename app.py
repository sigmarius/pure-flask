from flask import Flask, request, render_template
from werkzeug.exceptions import BadRequest

from my_shop.views import products_app

app = Flask(__name__)

app.register_blueprint(products_app)


@app.route('/')
@app.route('/<name>')
def hello_name(name='World'):
    return render_template("index.html", name=name)
    # передаем параметр в шаблон
    # return f"Hello, {name}!"


# в <> подставляется значение => возвращается строка => конвертация в число <int:product_id/>
@app.route('/product/<product_id>')
def get_product(product_id):
    return f"product: {product_id!r} | {product_id}"


@app.route('/sum/')
def sum_values():
    try:
        # http://127.0.0.1:5000/sum/?a=1&b=2 => передача параметров
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
    except ValueError:
        raise BadRequest('a and b have to be integer!')
        # return 'Please write numbers only!'

    return {'a': a, 'b': b, 'sum': a + b}


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
