from flask import Flask,url_for,request,render_template
from markupsafe import escape
app = Flask(__name__)

@app.route("/<name>/<int:id>/<path:str>")
def hi(name,id,str):
    return f"Hello {escape(name)} {escape(id)} {str}"

@app.route("/life/")
def how():
    return "bright"

@app.route("/wife",methods = ['POST','GET','PUT'])
def help():
    if request.method == 'POST':
        return "happy from POST"
    elif request.method == 'GET':
        return "happy from GET"
    else:
        return "whats wrong"
@app.get("/login")
def login():
    return render_template('login.html')
        

if __name__ == '__main__':
    app.run(debug=True)


with app.test_request_context():
    print(url_for("help",next="/xtra"))
    print(url_for("how"))