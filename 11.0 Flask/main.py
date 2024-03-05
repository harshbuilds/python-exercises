from flask import Flask, render_template, request
import jwt_helper
import json
from google.oauth2 import id_token
from google.auth.transport import requests
import config

CLIENT_ID = config.client_id

app = Flask(__name__)
app.secret_key = config.app_secret_key


@app.route('/')
def index():
    return "Main page"


@app.route('/auth', methods=['GET'])
def auth():
    return render_template("trial.html")


@app.route('/user_data', methods=['GET'])
def user_data():
    print(request.headers.get('Authorization'));
    user_token = request.headers.get('Authorization')
    verified = jwt_helper.verify(user_token, app.secret_key)
    if verified:
        return {
            'data': jwt_helper.decode(user_token, app.secret_key),
            'success': True,
        }
    else:
        return {
            'success': False,
        }


@app.route('/verifyGoogleToken', methods=['POST'])
def post_test():
    token_data = request.get_json()
    print(json.dumps)
    try:
        idinfo = id_token.verify_oauth2_token(token_data['credential'], requests.Request(), CLIENT_ID)
        print(idinfo, idinfo['sub'], idinfo['email'], sep="\n")
        a = {
            'sub': idinfo['sub'],
            'email': idinfo.get('email', 'test@example.com')
        }
        print(a)
        token = jwt_helper.encode({
            'sub': idinfo['sub'],
            'email': idinfo.get('email', 'test@example.com')
        }, app.secret_key)
        return {
            'valid': True,
            'token': token
        }
    except:
        return {'valid': False}


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8096, debug=True)
