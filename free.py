from flask import Flask,url_for,request,render_template
from markupsafe import escape
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/<name>/<int:id>/<path:str>')
def hi(name,id,str):
    return f'Hello {escape(name)} {escape(id)} {str}'

@app.route('/life/')
def how():
    return 'bright'

@app.route('/wife',methods = ['POST','GET','PUT'])
def help():
    if request.method == 'POST':
        return 'happy from POST'
    elif request.method == 'GET':
        return 'happy from GET'
    else:
        return 'whats wrong'
@app.get('/login')
def login():
    return render_template('login.html')
@app.post('/verify')
def handle_login():
    if valid_login(request.form['username'],request.form['password']):
        return render_template('upload.html')
    else:
        return render_template('login.html', error=f'Invalid username/password')
def valid_login(username,password):
    if username == 'test' and password == 'test':
        return True
    else:
        return False      
@app.route('/upload',methods = ['POST'])  
def upload():
    if 'doc' not in request.files:
        return 'No file present'
    file = request.files['doc']
    if file.filename == '':
        return 'No file selected'
    print(secure_filename(file.filename))
    file.save('jac.txt')
    return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)


with app.test_request_context():
    print(url_for('help',next='/xtra'))
    print(url_for('how'))