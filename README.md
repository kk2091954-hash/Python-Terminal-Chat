# 📡 Python Terminal Chat

A lightweight terminal-based two-way chat application built with **Python sockets**, featuring a simple **client–server** architecture for fast, real-time communication over **TCP**.


## 🚀 Overview

This project demonstrates a basic chat system using Python’s built-in socket module.
It includes:

- A Server (waits for incoming connections)
- A Client (connects and exchanges messages with server)

Perfect for beginners learning **network programming**, **TCP sockets** and **real-time** communication using Python.


## ✨ Features

- 🔌 Simple TCP client–server communication
- 💬 Two-way real-time messaging
- 🖥️ Fully terminal-based interface
- 🔁 Client auto-retry until server is online
- ⚙️ Clean and well-structured code
- 📦 No external libraries required
- 🧪 Perfect for learning socket programming


## 📂 Folder Structure

Here’s the structure of the **Python Terminal Chat** project:

```bash
python-terminal-chat/
│── server_chat.py      # Chat server implementation
│── client_chat.py      # Chat client implementation
│── LICENSE
└── README.md
```


## 🛠 Requirements

- Python 3.7+
- Works on Windows, Linux, macOS
- No third-party libraries needed


## ▶️ Getting Started

How to use this **Python Terminal Chat** project:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/iamx-ariful-islam/python-terminal-chat.git
cd python-terminal-chat
```

### 🖥️ Running the Chat Application

#### Start the Server
```bash
python server_chat.py
```

#### Start the Client (in another terminal)
```bash
python client_chat.py
```
Once connected, both sides can send messages to each other in real-time.


## 📌 Usage Example

### Server Terminal
```bash
[SERVER] Waiting for connection on 127.0.0.1:443
[SERVER] Connected with ('127.0.0.1', 58425)
Server: Hello client!
Client: Hello server!
```

### Client Terminal
```bash
[CLIENT] Trying to connect to 127.0.0.1:443
[CLIENT] Connected to server
Server: Hello client!
Client: Hello server!
```


## 📘 Learning Objectives

This project helps you understand:

- Socket creation
- Binding and listening on ports
- Accepting incoming connections
- Sending & receiving messages
- Basic error handling
- Clean client–server communication patterns


## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome! ❤️<br/>
To contribute:

1. Fork the repository
2. Create a new branch (`feature/new-feature`)
3. Commit your changes
4. Push and submit a Pull Request

💬 You can also open an issue if you’d like to discuss a feature or report a bug.


## 🌐 For more or connect with me

<p align='center'>
  <a href="https://github.com/iamx-ariful-islam"><img src="https://img.shields.io/badge/GitHub-iamx--ariful--islam-black?style=for-the-badge&logo=github" /></a>&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/iamx-ariful-islam"><img src="https://img.shields.io/badge/LinkedIn-Md.%20Ariful%20Islam-blue?style=for-the-badge&logo=linkedin" /></a>&nbsp;&nbsp;
  <a href="https://x.com/mx_ariful_islam"><img src="https://img.shields.io/badge/X-Md.%20Ariful%20Islam-black?style=for-the-badge&logo=x&logoColor=white" /></a>&nbsp;&nbsp;
  <a href="https://www.facebook.com/iamx.ariful.islam/"><img src="https://img.shields.io/badge/Facebook-MD.%20Ariful%20Islam-%231877F2.svg?style=for-the-badge&logo=facebook&logoColor=white" /></a>
</p>


## 📜 License

The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)


## 💖 Thank You for Visiting!

> “Good networking is about making communication simple yet real-time”  
> — *Md. Ariful Islam*