#created the game to be responsive and added some other creative html/css features
#enjoy! :-)

from flask import Flask, flash, session, request
from flask import url_for, redirect, render_template
import os
import pickle
import map

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login_get():
    if 'user' in session:
        return redirect(url_for['index'])
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    users = []
    username = request.form.get('username')
    password = request.form.get('password')
    with open('users.txt', 'r') as usrfile:
        if os.stat("users.txt").st_size != 0:
            users = pickle.loads(usrfile.read())
        else:
            users = {}
    try:
        users[username]
    except KeyError:
        return render_template('login.html', message="This user is not existing yet.")
    else:
        if users[username] == password:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message="Wrong password. Try again.")

@app.route('/register', methods=['GET'])
def register_get():
    if 'user' in session:
        return redirect(url_for['index'])
    else:
        return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')

    data = {username:password}
    with open('users.txt', 'r+') as usrfile:
        if os.stat("users.txt").st_size != 0:
            users = pickle.loads(usrfile.read())
            usrfile.seek(0)
            usrfile.truncate()
        else:
            users = {}
        users.update(data)
        pickle.dump(users,usrfile)
    return render_template('register.html', message="Welcome to the Game of Love. You can log in now.")

@app.route('/save', methods=['GET'])
def save():
    thescene = map.SCENES[session['scene']]
    data = {session['user']:thescene}
    saves = {}

    with open('savegames.txt', 'a+') as svfile:
        try:
            saves = pickle.loads(svfile.read())
        except:
            pass
        saves[session['user']] = thescene
        svfile.seek(0)
        svfile.truncate()
        pickle.dump(saves,svfile)
        flash("Game saved.")

    return redirect(url_for('game_get'))

@app.route('/load', methods=['GET'])
def load():
    thescene = map.SCENES[session['scene']]

    with open('savegames.txt', 'r') as svfile:
        try:
            saves = pickle.loads(svfile.read())
            thescene = saves[session['user']]
            session['scene'] = thescene.urlname
            flash("Saved game loaded.")
        except:
            flash("No saved game to load.")
        return redirect(url_for('game_get'))


@app.route('/logout', methods=['GET'])
def logout():
    session.pop("user")
    return redirect(url_for('index'))

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        return redirect(url_for('login_get'))
        #this is when a user enters the game in the middle of action
        #this could happen because of a url string in the middle of a scene
        #he did not enter the game at the beginning, so he has to be redirected
        #preferably to login

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput').lower()

    if 'scene' in session:
        currentscene = map.SCENES[session['scene']]
        nextscene = currentscene.go(userinput)

        if userinput == '':
            return render_template('show_scene.html', scene=currentscene, message="Write anything, please.")
        else:
            if nextscene is None:
                return render_template('show_scene.html', scene=currentscene, message="Write anything, please.")
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        index()

@app.route('/')
def index():
    if 'user' in session:
        session['scene'] = map.START.urlname
        print session['scene']
        return redirect(url_for('game_get'))
    else:
        return redirect(url_for('login_get'))

app.secret_key = 'xxkakdndnck/nsfcadk/pnzrln'

if __name__ == "__main__":
    app.run(port=5001)
