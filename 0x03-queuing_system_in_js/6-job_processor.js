import kue from 'kue';

// create the Kue que
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);   
}

queue.process('push_notification_code', (job, done) => {
    const { phoneNumber, message } = job.data; // extract phoneNumber and message
    sendNotification(phoneNumber, message); // call sendNotification with job's data
    done(); // mark job as done
});
