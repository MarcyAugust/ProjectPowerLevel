from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import asyncio
import configparser
from twitchio.ext import commands


from pynput.keyboard import Key, Controller as kController
from pynput.mouse import Button, Controller as mController
import time

mouse = mController()
keyboard = kController()

parser = configparser.ConfigParser()
parser.read('config.ini')
irc_token_fixed = None

APP_ID = parser.get('DEFAULT', 'app_id')
APP_SECRET = parser.get('DEFAULT', 'app_secret')
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = 'marxcie'


# this will be called when the event READY is triggered, which will be on bot start
async def on_ready(ready_event: EventData):
    print('Bot is ready for work, joining channels')
    # join our target channel, if you want to join multiple, either call join for each individually
    # or even better pass a list of channels as the argument
    await ready_event.chat.join_room(TARGET_CHANNEL)
    # you can do other bot initialization things in here


# this will be called whenever a message in a channel was send by either the bot OR another user
async def on_message(msg: ChatMessage):
    print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')


# this will be called whenever someone subscribes to a channel
async def on_sub(sub: ChatSub):
    print(f'New subscription in {sub.room.name}:\\n'
          f'  Type: {sub.sub_plan}\\n'
          f'  Message: {sub.sub_message}')


# this will be called whenever the !reply command is issued
async def test_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply('you did not tell me what to reply with')
    else:
        await cmd.reply(f'{cmd.user.name}: {cmd.parameter}')

async def press_w(cmd: ChatCommand):
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')

async def press_mouse_right(cmd: ChatCommand):
        mouse.press(Button.right)
        mouse.release(Button.right)
    
async def press_meow(cmd:ChatCommand):
        time.sleep(5)
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(1)
        keyboard.press(Key.space)
        time.sleep(2)
        keyboard.release(Key.space)

async def press_smile(cmd:ChatCommand):
        time.sleep(3)
        mouse.position = 911, 447
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        mouse.position = 1166, 913
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        mouse.position = 970, 320
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.4)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = 928, 253
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.2)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        time.sleep(0.8)
        keyboard.press('S')
        time.sleep(0.4)
        keyboard.press('M')
        time.sleep(0.4)
        keyboard.press('I')
        time.sleep(0.4)
        keyboard.press('L')
        time.sleep(0.4)
        keyboard.press('E')
        time.sleep(0.8)
        keyboard.press('.')
        time.sleep(0.4)
        keyboard.press('E')
        time.sleep(0.4)
        keyboard.press('X')
        time.sleep(0.4)
        keyboard.press('E')
        time.sleep(1.5)
        mouse.position = 944, 60
        time.sleep(0.2)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(1)
        mouse.position = 742, 199
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        mouse.position = 545, 321
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        keyboard.press('S')
        time.sleep(0.4)
        keyboard.press('M')
        time.sleep(0.4)
        keyboard.press('I')
        time.sleep(0.4)
        keyboard.press('L')
        time.sleep(0.4)
        keyboard.press('E')
        time.sleep(0.8)
        keyboard.press('.')
        time.sleep(0.4)
        keyboard.press('E')
        time.sleep(0.4)
        keyboard.press('X')
        time.sleep(0.4)
        keyboard.press('E')
        time.sleep(1.5)
        mouse.position = 694, 986
        time.sleep(1)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(5)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(0.3)
        mouse.move(-50,0)
        time.sleep(0.3)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        mouse.move(110,-400)
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.2)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(0.2)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(1)
        keyboard.press('e')
        keyboard.release('e')
        time.sleep(0.5)
        mouse.position = 1034, 459
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        mouse.position = 714, 682
        time.sleep(0.5)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(0.5)
        mouse.position = 959, 528
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(1)
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.press(Key.shift_l)
        time.sleep(0.2)
        keyboard.press('a')
        time.sleep(34.5)
        keyboard.release('w')
        time.sleep(37.4)
        keyboard.release('a')
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')
        keyboard.release(Key.shift_l)

        #This part here is the bridge between the two halves
        time.sleep(1)
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')
        time.sleep(0.1)
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        keyboard.press('d')
        time.sleep(0.2)
        keyboard.release('d')
        time.sleep(0.2)
        keyboard.press('w')
        time.sleep(0.4)
        keyboard.release('w')
        time.sleep(0.2)
        keyboard.press('a')
        time.sleep(0.3)
        keyboard.release('a')
        time.sleep(0.5)
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.release('s')
        time.sleep(0.2)
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        time.sleep(0.2)
        mouse.press(Button.left)
        mouse.release(Button.left)

        #This is where the bridge ends

        keyboard.press('s')
        time.sleep(0.55)
        keyboard.release('s')
        time.sleep(0.5)
        keyboard.press('a')
        time.sleep(0.35)
        keyboard.release('a')
        time.sleep(0.5)
        keyboard.press('p')
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        keyboard.release('p')
        time.sleep(0.5)
        keyboard.press('d')
        time.sleep(0.25)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        keyboard.release('d')
        time.sleep(0.2)
        keyboard.press('p')
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        keyboard.release('p')
        time.sleep(0.5)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.2)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.3)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.2)
        keyboard.press('a')
        time.sleep(0.25)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        keyboard.release('p')
        time.sleep(0.3)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.1)
        time.sleep(0.5)
        keyboard.release('a')
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.2)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.3)
        keyboard.press('d')
        time.sleep(2.9)
        keyboard.release('d')
        time.sleep(0.1)
        keyboard.press('s')
        time.sleep(2.4)
        keyboard.release('s')
        time.sleep(1)


async def test(cmd:ChatCommand):
        time.sleep(1)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.2)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.3)
        keyboard.press('s')
        time.sleep(0.75)
        keyboard.release('s')
        time.sleep(0.5)
        keyboard.press('a')
        time.sleep(0.55)
        keyboard.release('a')
        time.sleep(0.5)
        keyboard.press('p')
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        keyboard.release('p')
        time.sleep(0.5)
        keyboard.press('d')
        time.sleep(0.25)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        keyboard.release('d')
        time.sleep(0.2)
        keyboard.press('p')
        time.sleep(0.2)
        mouse.press(Button.right)
        mouse.release(Button.right)
        keyboard.release('p')
        time.sleep(0.5)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.2)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.3)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.2)
        keyboard.press('a')
        time.sleep(0.25)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.2)
        keyboard.release('p')
        time.sleep(0.3)
        mouse.press(Button.right)
        mouse.release(Button.right)
        time.sleep(0.1)
        time.sleep(0.5)
        keyboard.release('a')
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.2)
        keyboard.press('p')
        time.sleep(0.1)
        keyboard.release('p')
        time.sleep(0.3)
        keyboard.press('d')
        time.sleep(2.9)
        keyboard.release('d')
        time.sleep(0.1)
        keyboard.press('s')
        time.sleep(2.4)
        keyboard.release('s')
        time.sleep(1)



async def move_mouse(cmd:ChatCommand):
        time.sleep(1)
        keyboard.press('w')
        keyboard.press('w')

async def find_mouse(cmd:ChatCommand):
        time.sleep(1)
        print('Current pos: {0}'.format(mouse.position))
        
# this is where we set up the bot
async def run():
    # set up twitch api instance and add user authentication with some scopes
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    irc_token_fixed = 'oauth:' + token
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # create chat instance
    chat = await Chat(twitch)

    # register the handlers for the events you want

    # listen to when the bot is done starting up and ready to join channels
    chat.register_event(ChatEvent.READY, on_ready)
    # listen to chat messages
    chat.register_event(ChatEvent.MESSAGE, on_message)
    # listen to channel subscriptions
    chat.register_event(ChatEvent.SUB, on_sub)
    # there are more events, you can view them all in this documentation

    # you can directly register commands and their handlers, this will register the !reply command
    chat.register_command('reply', test_command)
    chat.register_command('up', press_w)
    chat.register_command('place', press_mouse_right)
    chat.register_command('meow', press_meow)
    chat.register_command('mouse', find_mouse)
    chat.register_command('smile', press_smile)
    chat.register_command('m', move_mouse)
    chat.register_command('test', test)

    # we are done with our setup, lets start this bot up!
    chat.start()

    # lets run till we press enter in the console
    try:
        input('press ENTER to stop\\n')
    finally:
        # now we can close the chat bot and the twitch api client
        chat.stop()
        await twitch.close()

    class Bot(commands.Bot):

        def __init__(self):
         #irc_token is bot irc token, client_id is from app client_id, nick is username that's logged in, initial channels is where the bot goes to live.
         super().__init__(irc_token=irc_token_fixed, client_id=APP_ID, nick='AugustMarcy', prefix='!',
                         initial_channels=['Marxcie'])




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


# lets run our setup
asyncio.run(run())

#pass in irc token and app id in when initalizing bot
