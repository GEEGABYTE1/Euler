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
contract_addresses = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[InputRequired()])
    contract_address = StringField()
    submit = SubmitField('Upload File')


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data #Grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename))) # Then save the file
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        rel_file_path = file_path
        print('-'*26)
        print(rel_file_path)
        print('-'*26)
        text = form.contract_address.data
        contract_addresses.append(text)
        return redirect(url_for('landing'))
    return render_template('index.html', form=form)

class UploadFileForm2(FlaskForm):
    name = StringField()
    description = StringField()
    submit = SubmitField('DeployNFT')

@app.route('/landing', methods=['GET', 'POST'])
def landing():
    
    

    
    return render_template('landing.html', result=str((2+2)), address=contract_addresses[0])

         



@app.route('/fail')
def fail():
    return 'Your submission has failed'

if __name__ == '__main__':
    app.run(debug=True)
