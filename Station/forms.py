from wtforms import Form, StringField, SubmitField, TextAreaField, SelectField, HiddenField, IntegerField
from wtforms import validators, FormField
from wtforms.validators import DataRequired
from wtforms_alchemy import ModelForm, ModelFieldList, QuerySelectField
from wtforms_alchemy.validators import Unique
from entity import Station, Train


class StationForm(ModelForm):
    class Meta:
        entity = Station
        include_primary_keys = True

    Number = IntegerField('Number', validators=[DataRequired()])
    Type = StringField('Type', validators=[DataRequired()])
    button_save = SubmitField("Сохранить")
    button_delete = SubmitField("Удалить")
