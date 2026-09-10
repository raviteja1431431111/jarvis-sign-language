# Jarvis Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     CLIENT LAYER                         │
│  ┌──────────────────┐          ┌──────────────────┐    │
│  │  Web Application │          │ Desktop App      │    │
│  │  (React + Vite)  │          │ (Electron)       │    │
│  └────────┬─────────┘          └────────┬─────────┘    │
│           │                             │               │
└───────────┼─────────────────────────────┼───────────────┘
            │                             │
            └──────────────┬──────────────┘
                           │
            ┌──────────────▼──────────────┐
            │     API GATEWAY / WebSocket │
            └──────────────┬──────────────┘
                           │
┌──────────────────────────┼──────────────────────────┐
│                    BACKEND LAYER                    │
│  ┌──────────────────────────────────────────────┐  │
│  │  Node.js/Python API Server                   │  │
│  │  - Request handling                          │  │
│  │  - WebSocket management                      │  │
│  │  - Data validation                           │  │
│  └──────────────────┬──────────────────────────┘  │
│                     │                              │
│  ┌──────────────────▼──────────────────────────┐  │
│  │  ML/AI Processing Layer                     │  │
│  │  - Sign language recognition model          │  │
│  │  - Pose detection (MediaPipe)               │  │
│  │  - Frame preprocessing                      │  │
│  └──────────────────┬──────────────────────────┘  │
└──────────────────────┼───────────────────────────────┘
                       │
            ┌──────────▼──────────┐
            │  DATA LAYER         │
            │  - Cache (Redis)    │
            │  - Database (SQL)   │
            │  - File Storage     │
            └─────────────────────┘
```

## Component Details

### Frontend Components
- **VideoCapture**: Handles camera stream and frame capture
- **TextDisplay**: Shows recognized text and history
- **SpeechOutput**: Manages text-to-speech conversion
- **SettingsPanel**: User preferences and configuration

### Backend Components
- **WebSocket Server**: Real-time communication
- **ML Pipeline**: Video frame processing
- **Database**: User data persistence
- **Cache Layer**: Performance optimization

### ML Model Pipeline
1. Video frame capture
2. Hand detection
3. Keypoint extraction
4. Feature processing
5. Sign classification
6. Confidence calculation
7. Text generation

## Data Flow

1. User starts video capture
2. Video stream sent to backend via WebSocket
3. ML model processes frames
4. Sign detected → Text generated
5. Text sent back to frontend
6. Text displayed and passed to TTS
7. Speech synthesized and played
