from json2html import *
from flask import Flask, render_template,json
from jinja2 import Environment,FileSystemLoader

app = Flask(__name__)

@app.route('/')
def my_form_post():
        with open("data.json") as f:
            infoFromJson = json.load(f)
            # x=json2html.convert(json=infoFromJson)
            fileloader=FileSystemLoader("templates")
            env=Environment(loader=fileloader)
            rendered=env.get_template("index.html").render(infoFromJson)
            y="templates/index.html"
            with open(y,"w") as g:
                g.write(str(rendered))
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)