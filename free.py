from flask import Flask,url_for,request,render_template,make_response, redirect, session, flash
from markupsafe import escape
from werkzeug.utils import secure_filename
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex()

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
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404
@app.route('/')
def enter():
    return redirect(url_for('login'))
@app.get('/login/')
def login():
    return render_template('login.html')
@app.post('/verify')
def handle_login():
    if valid_login(request.form['username'],request.form['password']):
        response = make_response(render_template('upload.html'))
        response.set_cookie('username', request.form['username'])
        response.headers['X-something'] = 'login may be'
        return response
    else:
        return render_template('login.html', error=f'Invalid username/password')
def valid_login(username,password):
    if username == 'test' and password == 'test':
        session['username'] = username
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
    file.save(f"temp_files/{secure_filename(file.filename)}")
    flash('file uploaded successfully')
    return render_template('success.html')
@app.route('/logout')
def handle_logout():
    session.pop('username',None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)


with app.test_request_context():
    print(url_for('help',next='/xtra'))
    print(url_for('how'))