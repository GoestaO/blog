import os, sys
sys.path.append(os.getcwd())
#sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

from main import db

if __name__ == '__main__':
    db.create_all()