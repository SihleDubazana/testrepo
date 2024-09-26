import jwt

class Decoder:

    def decode(jwt_token):

        token = jwt_token.split(' ')[1]
        
        return jwt.decode(token, algorithms=['HS256'], options={"verify_signature": False})