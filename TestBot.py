from twitchio.ext import commands
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

class Bot(commands.Bot):

    def __init__(self):
        #irc_token is bot irc token, client_id is from app client_id, nick is username that's logged in, initial channels is where the bot goes to live.
        super().__init__(irc_token='bot_irc_token', client_id='app_key', nick='AugustMarcy', prefix='!',
                         initial_channels=['Marxcie'])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)

    # Commands use a decorator...
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='text')
    async def my_command(self, ctx):
        time.sleep(200)
        await ctx.send(keyboard.press('h'))

bot = Bot()
bot.run()