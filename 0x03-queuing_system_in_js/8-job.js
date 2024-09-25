function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error(`Jobs is not an array`);
    }

    jobs.forEach((jobdData) => {
        const job = queue.createJob('push_notification_code_3', jobdData)
            .save((error) => {
            if (!error) {
                console.log(`Notification job created: ${job.id}`);
            } else {
                console.error(`Failed to create job: ${error}`);
            }
            })
        
    // hanlde job events
    job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
    });
    // Handle the 'failed' event
    job.on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
    });
    // handle 'progress event
    job.on('progress', (progress) => {
        console.log(`Notification job #${job.id} ${progress}% complete`)
    });
    })
}

export default createPushNotificationsJobs;
