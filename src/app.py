import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from main import *
 
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = "secret key"
 
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        rate = request.form['rate']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = 'image.png' #secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Image successfully uploaded and displayed below')
            return render_template('index.html', filename=filename, rate=rate)
        else:
            flash('Allowed image types are - png, jpg, jpeg')
            return redirect(request.url)

@app.route('/uploads/<name>')
def download_image(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)

@app.route('/uploads/compress.png')
def download_image_compress():
    return send_from_directory(app.config["UPLOAD_FOLDER"], 'compress.png', as_attachment=True)
 
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/display/<rate>/compress.png')
def display_image_c(rate):
    aRed, aGreen, aBlue, originalImage = openImage('static/uploads/image.png')

    singularValuesLimit = int(rate)

    aRedCompressed = compressSingleChannel(aRed, singularValuesLimit)
    aGreenCompressed = compressSingleChannel(aGreen, singularValuesLimit)
    aBlueCompressed = compressSingleChannel(aBlue, singularValuesLimit)

    imr = Image.fromarray(aRedCompressed, mode=None)
    img = Image.fromarray(aGreenCompressed, mode=None)
    imb = Image.fromarray(aBlueCompressed, mode=None)

    newImage = Image.merge("RGB", (imr, img, imb))

    newImage.save(os.path.join(app.config['UPLOAD_FOLDER'], 'compress.png'))

    return redirect(url_for('static', filename='uploads/' + 'compress.png'), code=301)

if __name__ == "__main__":
    app.run(debug=True)
