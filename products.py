from flask import Flask , jsonify , abort


class Product(object):
    def __init__(self,mysql):
        self.counter = 0
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor()
        self.columns = ['id','name','code','price','qty','image','status'] 

    def get_one(self, id):
        self.cursor.execute("SELECT * from Product where id="+str(id))
        data = self.cursor.fetchone()
        if data is None:
            abort(404, "Product {} doesn't exist".format(id))
        else:
            data = dict(zip(self.columns,data))
            return jsonify(results=data)

    def get_all(self):
        self.cursor.execute("SELECT * from Product")
        data = self.cursor.fetchall()
        if data is None:
            api.abort(404, "Product {} doesn't exist".format(id))
        else:
            all_products = []
            for d in data:
                all_products.append(dict(zip(self.columns,d)))
            return jsonify(results=all_products)
       
    def create(self, data):
        sql = ("INSERT INTO  Product (name,description,code,price,status)"
                "values('{}','{}','{}','{}','{}')").format(data['name'],data['description'],data['product_code'],data['price'],data['status'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = {'status':'success', 'msg': "Product added successfully"}
        except Exception as e:
            result = {'status':'error', 'msg': "Problem inserting into db: {}".format(e)}
        return jsonify(result=result)

    def update(self, id, data):
        sql = ("UPDATE Product "
                "SET name={}, description={}, product_code={}, price={}, status={} "
                "WHERE id={}").format(data['name'],data['description'],data['product_code'],data['price'],data['status'],id)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = {'status':'success', 'msg':"Basket item {} updated successfully".format(id)}

        except Exception as e:
            result = {'status':'error', 'msg': "Problem updating db: {}".format(e)}
        return jsonify(result=result) 

    def delete(self, id):
        sql = ("DELETE from Product WHERE id={}").format(id)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = {'status':'success', 'msg':"Product {} deleted successfully".format(id)}
            
        except Exception as e:
            result = {'status':'error', 'msg': "Problem deleting from db: {}".format(e)}
        return jsonify(result=result) 

