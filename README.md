# Online-Chat-App
Online Chat App made with Flask, Flask Socket IO and JavaScript. This app allows you to chat in private rooms with your friends!

## Features
- You can chat in real time with the people in the room
- You can access the room with a code provided by the host.
- Every user has a message history

## Installation

### Local Development
1. Clone the repository or download the zip
   ```bash
   git clone https://github.com/ecisterna/Online-Chat-App.git
   ```
2. Install the dependencies with:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the command:
   ```bash
   python main.py
   ```
4. Click the link and start chatting!

## Deployment

### Deploy on Railway (Recommended)
This app is configured to deploy on Railway. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

**Quick steps:**
1. Push your code to GitHub
2. Go to [railway.app](https://railway.app) and connect your repository
3. Set the `SECRET_KEY` environment variable
4. Deploy!

**Live Demo:** [Your app will be here after deployment]

## Tech Stack
- **Backend:** Flask, Flask-SocketIO
- **Database:** SQLAlchemy (SQLite/PostgreSQL)
- **Real-time:** WebSockets
- **Frontend:** HTML, CSS, JavaScript
