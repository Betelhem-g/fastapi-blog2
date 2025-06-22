import uvicorn
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def start_server():
    try:
        print("🚀 Starting FastAPI Blog Server...")
        print("📍 Server: http://localhost:8000")
        print("📚 Docs: http://localhost:8000/docs")
        
        from main import app
        
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, log_level="info")
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("Install dependencies: pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ Server Error: {e}")

if __name__ == "__main__":
    start_server()
