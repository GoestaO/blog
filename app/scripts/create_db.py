import os
import sys

sys.path.append(os.getcwd())
#sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from app.main import db

if __name__ == '__main__':
    db.create_all()