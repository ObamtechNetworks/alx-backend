import kue from 'kue';

const blackListedPoneNumbers = ['4153518780', '4153518781'];

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
    // start tracking job progress
    job.progress(0, 100);

    // check if the phone number is blacklisted
    if (blackListedPoneNumbers.includes(phoneNumber)) {
        // if blacklisted, fail the job and log an error
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    // if not placklisted, update progress to 50%
    job.progress(50, 100);

    // simulate sending the notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // complete the job by calling done without error
    done();
}

//  create the queue processor
queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;

    // call the sendNotification function
    sendNotification(phoneNumber, message, job, done);
});
