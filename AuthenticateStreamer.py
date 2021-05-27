from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from twitchAPI.types import AuthScope
from pprint import pprint
import configparser


#Reads config information from .gitignore file
parser = configparser.ConfigParser()
parser.read('config.ini')

#pulls config information from separate file
twitch = Twitch(parser.get('DEFAULT', 'app_key'), parser.get('DEFAULT', 'app_secret'))



target_scope = [AuthScope.USER_READ_SUBSCRIPTIONS]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)


# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = parser.get('DEFAULT', 'user_oauth_token'), parser.get('DEFAULT', 'user_oauth_refresh_token')


twitch.set_user_authentication(token, target_scope, refresh_token)
pprint(twitch.get_users(logins=['MarcyAugust']))
