import mistune
import os
#import glob
from flask import render_template,Flask,Markup
app = Flask(__name__, static_folder='static',static_url_path='')

def Renderer(fname):
    fname = os.getcwd()+"/"+fname
    print(fname)
    with open(fname) as f:
        content = f.read()

    content = Markup(mistune.markdown(content))
    return render_template('index.html', content=content)

@app.route('/')
def index():
     return Renderer("FRONT-PAGE.md")

@app.route('/<fname>')
def read(fname):
    return Renderer(fname+".md")
    #files = [f for f in glob.glob("*.md")]
    #content = ""
    #for fname in files:
    #    content = content + "<a href=/index/"+fname+" >"+fname+"</a><br>"
    #return render_template('index.html', content=Markup(content))

@app.route('/<pname>/<fname>')
def readdir(pname,fname):
    file_path = pname+"/"+fname+".md"
    if not os.path.exists(file_path):
        return "not found",404
    else:
        return Renderer(file_path)
