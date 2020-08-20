import asyncio

from confluent_kafka import Consumer, Producer, OFFSET_BEGINNING
from confluent_kafka.admin import AdminClient, NewTopic


BROKER_URL = "PLAINTEXT://localhost:9092"


async def consume(topic_name):
    """Consumes data from the Kafka Topic"""
    # Sleep for a few seconds to give the producer time to create some data
    await asyncio.sleep(2.5)

    # TODO: What happens if we try `earliest` or `latest` offset?
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "0"})

    # TODO: Configure the on_assign callback
    c.subscribe([topic_name], on_assign=on_assign)

    while True:
        message = c.poll(1.0)
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            print(f"consumed message {message.key()}: {message.value()}")
        await asyncio.sleep(0.1)


def on_assign(consumer, partitions):
    """Callback for when topic assignment takes place"""
    # TODO: Configure on_assign to offset to the beginning
    consumer.assign(partitions)


def main():
    """Runs the exercise"""
    client = AdminClient({"bootstrap.servers": BROKER_URL})
    try:
        asyncio.run(produce_consume("com.udacity.lesson2.sample5.iterations"))
    except KeyboardInterrupt as e:
        print("shutting down")
        # TODO: Uncomment when you want to delete
        # client.delete_topics(["com.udacity.lesson2.sample5.iterations"])


async def produce(topic_name):
    """Produces data into the Kafka Topic"""
    p = Producer({"bootstrap.servers": BROKER_URL})

    curr_iteration = 0
    while True:
        p.produce(topic_name, f"iteration {curr_iteration}".encode("utf-8"))
        curr_iteration += 1
        await asyncio.sleep(0.1)


async def produce_consume(topic_name):
    """Runs the Producer and Consumer tasks"""
    t1 = asyncio.create_task(produce(topic_name))
    t2 = asyncio.create_task(consume(topic_name))
    await t1
    await t2


if __name__ == "__main__":
    main()