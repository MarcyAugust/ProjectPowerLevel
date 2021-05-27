from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from twitchAPI.types import AuthScope
import configparser
from pprint import pprint


#TO DO: For user token and refresh token, implement:
#App starts -> checks file for saved tokens -> loads tokens if found, if not then triggers the "get tokens" code -> other files ask the prior one for tokens when needed.
#Or just first time program starts, trigger get tokens code -> save to file -> comment that out and assume you'll always have them and always load from file
#From Kelgand.

parser = configparser.ConfigParser()
parser.read('config.ini')

#parameters: app_key, app_secret
twitch = Twitch(parser.get('DEFAULT', 'app_key'), parser.get('DEFAULT', 'app_secret'))

print(twitch)

target_scope = [AuthScope.USER_READ_SUBSCRIPTIONS]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = auth.authenticate()

#new_token, new_refresh_token = refresh_access_token(refresh_token, 'client_id', 'client_secret')
#pprint(new_token, new_refresh_token_)

twitch.set_user_authentication(token, target_scope, refresh_token)
pprint(twitch.get_users(logins=['MarcyAugust']))
