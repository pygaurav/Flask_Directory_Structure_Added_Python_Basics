from app import app,Resource
import random

class Auth(Resource):
    def get(self):
        return "<h1>Hello World Auth</h1>"


class Student:
    def __init__(self,*args,**kwargs):
        self.description = args[0]
        self.email = kwargs['email']

    def create_ticket(self):
        self.ticket_no = random.randint(5669959595, 57475775475754745)
        self.assigned_to = "Gaurav"
        self.assigned_to_email = "info@ittwist.com"
        print("Your ticket is generated {}".format(self.ticket_no))


