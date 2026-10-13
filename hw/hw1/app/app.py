import os, random, requests
from flask import Flask, request, jsonify
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, func, create_engine
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    category = Column(String(200))
    description = Column(String(200))
    reviews = Column(ARRAY(String))
    users = relationship("User", back_populates="coffee")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    has_sale = Column(Boolean)
    address = Column(JSON)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))
    coffee = relationship("Coffee", back_populates="users")

app = Flask(__name__)
engine = create_engine(os.getenv("DATABASE_URL", "postgresql://skillbox_user:password@localhost:5432/skillbox_db"))
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

@app.before_request
def seed_data():
    if getattr(app, '_data_seeded', False): return
    with SessionLocal() as db:
        if db.query(Coffee).first():
            app._data_seeded = True
            return
        
        c_data = requests.get("https://dummyjson.com").json()["products"][0]
        coffee = Coffee(
            title=c_data["title"], category=c_data["category"], 
            description=c_data["description"][:200],
            reviews=[r["comment"] for r in c_data.get("reviews", [])]
        )
        db.add(coffee)
        db.commit()

        u_data = requests.get("https://dummyjson.com").json()["users"]
        for i in range(10):
            db.add(User(
                name=random.choice(["Jon", "Jane", "Alex", "Emma", "Liam", "Ava"]),
                has_sale=random.choice([True, False]),
                address=u_data[i]["address"], coffee_id=coffee.id
            ))
        db.commit()
    app._data_seeded = True

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json or {}
    with SessionLocal() as db:
        user = User(name=data.get('name'), has_sale=data.get('has_sale'), address=data.get('address'), coffee_id=data.get('coffee_id'))
        db.add(user)
        db.commit()
        return jsonify({"user_name": user.name, "coffee_title": user.coffee.title if user.coffee else None})

@app.route('/coffee/search')
def search_coffee():
    with SessionLocal() as db:
        q = func.plainto_tsquery('english', request.args.get('q', ''))
        res = db.query(Coffee).filter(func.to_tsvector('english', Coffee.title).op('@@')(q)).all()
        return jsonify([{"id": c.id, "title": c.title} for c in res])

@app.route('/coffee/unique-reviews')
def unique_reviews():
    with SessionLocal() as db:
        res = db.query(func.distinct(func.unnest(Coffee.reviews))).all()
        return jsonify({"unique_reviews": [r[0] for r in res if r and r[0]]})

@app.route('/users/by-country')
def users_by_country():
    with SessionLocal() as db:
        res = db.query(User).filter(User.address['country'].as_string() == request.args.get('country', '')).all()
        return jsonify([{"id": u.id, "name": u.name, "country": u.address.get('country')} for u in res])

if __name__ == '__main__':
    app.run(debug=True)

