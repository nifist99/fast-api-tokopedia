from fastapi import Request

class Admin:
    def __init__(
            self,
            privileges: str,
    ):
        self.privileges = privileges

    async def __call__(self, request: Request, call_next):
        # do something with the request object

        if(self.privileges == 'admin'):
            content_type = request.headers.get('Content-Type')
            print(content_type)
            
            # process the request and get the response    
            response = await call_next(request)
            
            return response
        else:
            return {
                "status" :False,
                "code"   :401,
                "message":"You not have access to this route"
            }