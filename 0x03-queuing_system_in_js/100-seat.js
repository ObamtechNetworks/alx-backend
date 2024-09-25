import kue from 'kue';
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

// create the Redis client
const client = redis.createClient();

// Promisify Redis methods for async/await usage
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);  // Corrected this line

let reservationEnabled = true;
const queue = kue.createQueue();
const app = express();
const PORT = 1245;
const availableSeatsKey = 'available_seats';

// create a function reserveSeat
async function reserveSeat(number) {
    return await setAsync(availableSeatsKey, number);
}

async function getCurrentAvailableSeats() {
    const seats = await getAsync(availableSeatsKey);
    return parseInt(seats);
}

// Initialize available seats to 50 when launching the app
client.set(availableSeatsKey, 50);

// Route to get the current number of available seats
app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats: availableSeats });
});

// route to reserve a seat
app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: "Reservation are blocked" });
    }

    const job = queue.create('reserve_seat')
        .save((error) => {
            if (error) {
                return res.json({ status: "Reservation failed" });
            }
            res.json({ status: "Reservation in process" });
        });
    
    job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
    });

    job.on('failed', (errorMessage) => {
        console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
})

// route to process the reservation queue
app.get('/process', (req, res) => {
    res.json({ status: "Queue processing" });

    queue.process('reserve_seat', async (job, done) => {
        let availableSeats = await getCurrentAvailableSeats();

        if (availableSeats > 0) {
            availableSeats -= 1;
            await reserveSeat(availableSeats);

            if (availableSeats === 0) {
                reservationEnabled = false;
            }

            done();
        } else {
            done(new Error('Not enough seats available'))
        }
    });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
