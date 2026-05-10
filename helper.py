import requests

LOGIN_URL = "http://chocolate.cyber.org.il/Account/Login"
# "http://ec2-52-27-145-33.us-west-2.compute.amazonaws.com/Account/Login"
# "http://localhost:50168/Account/Login"


def execute_request(url, email, password):
    data = dict(email=email, password=password)

    r = requests.post(LOGIN_URL, data=data, allow_redirects=True)
    return str(r.content)


def check_password_correct(email, password):
    request_content = execute_request(LOGIN_URL, email, password)
    return ("The user name or password provided is incorrect." not in request_content) and ("Password must be at least 4 characters" not in request_content)


def get_password(*args):
    password = ""

    for num in args:
        password += str(num)
    return password


num = ord('a')
char = chr(97)
