const redis = require('redis');

// Create a Redis client
const subscriber = redis.createClient();


// Handle error events
subscriber.on('error', function (err) {
    console.error('Redis client not connected to the server:', err);
});

// Connect to Redis server
subscriber.on('connect', function() {
    console.log('Redis client connected to the server');

    // on connect, log success message
    subscriber.subscribe('holberton school channel');
});


// listen for messages on the channel
subscriber.on('message', (channel, message) => {
    console.log(message);

    // if message is 'KILL_SERVER', unsubscribe and quit
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe('holberton school channel');
        subscriber.quit
    }
});
