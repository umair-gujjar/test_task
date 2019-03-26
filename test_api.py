from requests import get

class TestApi():

    def test_list_all_product_response(self):
        print 'Get All Products'
        all_products_url = 'http://localhost/Products/'
        assert get(all_products_url).text != ''

    def test_list_all_item_response(self):
        print 'Get All Basket Items'
        all_basket_item_url = 'http://localhost/Basket/'
        assert get(all_basket_item_url).text != ''
