from flask import Flask, render_template, request, url_for
import os

PEOPLE_FOLDER = os.path.join('static', 'image')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
@app.route('/index2')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'identity.jpg')
    return render_template("index2.html", user_image = full_filename)
	
if __name__ == "__main__":
#lance le serveur Flask
   app.run()