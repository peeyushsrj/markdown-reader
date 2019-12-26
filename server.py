import mistune
import glob
from flask import render_template,Flask,Markup
app = Flask(__name__, static_folder='static',static_url_path='')

@app.route('/')
def index2():
    files = [f for f in glob.glob("*.md")]
    content = ""
    for fname in files:
        content = content + "<a href=/index/"+fname+" >"+fname+"</a><br>"
    return render_template('index.html', content=Markup(content))

@app.route('/index/<fname>')
def index(fname):
    print(fname)
    with open(fname) as f:
        content = f.read()

    content = Markup(mistune.markdown(content))
    return render_template('index.html', content=content)

