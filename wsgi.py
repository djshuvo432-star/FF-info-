# wsgi.py
from app import app

# This is used by Vercel
application = app

if __name__ == '__main__':
    app.run(debug=True)
