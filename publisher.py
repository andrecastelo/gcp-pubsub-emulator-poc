from google.cloud import pubsub_v1

INBOUND_EMAILS_TOPIC = "projects/subscription-tests/topics/inbound-emails"


def main(topic_path):
    publisher = pubsub_v1.PublisherClient()
    print(f"Publishing on: {topic_path}")
    future = publisher.publish(topic_path, b"hello")
    future.result()


if __name__ == "__main__":
    main(topic_path=INBOUND_EMAILS_TOPIC)
