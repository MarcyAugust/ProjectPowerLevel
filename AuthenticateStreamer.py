import twitchio
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.oauth import refresh_access_token
from twitchAPI.type import AuthScope, TwitchAPIException
from pprint import pprint
import configparser
from twitchAPI.helper import first
import asyncio
from twitchAPI.oauth import UserAuthenticationStorageHelper
from typing import List

#Reads config information from .gitignore file
parser = configparser.ConfigParser()
parser.read('config.ini')

passID = parser.get('DEFAULT', 'app_id')
passSecret = parser.get('DEFAULT', 'app_secret')



async def my_token_generator(twitch: Twitch, target_scope: List[AuthScope]):

     # generate new token + refresh token here and return it

     return 'token', 'refresh_token'

async def twitch_example():

    twitch = await Twitch('rj7msdw7x9dhu60lvopjwqtjo36glx', 'uydbanfwn56sqijoi2c7jecli5xxji')
    user = await first(twitch.get_users(logins='marxcie'))
    print(user.id)
    await twitch.close()

    #pulls config information from separate file
    #twitch = Twitch(parser.get('DEFAULT', 'app_id'), parser.get('DEFAULT', 'app_secret'))



    target_scope = [AuthScope.CHAT_READ]
    auth = UserAuthenticator(twitch, target_scope, force_verify=False)
    helper = UserAuthenticationStorageHelper(twitch, target_scope, auth_generator_func=my_token_generator)
    await helper.bind()

    # this will open your default browser and prompt you with the twitch verification website
    #token, refresh_token = parser.get('DEFAULT', 'user_oauth_token'), parser.get('DEFAULT', 'user_oauth_refresh_token')
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, target_scope, refresh_token)
    pprint(twitch.get_users(logins=['Marxcie']))



asyncio.run(twitch_example())


