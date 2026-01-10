from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import random
from string import ascii_uppercase
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'riverplate')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///chat-app.db')
app.config['TIMEZONE'] = pytz.utc
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

rooms = {}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    messages = db.relationship('Message', backref='user', lazy=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(4), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
            
        if code not in rooms:
            break
        
    return code

@app.route('/', methods=['POST', 'GET'])
def home():
    session.clear()
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)
        
        if not name:
            return render_template('home.html', error='Please enter a valid name.', code=code, name=name)
        
        if join != False and not code:
            return render_template('home.html', error='Please enter a valid room code.', code=code, name=name)
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {'members': 0, "messages": []}
        elif code not in rooms:
            return render_template('home.html', error='Room doesn\'t exist!', code=code, name=name)
        
        session['room'] = room
        session['name'] = name
        
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        session['user_id'] = user.id
        
        return redirect(url_for('room'))
    
    return render_template('home.html')

@app.route('/room')
def room():
    room = session.get('room')
    if room is None or session.get('name') is None or room not in rooms:
        return redirect(url_for('home'))
    
    return render_template('room.html', code=room, messages=rooms[room]["messages"])

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('home'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    messages = user.messages
    return render_template('history.html', messages=messages, app=app)

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return
    
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    
    user_id = session.get('user_id')
    message = Message(room=room, user_id=user_id, content=data["data"])
    db.session.add(message)
    db.session.commit()
    
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

@socketio.on('connect')
def connect(auth):
    room = session.get('room')
    name = session.get('name')
    if not room or not name:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    join_room(room)
    send({'name': name, 'message': 'has entered the room'}, to=room)
    rooms[room]['members'] += 1
    print(f'{name} joined room {room}')

@socketio.on('disconnect')
def disconnect():
    room = session.get('room')
    name = session.get('name')
    leave_room(room)
    
    if room in rooms:
        rooms[room]['members'] -= 1
        if rooms[room]['members'] <= 0:
            del rooms[room]
            
    send({'name': name, 'message': 'has left the room'}, to=room)
    print(f'{name} has left room {room}')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)