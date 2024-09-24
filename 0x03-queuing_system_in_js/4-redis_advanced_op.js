const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Connect to Redis server
client.on('connect', function() {
    console.log('Redis client connected to the server');
});

// Handle error events
client.on('error', function (err) {
    console.error('Redis error:', err);
});

// Using hset to add values to a Redis hash
client.hset('HolbertonSchools', 'Portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);

// Retrieve all values using hgetall
client.hgetall('HolbertonSchools', function(err, reply) {
    if (err) throw err;
    console.log(reply);
});

// Close the Redis connection
client.quit();
