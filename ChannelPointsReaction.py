from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from twitchio.ext import commands
from pprint import pprint
from uuid import UUID
import configparser
from BotStart import Bot


#Reads config information from .gitignore file
parser = configparser.ConfigParser()
parser.read('config.ini')
app_key = parser.get('DEFAULT', 'app_key')
app_secret = parser.get('DEFAULT', 'app_secret')
user_token = parser.get('DEFAULT', 'user_oauth_token')
user_refresh_token = parser.get('DEFAULT', 'user_oauth_refresh_token')
bot_token = parser.get('DEFAULT', 'bot_oauth_token')
bot_refresh_token = parser.get('DEFAULT', 'bot_oauth_refresh_token')


def user_refresh(token: str, refresh_token: str):
    print(f'my new user token is: {token}')

def app_refresh(token: str):
    print(f'my new app token is: {token}')



def callback_whisper(uuid: UUID, data: dict) -> None:
    print('got callback for UUID ' + str(uuid))
    #username = data["data_object"].get("display_name")
    #print(username)
    #user_message = data["data_object"].get("body")
    #print(user_message)# + ": " + user_message) #+ data["data_object"].get("body"))#["recipient"])#, + ": " + data["data_object"]["body"])
    #pprint(data)


def points_redemption_to_console(uuid: UUID, data: dict) -> None:
    print('A channel points reward has been redeemed!')
    #username = data["data_object"].get("display_name")
    #print(username)
    #user_message = data["data_object"].get("body")
    #print(user_message)# + ": " + user_message) #+ data["data_object"].get("body"))#["recipient"])#, + ": " + data["data_object"]["body"])
    #pprint(data)



# setting up Authentication and getting your user id
twitch = Twitch(app_key, app_secret)


#listen don't question me I need all these permissions because reasons
target_scope = [AuthScope.CHANNEL_READ_REDEMPTIONS, AuthScope.ANALYTICS_READ_EXTENSION, AuthScope.ANALYTICS_READ_GAMES, 
                AuthScope.BITS_READ, AuthScope.CHANNEL_READ_SUBSCRIPTIONS, AuthScope.CHANNEL_READ_STREAM_KEY, 
                AuthScope.CHANNEL_EDIT_COMMERCIAL, AuthScope.CHANNEL_READ_HYPE_TRAIN, AuthScope.CHANNEL_MANAGE_BROADCAST, 
                AuthScope.CHANNEL_MANAGE_REDEMPTIONS, AuthScope.CLIPS_EDIT, AuthScope.USER_EDIT, AuthScope.USER_EDIT_BROADCAST, 
                AuthScope.USER_READ_BROADCAST, AuthScope.USER_READ_EMAIL, AuthScope.USER_EDIT_FOLLOWS, AuthScope.CHANNEL_MODERATE, 
                AuthScope.CHAT_EDIT, AuthScope.CHAT_READ, AuthScope.WHISPERS_READ, AuthScope.WHISPERS_EDIT, AuthScope.MODERATION_READ, 
                AuthScope.CHANNEL_SUBSCRIPTIONS, AuthScope.CHANNEL_READ_EDITORS, AuthScope.CHANNEL_MANAGE_VIDEOS, 
                AuthScope.USER_READ_BLOCKED_USERS, AuthScope.USER_MANAGE_BLOCKED_USERS, AuthScope.USER_READ_SUBSCRIPTIONS]
twitch.app_auth_refresh_callback = app_refresh
twitch.user_auth_refresh_callback = user_refresh
twitch.authenticate_app([])



#auth = UserAuthenticator(twitch, target_scope, force_verify=False)
#new_token, new_refresh_token = auth.authenticate()


#Refresh User's tokens, for set_user_authentication, and anything else related to the user
new_token, new_refresh_token = refresh_access_token(user_refresh_token, app_key, app_secret)

# you can get your user auth token and user auth refresh token following the example in twitchAPI.oauth
twitch.set_user_authentication(new_token, target_scope, new_refresh_token)
user_id = twitch.get_users(logins=['MarcyAugust'])['data'][0]['id']



# starting up PubSub
pubsub = PubSub(twitch)
pubsub.start()


# you can either start listening before or after you started pubsub.
uuid = pubsub.listen_channel_points(user_id, points_redemption_to_console)
bot = Bot()
bot.run()


input('press ENTER to close...')
# you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
pubsub.unlisten(uuid)
pubsub.stop()