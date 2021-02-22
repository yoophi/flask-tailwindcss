import os

from flask_tailwindcss import create_app

app = create_app(os.environ.get('FLASK_CONFIG', 'default'))
