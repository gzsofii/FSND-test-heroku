import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

#database_path = os.environ['DATABASE_URL']
#database_name ='local_db_name'
default_database_path="postgresql:///agency"
#default_database_path= "postgresql://{}:{}@{}/{}".format('postgres', 'password', 'localhost:5432', database_name)
#database_path = os.getenv('DATABASE_URL', default_database_path)
database_path = os.environ.get('DATABASE_URL')

if database_path:
    database_path = database_path.replace("://", "ql://", 1)
    print(".................................", database_path)
else:
    database_path=default_database_path
    print('database path: ', database_path)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Person
Have title and release year
'''
class Person(db.Model):  
  __tablename__ = 'People'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  catchphrase = Column(String)

  def __init__(self, name, catchphrase=""):
    self.name = name
    self.catchphrase = catchphrase

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'catchphrase': self.catchphrase}