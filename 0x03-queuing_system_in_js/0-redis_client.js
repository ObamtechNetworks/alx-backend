import { createClient } from "redis";

async function startNodeRedis() {
    try {
        const client = createClient();
        await client.connect();

        await client.set('myKey', 'Hello test node redis');
        // const myKeyValue = await client.get('myKey');
        console.log('Redis client connected to the server');

    } catch (error) {
        console.error(`Redis client not connected to the server: ${error}`);
    }
}

startNodeRedis();
