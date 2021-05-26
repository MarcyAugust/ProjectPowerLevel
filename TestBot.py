from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        #irc_token is user irc token, client_id is from app client_id, nick is username that's logged in, initial channels is where the bot goes to live.
        super().__init__(irc_token='user_irc_token', client_id='client_id', nick='AugustMarcy', prefix='!',
                         initial_channels=['MarcyAugust'])

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



    @commands.command(name='topgames')
    async def top_games(self, ctx):
        top_games_currently = await super().get_chatters('MarcyAugust')
        print(top_games_currently)
        await ctx.send(top_games_currently)


    #Combine get_users with get_chatters to have both ids and names available?
    #@commands.command(name='followback')
    #async def following_back(self, ctx):
    #    mutual_following = await super().get_follow({ctx.author.name}, 'AugustMarcy')
    #    print(mutual_following)
    #    await ctx.send(f'Followback status: ' + mutual_following)


bot = Bot()
bot.run()