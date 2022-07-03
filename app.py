import re
from flask import Flask, redirect, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import sys
from thirdweb import ThirdwebSDK
from dotenv import load_dotenv

load_dotenv()
rel_file_path = None


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[InputRequired()])
    contract_address = StringField()
    name = StringField()
    description = StringField()
    image_link = StringField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data #Grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename))) # Then save the file
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        name_of_nft = form.name.data 
        nft_description = form.description.data
        image_link = form.image_link.data
        rel_file_path = image_link
        print('-'*26)
        print(rel_file_path)
        print('-'*26)
        return redirect(url_for('landing'))
    return render_template('index.html', form=form)


@app.route('/landing', methods=['GET', 'POST'])
def landing():    
    return render_template('landing.html', result=str((2+2)), address=rel_file_path)

         



@app.route('/fail')
def fail():
    return 'Your submission has failed'

if __name__ == '__main__':
    app.run(debug=True)
