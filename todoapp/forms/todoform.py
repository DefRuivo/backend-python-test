from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import InputRequired


class TodoForm(FlaskForm):
    description = TextAreaField(label="Description", 
                                validators=[InputRequired(message="Description Invalid")], 
                                render_kw={"placeholder" : "Enter a task here", "class":"task-input", "row":"1"})