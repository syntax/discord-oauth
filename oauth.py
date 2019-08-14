import requests

class oauth(object):
    client_id = ''
    client_secret = ''
    scope = ''
    redirect_uri = 'http://127.0.0.1:5000/login'
    discord_login_url = f'https://discordapp.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}'
    discord_token_url = 'https://discordapp.com/api/oauth2/token'
    discord_api_url = 'https://discordapp.com/api'

    @staticmethod
    def get_accesstoken(code):
        payload = {
            'client_id': oauth.client_id,
            'client_secret': oauth.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': oauth.redirect_uri,
            'scope': oauth.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = requests.post(url = oauth.discord_token_url,data = payload,headers = headers)
        json = access_token.json()
        return json.get('access_token')

    @staticmethod
    def get_userjson(access_token):
        url = oauth.discord_api_url+'/users/@me'
        headers = {
            'Authorisation': f'Bearer {access_token}'
        }

        user_obj = requests.get(url = url, headers = headers)
        user_json = user_obj.json()
        return user_json
