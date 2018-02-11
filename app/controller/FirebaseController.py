import firebase_admin
from firebase_admin import credentials, db



class FirebaseController:

    def __init__(self):
        if not (len(firebase_admin._apps)):
            cred = credentials.Certificate('serviceAccountKey.json')
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://raspberry-sf.firebaseio.com'})

    def __del__(self):
        if (len(firebase_admin._apps)):
            firebase_admin.delete_app(firebase_admin.get_app())

    def getAll(self):
        components = db.reference('components')
        return components.get()

    def getById(self, id):
        component = db.reference('components/' + id)
        return component.get()

    def getStatus(self, id):
        componentStatus = db.reference('components/' + id + '/status')
        return componentStatus.get()


    def setStatus(self, id, status):
        componentStatus = db.reference('components/' + id + '/status')
        return componentStatus.set(status)
