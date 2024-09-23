import { createClient } from 'redis'

function startNodeRedis () {
  
    const client = createClient();
      client.on('connect', () => {
        console.log('Redis client connected to the server')
    })
    client.on('error', (error) => {
        console.error(`Redis client not connected to the server: ${error}`)
    });
    
    return client
}

function setNewSchool (schoolName, value) {
  const client = startNodeRedis();
  client.set(schoolName, value, print);
}

function displaySchoolValue (schoolName) {
  const client = startNodeRedis();
    client.get(schoolName, (error, reply) => {
        if (error) {
            console.log(`Error retrieving value: ${error}`);
        } else {
            console.log(reply); // log the value for the school
      }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
