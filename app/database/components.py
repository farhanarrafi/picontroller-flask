import firebase_admin
from firebase_admin import credentials, db


def initialize():
    if not (len(firebase_admin._apps)):
        cred = credentials.Certificate('serviceAccountKey.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://raspberry-sf.firebaseio.com'})


def get_all():
    initialize();
    ref = db.reference('components')
    return ref.get()