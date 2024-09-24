import kue from 'kue';

// create the Kue que
const queue = kue.createQueue();

// define the job data (phoneNumber and message)
const jobData = {
    phoneNumber: '1234567890',
    message: 'Hello! This is a message notification'
}

// create a new job in the 'push notification code' queue
const job = queue.create('push_notification_code', jobData)
    .save((error) => {
        if (!error) {
        console.log(`Notification job created: ${job.id}`);
        } else {
            console.log(`Failed to create job: ${error}`);
    }
    })

// hanlde job events
job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.log('Notification job failed');
    
});
