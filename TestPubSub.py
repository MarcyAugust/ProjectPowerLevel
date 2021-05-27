from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from pprint import pprint
from uuid import UUID
import configparser


#Reads config information from .gitignore file
parser = configparser.ConfigParser()
parser.read('config.ini')
app_key = parser.get('DEFAULT', 'app_key')
app_secret = parser.get('DEFAULT', 'app_secret')
user_token = parser.get('DEFAULT', 'user_oauth_token')
user_refresh_token = parser.get('DEFAULT', 'user_oauth_refresh_token')



def user_refresh(token: str, refresh_token: str):
    print(f'my new user token is: {token}')

def app_refresh(token: str):
    print(f'my new app token is: {token}')



def callback_whisper(uuid: UUID, data: dict) -> None:
    print('got callback for UUID ' + str(uuid))
    pprint(data)
    #username = data["data_object"].get("display_name")
    #print(username)
    #user_message = data["data_object"].get("body")
    #print(user_message)# + ": " + user_message) #+ data["data_object"].get("body"))#["recipient"])#, + ": " + data["data_object"]["body"])
    #pprint(data)



# setting up Authentication and getting your user id
twitch = Twitch(app_key, app_secret)

target_scope = [AuthScope.WHISPERS_READ]
twitch.app_auth_refresh_callback = app_refresh
twitch.user_auth_refresh_callback = user_refresh
twitch.authenticate_app([])

auth = UserAuthenticator(twitch, [AuthScope.WHISPERS_READ], force_verify=False)
token, refresh_token = user_token, user_refresh_token
new_token, new_refresh_token = refresh_access_token(refresh_token, app_key, app_secret)
print(new_token)
print(new_refresh_token)


# you can get your user auth token and user auth refresh token following the example in twitchAPI.oauth
twitch.set_user_authentication(new_token, target_scope, new_refresh_token)
user_id = twitch.get_users(logins=['MarcyAugust'])['data'][0]['id']


#target_scope = [AuthScope.BITS_READ]




# starting up PubSub
pubsub = PubSub(twitch)
pubsub.start()


# you can either start listening before or after you started pubsub.
uuid = pubsub.listen_whispers(user_id, callback_whisper)
input('press ENTER to close...')
# you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
pubsub.unlisten(uuid)
pubsub.stop()