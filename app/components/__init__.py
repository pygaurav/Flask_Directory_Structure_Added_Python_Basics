from app import api,admin,security
api.add_resource(admin.Admin,"/admin")
api.add_resource(security.Auth,"/auth")