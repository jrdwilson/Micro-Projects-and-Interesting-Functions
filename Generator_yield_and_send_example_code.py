# This example is taken from Jeff Knupp's excellent blog post on
# generators and the 'yield' keyword. Specifically using the send
# keyword to run coroutines. This is an example that is a more
# realistic use of yield/send but does not get explained in the blog
# post.

# Source - https://www.jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

import random

def get_data():
    """Return 3 random integers between 0 and 9"""
    return random.sample(range(10), 3)

def consume():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    """Produces a set of values and forwards them to the pre-defined consumer
    function"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        consumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('Producing...')
        next(producer)
