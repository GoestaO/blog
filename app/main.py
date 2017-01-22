from views import *
from entries.blueprint import entries

from app import app, db
app.register_blueprint(entries, url_prefix='/entries')

if __name__ == '__main__':
    app.run()