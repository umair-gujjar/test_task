from flask import Flask , jsonify , abort

class Basket(object):
    def __init__(self,mysql):
        self.counter = 0
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor()
        self.columns = ['id','userid','sessionid','productcode','qty','status','product_name','price'] 

    def get_by_id(self, id):
        sql = ("SELECT Basket.*,Product.name,Product.price from Basket "
            "INNER JOIN Product ON Basket.productcode=Product.code "
            "where Basket.id={}").format(id)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        if data is None:
            api.abort(404, "Basket item {} doesn't exist".format(id))
        else:
            data = dict(zip(self.columns,data))
            return jsonify(results=data)

    def get_by_userid(self, uid):
        sql = ("SELECT * from Basket "
            "INNER JOIN Product ON Basket.productcode=Product.code "
            "where userid={}").format(uid)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        if data is None:
            api.abort(404, "Basket item {} doesn't exist".format(id))
        else:
            data = dict(zip(self.columns,data))
            return jsonify(results=data)

    def get_all(self):
        sql = ("SELECT Basket.*,Product.name,Product.price from Basket "
            "INNER JOIN Product ON Basket.productcode=Product.code")
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if data is None:
            api.abort(404, "Basket item {} doesn't exist".format(id))
        else:
            all_items = []
            for d in data:
                all_items.append(dict(zip(self.columns,d)))
            return jsonify(results=all_items)
       
    def create(self, data):
        sql = ("INSERT INTO  Basket (userid,sessionid,productcode,qty,status)"
                "values('{}','{}','{}','{}','{}')").format(data['user_id'],data['session_id'],data['product_code'],data['qty'],data['status'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = {'status':'success', 'msg': "Basket item added successfully"}
        except Exception as e:
            result = {'status':'error', 'msg': "Problem inserting into db: {}".format(e)}
        return jsonify(result=result)

    def update(self, id, data):
        sql = ("UPDATE Basket "
                "SET userid={}, sessionid={}, productcode={}, qty={}, status={} "
                "WHERE id={}").format(data['user_id'],data['session_id'],data['product_code'],data['qty'],data['status'],id)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = {'status':'success', 'msg':"Basket item {} updated successfully".format(id)}

        except Exception as e:

            result = {'status':'error', 'msg': "Problem updating db: {}".format(e)}
        return jsonify(result=result) 


    def delete(self, id):
        sql = ("DELETE from Basket WHERE id={}").format(id)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = {'status':'success', 'msg':"Basket item {} deleted successfully".format(id)}

        except Exception as e:

            result = {'status':'error', 'msg': "Problem deleting from db: {}".format(e)}
        return jsonify(result=result) 
