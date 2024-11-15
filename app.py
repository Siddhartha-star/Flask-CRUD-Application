from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash

app =Flask(__name__)
app.secret_key= "secretKey"

app.config['MONGO_URI'] ="mongodb://localhost:27017/college"
mongo=PyMongo(app)

@app.route('/add', methods=['POST'])
def add_user():
   _json = request.json
   _name = _json['name']
   _email=_json['email']
   _password=_json['password']
   if _name and _email and _password and request.method == 'POST':
      _hashed_password = generate_password_hash(_password)
      id =mongo.db.students.insert_one({'name':_name,'email':_email,'password':_hashed_password}).inserted_id

      response= jsonify("User added succesfully")
      response.status_code=200

      return response
   else:return not_found()
   
@app.route('/users')
def users():
      users =mongo.db.students.find()
      response= dumps(users)
      return response

@app.route('/user/<id>')
def user(id):
   user = mongo.db.students.find_one({'_id': ObjectId(id)})
   response = dumps(user)
   return response

@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
   mongo.db.students.delete_one({'_id': ObjectId(id)})
   response =jsonify("User Deleted Succesfully")
   response.status_code = 200
   return response

@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
   _id=id
   _json=request.json
   _name= _json['name']
   _email= _json['email']
   _password =_json['password']

   if _name and _email and _password and _id and request.method =='PUT':
      _hashed_password = generate_password_hash(_password)

      mongo.db.students.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(id)},{'$set':{'name':_name,'email':_email, 'password':_hashed_password}})
      response=jsonify("User Updated")
      response.status_code=200
      return response
   else:
      return not_found()
   
@app.errorhandler(404)
def not_found(error=None):
   message ={
      'status':404,
      'message': 'Not Found' + request.url
   }
   response = jsonify(message)

   response.status_code= 404
   return response

if __name__== "__main__":
   app.run(debug=True)

