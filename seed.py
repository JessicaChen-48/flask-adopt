from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name="Fluffy", species="cat", age="baby", available=True)
pet2 = Pet(name="Mittens", species="cat", photo_url="https://tinyurl.com/3bym3xau", age="senior", available=True)
pet3 = Pet(name="Spike", species="hedgehog", age="adult", notes="may be lost hedgehog", available=False)


db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)

db.session.commit()