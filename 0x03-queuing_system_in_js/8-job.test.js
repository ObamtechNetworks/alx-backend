import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from "./8-job";

/* eslint-disable no-undef */
// Test suite for createPushNotificationsJobs
describe(`createPushNotificationsJobs`, () => {
    let queue;

    // before each test, create a new queue and enter test mode
    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    // After each test, clear the test queue and exit test mode
    afterEach(() => {
        queue.testMode.clear(); // clears jobs in memory
        queue.testMode.exit(); // Exit test mode
    });

    // Test case: check if an error is thrown when jobs is not an array
    it('should display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
        'Jobs is not an array'
        );
    });

    // Test case: check if two new jobs are added to the queue
    it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 4321 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
    ];

    createPushNotificationsJobs(jobs, queue);

    // validate the number of jobs added to the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // validate the job types and data
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });
});
