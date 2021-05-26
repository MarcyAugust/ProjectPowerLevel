from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from twitchAPI.types import AuthScope
from pprint import pprint



twitch = Twitch('zcqh30g4nc79kkbc648a7aaox4mof0', 'jm3fqk7xvk7iyx3lvamtkkh4ov5x4b')


target_scope = [AuthScope.BITS_READ]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
# this will open your default browser and prompt you with the twitch verification website
token, refresh_token = auth.authenticate()
#new_token, new_refresh_token = refresh_access_token(refresh_token, 'client_id', 'client_secret')
#pprint(new_token, new_refresh_token_)

twitch.set_user_authentication(token, target_scope, refresh_token)
pprint(twitch.get_users(logins=['MarcyAugust']))
