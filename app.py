from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:oudom123???@localhost:3306/ap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import terms
db.init_app(app)

@app.get('/terms')
def get_terms():
  t = db.session.query(terms).with_entities(terms.terms_id, terms.terms_description, terms.terms_due_days)
  
  ls = []
  for u in t:
    te = {
      "id": u.terms_id,
      "description": u.terms_description,
      "due_days": u.terms_due_days
    }
    ls.append(te)
  return ls

@app.get('/terms1')
def get_terms1():
  t = db.session.query(terms).with_entities(terms.terms_id, terms.terms_description, terms.terms_due_days)
  lst = [v._asdict() for v in t]
  return lst


if __name__=='__main__':
  app.run(host='127.0.0.1', port=5000)