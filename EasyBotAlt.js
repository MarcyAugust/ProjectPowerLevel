const { ChatClient } = require('twitch-chat-client');
const { RefreshableAuthProvider, StaticAuthProvider } = require('twitch-auth');

const clientId = 'zxlbhj12189pl3p4ouv93ogankagju';
const accessToken = '';
const clientSecret = '';
const refreshToken = '';
const authProvider = new RefreshableAuthProvider(
    new StaticAuthProvider(clientId, accessToken),
    {
        clientSecret,
        refreshToken,
        onRefresh: (token) => {
            console.log(token);
            // do things with the new token data, e.g. save them in your database
        }
    }
);\

const createBot = async () => {
    // listen to more events...
    const chatClient = new ChatClient(authProvider, { channels: ['kelgand'] });
    await chatClient.connect();

    chatClient.onMessage((channel, user, message, msg) => {
        console.log(message);
    });
}

createBot();