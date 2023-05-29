from datetime import datetime, timedelta
import jwt


class JwtToken(object):

    _salt = "@^4_00wedv**pi)+(!w1rwi=d3q4l=ie=g-u$s8jevmj*zgg2h" 

    _expire_message = dict(code=1200, msg="token 已经失效")

    _unknown_error_message = dict(code=4200, msg="token 解析失败")

    @classmethod
    def generate_token(cls, payload: dict) -> str:
        headers = dict(typ="jwt", alg="HS256")
        resut = jwt.encode(payload=payload, key=cls._salt, algorithm="HS256", headers=headers)
        return resut

    @classmethod
    def parse_token(cls, token: str) -> tuple:
        verify_status = False
        try:
            payload_data = jwt.decode(token, cls._salt, algorithms=['HS256'])
            verify_status = True
        except jwt.ExpiredSignatureError:
            payload_data = cls._expire_message
        except Exception as _err:
            payload_data = cls._unknown_error_message
        return verify_status, payload_data
    
def test():
    print(datetime.utcnow() - timedelta(seconds=10), datetime.utcnow(), timedelta(seconds=1))
    TEST_DATA = dict(name="mooor", exp=datetime.utcnow() + timedelta(seconds=1))
    
    token = JwtToken.generate_token(TEST_DATA)
    print(token)
    payload = JwtToken.parse_token(token)
    print(payload)

test()
