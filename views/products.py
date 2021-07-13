from flask import Blueprint, request, render_template, url_for, redirect
from werkzeug.exceptions import NotFound, BadRequest

products_app = Blueprint("products_app", __name__, url_prefix='/products')

PRODUCTS = {
    1: 'Smartphone',
    2: 'Tablet',
    3: 'Laptop'
}

# делаем автоматическое добавление индексов в БД
indexes = iter(range(len(PRODUCTS) + 1, 100))


@products_app.route('/', endpoint='list')
# или без указания url_prefix => @products_app.route('/products/list')
def products_list():
    return render_template('products/products_list.html',
                           products=PRODUCTS)


@products_app.route('/add', methods=['GET', 'POST'], endpoint='add')
def product_add():
    if request.method == 'GET':
        return render_template("products/add_product.html")

    # проверяем что название продукта пришло из формы
    product_name = request.form.get('product-name')
    if not product_name:
        raise BadRequest('Product name is required')

    # записываем в БД, если все ОК, автоматически увеличивая индекс
    index = next(indexes)
    PRODUCTS[index] = product_name
    # переводим на страницу продукта, используя эндпойнт блюпринта
    product_url = url_for('products_app.details', product_id=index)
    return redirect(product_url)


@products_app.route('/<int:product_id>', endpoint='details')
def product_details(product_id):
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"Product #{product_id} not found!")

    return render_template('products/product_details.html',
                    product_id=product_id,
                    product_name=product_name)

