from flask import Flask , jsonify
from flask_restplus import Api, Resource, fields
from flaskext.mysql import MySQL
from products import Product
from basket import Basket
import config

mysql = MySQL()

app = Flask(__name__)
api = Api(app, version='0.1.0', title='Shopping Basket API',
    description='A simple RestfulAPI for shopping basket',
)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = config.dbuser
app.config['MYSQL_DATABASE_PASSWORD'] = config.dbpass
app.config['MYSQL_DATABASE_DB'] = config.dbname
app.config['MYSQL_DATABASE_HOST'] = config.dbhost
app.config['MYSQL_DATABASE_PORT'] = config.dbport
mysql.init_app(app)

pns = api.namespace('Products', description='All availble products data')
bns = api.namespace('Basket', description='All availble products in the basket')

product_parser = api.parser()
product_parser.add_argument('name', type=str, required=True, help='Product Name', location='form')
product_parser.add_argument('description', type=str, required=True, help='Product Description', location='form')
product_parser.add_argument('price', type=int, required=True, help='Product Price', location='form')
product_parser.add_argument('product_code', type=str, required=True, help='Product Code', location='form')
product_parser.add_argument('status', type=str, required=True, help='Product Status', location='form')

basket_parser = api.parser()
basket_parser.add_argument('user_id', type=str, required=True, help='User id', location='form')
basket_parser.add_argument('session_id', type=str, required=True, help='Session id', location='form')
basket_parser.add_argument('product_code', type=str, required=True, help='Item Code', location='form')
basket_parser.add_argument('qty', type=int, required=True, help='Product Qty', location='form')
product_parser.add_argument('status', type=str, required=True, help='Item Status', location='form')


product = Product(mysql)
basket = Basket(mysql)

@pns.route('/')
class ProductList(Resource):
    '''Shows a list of all Products, and lets you to add new Products'''
    @pns.doc('list_all_product')
    def get(self):
        '''List all Products'''
        return product.get_all()

    @api.doc(parser=product_parser)
    def post(self):
        '''Add New Product'''
        args = product_parser.parse_args()
        return product.create(args)

@pns.route('/<int:id>')
class Products(Resource):
    @pns.doc('get_product_by_id')
    def get(self,id):
        '''List Product by id'''
        return product.get_one(id)

    @api.doc(parser=product_parser)
    def put(self):
        '''Update Product'''
        args = product_parser.parse_args()
        return product.update(args)

    @pns.doc('delete_product_by_id')
    def delete(self,id):
        '''delete Product by id'''
        return product.delete(id)

@bns.route('/')
class BasketList(Resource):
    '''Shows a list of all Items in basket, and lets you to add new Items'''
    @bns.doc('list_all_items')
    def get(self):
        '''List all Items'''
        return basket.get_all()

    @api.doc(parser=basket_parser)
    def post(self):
        '''Add New Item'''
        args = basket_parser.parse_args()
        return basket.create(args)

@bns.route('/<int:id>')
class Basket(Resource):
    @bns.doc('get_item_by_id')
    def get(self,id):
        '''List Item by id'''
        return basket.get_by_id(id)

    @api.doc(parser=basket_parser)
    def put(self):
        '''Update Product'''
        args = basket_parser.parse_args()
        return basket.update(args)

    @bns.doc('delete_item_by_id')
    def delete(self,id):
        '''delete Item by id'''
        return basket.delete(id)

@bns.route('/userid/<int:uid>')
class Basket(Resource):
    @bns.doc('list_all_item_by_userid')
    def get(self,uid):
        '''List all Items by User'''
        return basket.get_by_userid(uid)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5012,debug=True)

