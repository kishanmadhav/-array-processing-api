import os
import sys

# Ensure project root is on sys.path so we can import app
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app import app as vercel_app

# Vercel looks for a variable named "app" or a default export.
app = vercel_app


