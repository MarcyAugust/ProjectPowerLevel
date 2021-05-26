import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'App_Key': 'my_app_key',
					 'App_Secret': 'my_app_secret',
					  'User_IRC_Token': 'user_irc_token'}
with open('config.ini', 'w') as configfile:
	config.write(configfile)