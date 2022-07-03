from flask import Flask, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import sys

rel_file_path = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[InputRequired()])
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
        return redirect(url_for('landing'))
    return render_template('index.html', form=form)

@app.route('/landing')
def landing():
    return render_template('landing.html')

@app.route('/fail')
def fail():
    return 'Your submission has failed'

if __name__ == '__main__':
    app.run(debug=True)
