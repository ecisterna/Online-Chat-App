# 🏛️ Technical Architecture

## System Overview

This chat application follows a client-server architecture with real-time bidirectional communication using WebSockets.

## Architecture Diagram

```
┌─────────────────┐
│   Client Side   │
│                 │
│  HTML/CSS/JS    │
│  Socket.IO      │
└────────┬────────┘
         │
         │ WebSocket
         │ Connection
         │
┌────────▼────────┐
│   Server Side   │
│                 │
│  Flask          │
│  Flask-SocketIO │
│  Gunicorn       │
└────────┬────────┘
         │
         │ ORM
         │
┌────────▼────────┐
│   Database      │
│                 │
│  SQLAlchemy     │
│  SQLite/PG      │
└─────────────────┘
```

## Component Breakdown

### 1. Frontend Layer

**Technologies**: HTML5, CSS3, Vanilla JavaScript, Socket.IO Client

**Responsibilities**:
- User interface rendering
- WebSocket connection management
- Real-time message display
- Event handling (send message, join room)

**Key Files**:
- `templates/room.html` - Chat interface
- `templates/home.html` - Landing page
- `static/css/style.css` - Styling

### 2. Application Layer

**Technologies**: Flask 3.0, Flask-SocketIO 5.3

**Responsibilities**:
- HTTP request routing
- Session management
- WebSocket event handling
- Business logic
- Authentication state

**Key Components**:

#### Routes
- `/` (GET/POST) - Home page, room creation/joining
- `/room` (GET) - Chat room interface
- `/history` (GET) - User message history

#### WebSocket Events
- `message` - Broadcast messages to room members
- `connect` - Handle user joining
- `disconnect` - Handle user leaving

### 3. Data Layer

**Technologies**: SQLAlchemy 2.0, SQLite/PostgreSQL

**Database Schema**:

```sql
-- Users Table
CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

-- Messages Table
CREATE TABLE message (
    id INTEGER PRIMARY KEY,
    room VARCHAR(4) NOT NULL,
    user_id INTEGER NOT NULL,
    content VARCHAR(1000) NOT NULL,
    timestamp DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
```

**Relationships**:
- One-to-Many: User → Messages
- Each message belongs to one user
- Each user can have multiple messages

## Data Flow

### Message Sending Flow

1. User types message and clicks "Send"
2. JavaScript captures event, emits via Socket.IO
3. Server receives message event
4. Server validates session and room membership
5. Message saved to database with timestamp
6. Server broadcasts message to all room members
7. All clients receive and display message

### Room Creation Flow

1. User enters name, clicks "Create Room"
2. POST request to `/` endpoint
3. Server generates unique 4-character code
4. Room created in memory with empty members list
5. User session established with room and name
6. User added to database if new
7. Redirect to `/room` endpoint
8. WebSocket connection established

### Room Joining Flow

1. User enters name and room code
2. POST request to `/` endpoint
3. Server validates room existence
4. User session established
5. Redirect to `/room` endpoint
6. WebSocket joins room channel
7. Join notification broadcast to room
8. Previous messages loaded and displayed

## State Management

### Server-Side State

**Flask Sessions** (encrypted cookies):
- `session['room']` - Current room code
- `session['name']` - User display name
- `session['user_id']` - Database user ID

**In-Memory Storage**:
```python
rooms = {
    'ABCD': {
        'members': 2,
        'messages': [...]
    }
}
```

### Client-Side State

- Socket.IO connection object
- DOM state (message list)
- No persistent storage (stateless client)

## Scalability Considerations

### Current Implementation
- In-memory room storage (single server)
- SQLite database (single file)
- Single Gunicorn worker with Eventlet

### Production Scaling Options

**Horizontal Scaling**:
- Redis for distributed session storage
- PostgreSQL for database
- Multiple Gunicorn workers
- Load balancer (nginx)
- Sticky sessions for WebSocket connections

**Database Optimization**:
- Indexing on `user_id` and `room` columns
- Message archival strategy
- Connection pooling

## Security Measures

1. **Session Security**
   - Encrypted session cookies
   - Secret key from environment variables
   - HTTP-only cookies

2. **Input Validation**
   - Form data validation
   - Room code format checking
   - User name validation

3. **CORS Protection**
   - Configurable allowed origins
   - Production vs development settings

4. **SQL Injection Prevention**
   - SQLAlchemy ORM (parameterized queries)
   - No raw SQL execution

## Error Handling

- WebSocket disconnection handling
- Database error recovery
- Invalid room code handling
- Session expiration handling
- Graceful degradation

## Performance Optimizations

1. **Minimal Database Queries**
   - User lookup cached in session
   - Messages loaded once on room entry

2. **Efficient Broadcasting**
   - Socket.IO room-based targeting
   - Only room members receive messages

3. **Lazy Loading**
   - SQLAlchemy lazy relationships
   - On-demand message history

4. **Auto Cleanup**
   - Empty rooms automatically deleted
   - Memory optimization

## Technology Choices Rationale

### Why Flask?
- Lightweight and flexible
- Excellent for WebSocket integration
- Easy to understand and maintain
- Great ecosystem

### Why Flask-SocketIO?
- Seamless WebSocket integration
- Fallback to long-polling
- Room/namespace support
- Production-ready with Eventlet

### Why SQLAlchemy?
- ORM abstraction
- Database-agnostic
- Prevents SQL injection
- Easy migrations

### Why Gunicorn + Eventlet?
- Production-grade WSGI server
- Async worker support for WebSockets
- Reliable and performant
- Industry standard

## Deployment Architecture

```
Internet
   │
   ▼
Railway Platform
   │
   ├─ Auto-scaling
   ├─ Load Balancing
   ├─ SSL/TLS
   │
   ▼
Gunicorn (Eventlet worker)
   │
   ├─ Flask Application
   ├─ Flask-SocketIO
   │
   ▼
PostgreSQL Database
```

## Monitoring & Logging

- Application logs via Python logging
- Real-time console logs in development
- Railway provides production logs
- WebSocket connection tracking

---

**This architecture demonstrates**:
- Full-stack web development
- Real-time communication systems
- Database design and ORM usage
- Production deployment practices
- Scalable design patterns
- Security best practices
