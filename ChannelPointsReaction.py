from twitchAPI.eventsub import EventSub
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from twitchio.ext import commands
from pprint import pprint
from uuid import UUID
import configparser
from BotStart import Bot
import asyncio
from pynput.keyboard import Key, Controller
from pynput.mouse import Button
import time

#mouse = Controller()
keyboard = Controller()


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
    #pprint(data)


def points_redemption_to_console(uuid: UUID, data: dict) -> None:
    chan = bot.get_channel("Marxcie")
    loop = asyncio.get_event_loop()
    #keyboard.press(Key.f12)
    #keyboard.release(Key.f12)
    #loop.create_task(chan.send("A channel points reward has been redeemed!"))
    #print("A channel points reward has been redeemed!")
    #data_dict = data
    #pprint(dict)
   #data_redemption = data_dict[]
    #keyboard.press(Key.f12)
    #keyboard.release(Key.f12)
    #pprint(data)
    #if( == "Lurking but hiya :3"):


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



auth = UserAuthenticator(twitch, target_scope, force_verify=False)
marcy_token, marcy_refresh_token = auth.authenticate()


#Refresh User's tokens, for set_user_authentication, and anything else related to the user


#new_token, new_refresh_token = refresh_access_token(user_refresh_token, app_key, app_secret)

#Uncomment this and comment above if it breaks
new_token, new_refresh_token = refresh_access_token(bot_refresh_token, app_key, app_secret)
#marcy_token, marcy_refresh_token = refresh_access_token(user_refresh_token, app_key, app_secret)
print(new_token)
print(new_refresh_token)

# you can get your user auth token and user auth refresh token following the example in twitchAPI.oauth

#This below is the Bot's Oauth Reauthorization, we want to use My oauth reauthorization
#twitch.set_user_authentication(new_token, target_scope, new_refresh_token)
twitch.set_user_authentication(marcy_token, target_scope, marcy_refresh_token)
#Test for PubSub stuffs
#twitch.set_user_authentication(marcy_token, target_scope, marcy_refresh_token)
user_id = twitch.get_users(logins=['Marxcie'])['data'][0]['id']

    

# starting up PubSub
eventSub = EventSub(twitch)
eventSub.start()


# you can either start listening before or after you started pubsub.

# REMOVE BELOW COMMENT AT SOME POINT PROBABLY IDFK
# THIS ONE
# RIGHT HERE
# FOR THE LOVE OF GOD REMEMBER IT 
uuid = EventSub.listen_channel_points(user_id, points_redemption_to_console)
#uuid = pubsub.listen_whispers(user_id, callback_whisper)
bot = Bot()
bot.run()



input('press ENTER to close...')
# you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
eventSub.unlisten(uuid)
eventSub.stop()