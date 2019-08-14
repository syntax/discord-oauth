from flask import Flask, render_template, request, redirect, session
from oauth import oauth
app = Flask(__name__)

@app.route("/",methods = ['get'])
def home():
    return redirect(oauth.discord_login_url)

@app.route("/login",methods = ['get'])
def login():
    code = request.args.get('code')
    access_token = oauth.get_accesstoken(code)
    user_json = oauth.get_userjson(access_token)
    print(user_json)
    username = user_json.get('username')
    discrim = user_json.get('discriminator')
    userid = user_json.get('id')
    return 'helllo world'

if __name__ == "__main__":
    app.run(debug=True)
