from twitchio.ext import commands
from twitchAPI.oauth import refresh_access_token
from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.types import AuthScope
from twitchAPI.oauth import UserAuthenticator

import configparser
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

#Refresh Bot's token, so that it can run itself as well as listen for channel things. 
new_bot_token, new_bot_refresh_token = refresh_access_token(bot_refresh_token, app_key, app_secret)
irc_token_fixed = 'oauth:' + new_bot_token





#pass in irc token and app key in when initalizing bot
class Bot(commands.Bot):

    def __init__(self):
        #irc_token is bot irc token, client_id is from app client_id, nick is username that's logged in, initial channels is where the bot goes to live.
        super().__init__(irc_token=irc_token_fixed, client_id=app_key, nick='AugustMarcy', prefix='!',
                         initial_channels=['MarcyAugust'])




    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a decorator...
    @commands.command(name='test')
    async def test_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')
        #keyboard.press('a')
        #keyboard.release('a')


    @commands.command(name='screenshot')
    async def screenshot_command(self, ctx):
        #await ctx.send(f'Screenshot')
        keyboard.press(Key.f12)
        keyboard.release(Key.f12)

    @commands.command(name='dash')
    async def dash_command(self, ctx):
        #await ctx.send(f'Dashing')
        keyboard.press('p')
        time.sleep(0.2)
        keyboard.release('p')

    @commands.command(name='up')
    async def up_command(self, ctx):
        #await ctx.send(f'Up')
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')

    @commands.command(name='down')
    async def down_command(self, ctx):
        #await ctx.send(f'down')
        keyboard.press('s')
        time.sleep(1)
        keyboard.release('s')

    @commands.command(name='left')
    async def left_command(self, ctx):
        #await ctx.send(f'left')
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')

    @commands.command(name='right')
    async def right_command(self, ctx):
        #await ctx.send(f'right')
        keyboard.press('d')
        time.sleep(1)
        keyboard.release('d')

    @commands.command(name='attack')
    async def attack_command(self, ctx):
        #await ctx.send(f'attack')
        keyboard.press('o')
        time.sleep(1)
        keyboard.release('o')

    @commands.command(name='pause')
    async def space_command(self, ctx):
        #await ctx.send(f'pause')
        keyboard.press(Key.space)
        time.sleep(1)
        keyboard.release(Key.space)


    #@commands.command(name='topgames')
    #async def top_games(self, ctx):
    #    top_games_currently = await super().get_chatters('MarcyAugust')
    #    print(top_games_currently)
    #    await ctx.send(top_games_currently)

        #Combine get_users with get_chatters to have both ids and names available?
    #@commands.command(name='followback')
    #async def following_back(self, ctx):
    #    mutual_following = await super().get_follow({ctx.author.name}, 'AugustMarcy')
    #    print(mutual_following)
    #    await ctx.send(f'Followback status: ' + mutual_following)

