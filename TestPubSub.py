from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from pprint import pprint
from uuid import UUID

def callback_whisper(uuid: UUID, data: dict) -> None:
    print('got callback for UUID ' + str(uuid))
    username = data["data_object"].get("display_name")
    print(username)
    #user_message = data["data_object"].get("body")
    #print(user_message)# + ": " + user_message) #+ data["data_object"].get("body"))#["recipient"])#, + ": " + data["data_object"]["body"])
    #pprint(data)

# setting up Authentication and getting your user id
twitch = Twitch('my_app_key', 'client_id')

twitch.authenticate_app([])
auth = UserAuthenticator(twitch, [AuthScope.WHISPERS_READ], force_verify=False)
token, refresh_token = auth.authenticate()
# you can get your user auth token and user auth refresh token following the example in twitchAPI.oauth
twitch.set_user_authentication(token, [AuthScope.WHISPERS_READ], refresh_token)
user_id = twitch.get_users(logins=['MarcyAugust'])['data'][0]['id']

# starting up PubSub
pubsub = PubSub(twitch)
pubsub.start()
# you can either start listening before or after you started pubsub.
uuid = pubsub.listen_whispers(user_id, callback_whisper)
input('press ENTER to close...')
# you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
pubsub.unlisten(uuid)
pubsub.stop()