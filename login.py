from flask import Flask, session, redirect, url_for, escape, request,g

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
         return 'Logged in as %s' % escape(session['username'])
        #return 'Logged in as ' +  g.user
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        g.user=request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8089)

# set the secret key.  keep this really secret:
