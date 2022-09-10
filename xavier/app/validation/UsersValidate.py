
class UsersValidate:

    def forgotPassword(req):
        if req['email'] is None:
            return {
                "status":False,
                "message":"email required"
            }
        else:
            return {
                "status":True,
                "message":"success"
            }
