# 💬 Real-Time Chat Application

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-green?logo=flask&logoColor=white)
![WebSockets](https://img.shields.io/badge/WebSockets-Real--Time-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A modern, real-time chat application with private rooms and message history**

[Live Demo](#) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-quick-start)

</div>

---

## 🌟 Overview

A fully-functional, production-ready chat application that enables real-time communication in private rooms. Built with modern web technologies and best practices, featuring WebSocket connections for instant message delivery, persistent message history, and a clean, responsive UI.

## ✨ Key Features

### 🔐 **Private Room System**
- Create instant chat rooms with unique 4-character codes
- Join existing rooms using secure room codes
- Automatic room cleanup when empty

### ⚡ **Real-Time Messaging**
- Instant message delivery using WebSocket technology
- Live user join/leave notifications
- No page refresh required
- Sub-second message latency

### 📊 **Message History**
- Personal message history for every user
- Persistent storage using SQLAlchemy ORM
- Timestamp tracking for all messages
- Easy access to conversation history

### 🎨 **Modern UI/UX**
- Clean, responsive design
- Intuitive user interface
- Real-time message updates
- Mobile-friendly layout

## 🛠 Tech Stack

### Backend
- **Flask** - Lightweight WSGI web application framework
- **Flask-SocketIO** - WebSocket implementation for real-time bidirectional communication
- **SQLAlchemy** - SQL toolkit and Object-Relational Mapping (ORM)
- **Gunicorn + Eventlet** - Production-grade WSGI server with async workers

### Frontend
- **HTML5/CSS3** - Modern semantic markup and styling
- **JavaScript (ES6+)** - Client-side interactivity
- **Socket.IO Client** - Real-time event-based communication

### Database
- **SQLite** (Development) - Lightweight, serverless database
- **PostgreSQL** (Production) - Enterprise-grade relational database

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ecisterna/Online-Chat-App.git
   cd Online-Chat-App
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Access the app**
   
   Open your browser and navigate to `http://localhost:5000`

## 🏗 Architecture Highlights

- **Event-Driven Architecture**: Leverages WebSocket events for real-time updates
- **Session Management**: Secure Flask sessions for user state
- **Database Persistence**: Relational database design with proper foreign keys
- **Scalable Design**: Ready for horizontal scaling with proper session handling
- **Production-Ready**: Configured with Gunicorn and environment-based settings

## 📁 Project Structure

```
Online-Chat-App/
├── main.py                 # Application entry point & route handlers
├── templates/              # Jinja2 HTML templates
│   ├── base.html          # Base template with shared layout
│   ├── home.html          # Landing page & room selection
│   ├── room.html          # Chat room interface
│   └── history.html       # Message history view
├── static/                # Static assets
│   └── css/
│       └── style.css      # Application styles
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔑 Core Functionality

### Room Management
```python
# Automatic room code generation
# Dynamic room creation and cleanup
# Real-time member count tracking
```

### Real-Time Events
```python
# User join/leave notifications
# Instant message broadcasting
# Connection state management
```

### Data Persistence
```python
# User registration and tracking
# Message history storage
# Timestamp management with timezone support
```

## 🌐 Deployment

This application is production-ready and can be deployed to various platforms:
- **Render** (Recommended) - Easy deployment with free tier and WebSocket support
- **Heroku** - Easy deployment with add-ons
- **AWS/GCP/Azure** - Enterprise deployment options

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Emiliano Félix Cisterna**
- GitHub: [@ecisterna](https://github.com/ecisterna)

## 🙏 Acknowledgments

- Built with Flask and Flask-SocketIO
- Inspired by modern chat applications
- Designed with scalability and maintainability in mind

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ and Python

</div>
