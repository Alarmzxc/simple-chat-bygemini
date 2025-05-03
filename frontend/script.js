const socket = io();
const messages = document.getElementById('messages');
const messageInput = document.getElementById('message');
const sendButton = document.getElementById('send');
const userList = document.getElementById('user-list');
const nicknameInput = document.getElementById('nickname');
const setNicknameButton = document.getElementById('set-nickname-btn');

let currentNickname = '';

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('user_connected', (data) => {
    const newUser = document.createElement('li');
    newUser.textContent = `User ${data.sid.substring(0, 5)} connected`;
    // messages.appendChild(newUser); // 可以选择显示连接通知在消息区域
});

socket.on('user_disconnected', (data) => {
    // const userLeft = document.createElement('li');
    // userLeft.textContent = `User ${data.sid.substring(0, 5)} disconnected`;
    // messages.appendChild(userLeft); // 可以选择显示断开通知在消息区域
});

socket.on('user_list', (users) => {
    userList.innerHTML = '';
    users.forEach(user => {
        const li = document.createElement('li');
        li.textContent = user.nickname;
        userList.appendChild(li);
    });
});

socket.on('nickname_updated', (data) => {
    if (socket.id === data.sid) {
        currentNickname = data.nickname;
    }
});

socket.on('message', (data) => {
    const newMessage = document.createElement('li');
    newMessage.innerHTML = `<strong>${data.nickname}:</strong> ${data.text}`;
    messages.appendChild(newMessage);
    messages.scrollTop = messages.scrollHeight; // 保持滚动到底部
});

sendButton.addEventListener('click', () => {
    const messageText = messageInput.value.trim();
    if (messageText) {
        socket.emit('new_message', { text: messageText });
        messageInput.value = '';
    }
});

messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendButton.click();
    }
});

setNicknameButton.addEventListener('click', () => {
    const nickname = nicknameInput.value.trim();
    if (nickname) {
        socket.emit('set_nickname', { nickname: nickname });
    }
});