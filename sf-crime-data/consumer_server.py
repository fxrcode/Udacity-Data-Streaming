from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic
import asyncio

BROKER_URL = "localhost:9092"
TOPIC = "com.udacity.police-call"


async def consume(topic_name):
    """Consume messages from kafka topic"""

    c = Consumer(
        {
            "bootstrap.servers": BROKER_URL,
            "group.id": "0",
            "auto.offset.reset": "earliest",
        }
    )
    c.subscribe([topic_name])

    while True:
        message = c.poll(1.0)
        if message is None:
            print("no message received by consumer")
        elif message.error() is not None:
            print(f"error from consumer {message.error()}")
        else:
            try:
                print(message.value())
            except KeyError as e:
                print(f"Failed to unpack message {e}")
        await asyncio.sleep(1.0)


def main():
    try:
        asyncio.run(consume(TOPIC))
    except KeyboardInterrupt as e:
        print("Shutting down", e)


if __name__ == "__main__":
    main()
