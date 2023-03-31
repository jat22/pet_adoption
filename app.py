from flask import Flask, redirect, render_template
from models import db, connect_db, Pet
from forms import AddPetForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "SECRET"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_homepage():
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add', methods=['GET','POST'])
def add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data,
                        species=form.species.data,
                        photo_url=form.photo_url.data,
                        age=form.age.data,
                        notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        # raise
        return render_template('form.html', form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm()
    
    return render_template('show_pet.html', pet=pet, form=form)