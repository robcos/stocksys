from appengine_django import models
from google.appengine.ext import db

class Quote(models.BaseModel):
  date = db.TextProperty(required=True)
  value = db.TextProperty(required=True)

class Stock(models.BaseModel):
  name = db.TextProperty(required=True)
  quotes = db.ListProperty(db.Key)
  
  def by_name(name):
    stocks = Stock.all().filter('name = ', name).fetch(1)
    return stocks[0]

  by_name = staticmethod(by_name)

