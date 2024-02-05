from flask import Flask,url_for
from markupsafe import escape
app = Flask(__name__)



@app.route("/<name>/<int:id>/<path:str>")
def hi(name,id,str):
    return f"Hello {escape(name)} {escape(id)} {str}"

@app.route("/fuckaround/")
def pussy():
    return "fucked"

@app.route("/suck")
def dick():
    return "sucked"

if __name__ == '__main__':
    app.run(debug=True)


with app.test_request_context():
    print("yesko")
    print(url_for("dick",next="/lick"))