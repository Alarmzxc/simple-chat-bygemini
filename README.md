# simple-chat-bygemini
# Simple Chat Application

这是一个使用 Flask (后端) 和 SocketIO 实现的简单聊天应用程序。前端使用 HTML, CSS 和 JavaScript 构建。

## 如何运行

### 本地运行 (开发环境)

1.  确保你已经安装了 Python 和 pip。
2.  克隆此仓库到你的本地机器。
3.  导航到 `backend` 目录：
    ```bash
    cd backend
    ```
4.  安装后端依赖：
    ```bash
    pip install -r requirements.txt
    ```
5.  运行后端应用：
    ```bash
    python app.py
    ```
    (请注意，在本地运行时，前端 `index.html` 需要通过一个 Web 服务器来访问，或者你可以修改 `app.py` 来提供静态文件服务。)

### 在 Replit 上部署

1.  将此仓库导入到你的 Replit 账户。
2.  Replit 会自动检测 `requirements.txt` 并安装依赖。
3.  运行 `backend/app.py`。
4.  Replit 会提供一个 Webview URL，你可以在浏览器中打开它来访问聊天应用。

## 功能

* 实时发送和接收消息。
* 显示在线用户列表。
* 可以设置自己的昵称。
* 简单的用户连接和断开通知。

## 技术栈

* **后端:** Python, Flask, Flask-SocketIO
* **前端:** HTML, CSS, JavaScript, Socket.IO Client

## 贡献

欢迎提交 issue 和 pull request。
