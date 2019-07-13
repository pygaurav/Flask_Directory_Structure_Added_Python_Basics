from app import app,Resource
from app.security import secure

class Admin(Resource):
    def get(self):
        return "<h1> Hello World Admin </h1>"
