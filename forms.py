from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, URLField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, AnyOf, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
	"""From to add pet"""
    
	name = StringField('Name', 
		    			validators=[InputRequired(message = "Name is required")])
	species = SelectField('Species', 
		       			choices=["Select Species", "Cat", "Dog", "Porcupine"],
						validators=[InputRequired(message="Species is required."),
		  					AnyOf(["Cat", "Dog", "Porcupine"], message="Species is required.")])
	photo_url = URLField('Photo URL', validators=[URL(message="Please enter a valid URL."), Optional()])
	age = IntegerField("Pet's Age", 
		    			validators=[Optional(), 
		     				NumberRange(min=0, max=30, message="Must be between 0 and 30.")])
	notes = TextAreaField("Notes")
