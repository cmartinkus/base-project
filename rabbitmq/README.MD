logic to send:

job_requests

API
 |
 ↓
RabbitMQ
 |
 ↓
Worker


job_results

Worker
 |
 ↓
RabbitMQ
 |
 ↓
API

logic to receive: 
job_requests

API
 |
 ↓
RabbitMQ
 |
 ↓
Worker


job_results

Worker
 |
 ↓
RabbitMQ
 |
 ↓
API


idea behind rabbitmq
Sender
  |
  ↓
Exchange  (mail sorting facility)
  |
  ↓
Queue     (mailbox)
  |
  ↓
Consumer  (person reading mail)

or

"I have a job.requested event"

          ↓

RabbitMQ

          ↓

Whoever cares handles it