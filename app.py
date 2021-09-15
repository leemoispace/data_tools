#表单用到的类
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from wtforms import StringField, PasswordField, BooleanField, IntegerField, \
    TextAreaField, SubmitField, MultipleFileField

import os
import uuid

app = Flask(__name__) #flask类的实例化


# Custom config 上传文件位置
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.datafile.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        session['filenames'] = [filename]
        return redirect(url_for('uploaded'))
    return render_template('upload.html', form=form)


@app.route('/uploaded')
def uploaded():
    return render_template('uploaded.html')

#下载处理后的文件
@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


# upload form
class UploadForm(FlaskForm):
    datafile = FileField('Upload excel data', validators=[FileRequired(), FileAllowed(['xls', 'xlsx'])])
    submit = SubmitField()

def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename
