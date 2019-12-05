from flask import Flask, render_template
#déclare le serveur flask
app = Flask(__name__)
#crée la route web de la racine du site

@app.route('/<page_name>/')
def render_static(page_name):
    return render_template(f'{page_name}.html')

if __name__ == "__main__":
#lance le serveur Flask
   app.run(debug = True)