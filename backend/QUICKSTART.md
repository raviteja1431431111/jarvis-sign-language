"""
Quick start guide for Jarvis Backend
"""

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/raviteja1431431111/jarvis-sign-language.git
cd jarvis-sign-language/backend
```

### 2. Setup Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings (optional)
```

### 4. Run Development Server
```bash
python app.py
```

Server starts on `http://localhost:5000`

### 5. Test Installation
```bash
curl http://localhost:5000/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "Jarvis Sign Language Recognition API",
  "version": "1.0.0"
}
```

## Testing with Frontend

### Connect Web Application
The frontend (running on port 3000) will connect to the backend on port 5000.

### Test API Endpoints

**Upload image for sign recognition:**
```bash
curl -X POST http://localhost:5000/api/sign/recognize \
  -F "image=@test_image.jpg"
```

**Get sign dictionary:**
```bash
curl http://localhost:5000/api/sign/dictionary
```

## Docker Deployment

```bash
docker-compose up -d
```

## Troubleshooting

### Issue: ModuleNotFoundError: No module named 'mediapipe'
**Solution:**
```bash
pip install --upgrade mediapipe
```

### Issue: Port 5000 already in use
**Solution:**
```bash
# Change port in .env
API_PORT=5001
python app.py
```

### Issue: Camera/Video processing not working
**Solution:**
- Ensure camera permissions are granted
- Check OpenCV installation: `pip install --upgrade opencv-python`

## Next Steps

1. ✅ Backend running
2. Run frontend: `cd ../web && npm run dev`
3. Connect both apps
4. Test sign recognition
5. Train custom ML model

## Documentation

- [Backend README](README.md)
- [API Documentation](README.md#api-endpoints)
- [Architecture](README.md#architecture)

## Support

For issues, create an issue on GitHub or check [README.md](README.md#troubleshooting)
