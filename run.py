#!/usr/bin/env python3
"""
Simple startup script for the Array Processing API
"""

import os
import sys
from app import app

if __name__ == '__main__':
    print("🚀 Starting Array Processing API...")
    print("📍 API will be available at: http://localhost:5000")
    print("📖 API Documentation: http://localhost:5000/")
    print("💚 Health Check: http://localhost:5000/health")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)
