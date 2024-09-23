const { createClient } = require('redis');
const { promisify } = require('util');

// Create Redis client
const client = createClient();

// Set up event listeners
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Connect to Redis server
client.connect().catch(console.error);

// Promisify Redis methods
const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// Function to set a new key-value pair in Redis
async function setNewSchool(schoolName, value) {
  try {
    const reply = await setAsync(schoolName, value);
    console.log(reply);
  } catch (error) {
    console.error(`Error setting school: ${error.message}`);
  }
}

// Function to get and display the value of a key
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error(`Error getting school value: ${error.message}`);
  }
}

// Main execution function
async function main() {
  // First call to display an uninitialized value
  await displaySchoolValue('Holberton');

  // Set new school and then display its value
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

// Run the main function
main().catch(console.error);
