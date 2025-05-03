from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # 实际应用中需要更安全的密钥
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')
    emit('user_connected', {'sid': request.sid}, broadcast=True)
    users[request.sid] = {'nickname': f'User {len(users) + 1}'} # 简单分配昵称
    emit('user_list', list(users.values()))
    emit('message', {'nickname': 'System', 'text': f'{users[request.sid]["nickname"]} joined the chat.'}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconnected: {request.sid}')
    nickname = users.pop(request.sid, {}).get('nickname', 'Unknown')
    emit('user_disconnected', {'sid': request.sid}, broadcast=True)
    emit('user_list', list(users.values()))
    emit('message', {'nickname': 'System', 'text': f'{nickname} left the chat.'}, broadcast=True)

@socketio.on('new_message')
def handle_new_message(data):
    message = data.get('text')
    nickname = users.get(request.sid, {}).get('nickname', 'Anonymous')
    emit('message', {'nickname': nickname, 'text': message}, broadcast=True)

@socketio.on('set_nickname')
def handle_set_nickname(data):
    nickname = data.get('nickname')
    if request.sid in users:
        old_nickname = users[request.sid].get('nickname', 'Anonymous')
        users[request.sid]['nickname'] = nickname
        emit('nickname_updated', {'sid': request.sid, 'nickname': nickname})
        emit('user_list', list(users.values()), broadcast=True)
        emit('message', {'nickname': 'System', 'text': f'{old_nickname} changed nickname to {nickname}.'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
