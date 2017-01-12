from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from classes.blog_config import Configuration # import our configuration data

app = Flask(__name__)
app.config.from_object(Configuration) # use values from our Configuration object
db = SQLAlchemy(app)

