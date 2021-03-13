"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPet, EditPet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    """Home page"""
    pets = Pet.query.all()
    return render_template('index.html', pets = pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPet()

    if form.validate_on_submit():
        #after validating input, add to database then redirect back to same page
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, 
                photo_url=photo_url, age=age, 
                notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}!")
        
        return redirect("/")

    else:
        #render add pet page on get or submission failure
        return render_template("add_pet_form.html", form=form)


@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet_details(id):
    """Edit pet details."""

    pet = Pet.query.get_or_404(id)

    form = EditPet(obj=pet)    

    if form.validate_on_submit():
        #after validating input, add to database then redirect back to same page
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        
        return redirect(f"/{id}")

    else:
        #render edit pet page on get or submission failure
        return render_template("edit_pet_detail.html", pet=pet, form=form)