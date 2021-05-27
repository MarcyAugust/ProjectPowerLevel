from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from twitchAPI.types import AuthScope
from pprint import pprint
import configparser


#Reads config information from .gitignore file
parser = configparser.ConfigParser()
parser.read('config.ini')
app_key = parser.get('DEFAULT', 'app_key')
app_secret = parser.get('DEFAULT', 'app_secret')
user_token = parser.get('DEFAULT', 'user_oauth_token')
user_refresh_token = parser.get('DEFAULT', 'user_oauth_refresh_token')

#Needed to refresh oauth tokens
new_token, new_refresh_token = refresh_access_token(user_refresh_token, app_key, app_secret)


#uses pulled config information to make new app instance.
twitch = Twitch(app_key, app_secret)


target_scope = [AuthScope.BITS_READ]

auth = UserAuthenticator(twitch, target_scope, force_verify=False)


# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = user_token, user_refresh_token



twitch.set_user_authentication(token, target_scope, refresh_token)
pprint(twitch.get_users(logins=['MarcyAugust']))
