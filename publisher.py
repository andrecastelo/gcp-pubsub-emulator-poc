from google.cloud import pubsub_v1

INBOUND_EMAILS_TOPIC = "projects/subscription-tests/topics/inbound-emails"


def main(topic_path):
    publisher = pubsub_v1.PublisherClient()
    print(f"Publishing on: {topic_path}")

    for n in range(1, 10):
        data_str = f"Message number {n}"
        # Data must be a bytestring
        data = data_str.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        print(future.result())


if __name__ == "__main__":
    main(topic_path=INBOUND_EMAILS_TOPIC)
