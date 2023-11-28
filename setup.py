from google.cloud import pubsub_v1

PROJECT_ID = "subscription-tests"
EMAILS_TOPIC = "inbound-emails"
EMAILS_SUBSCRIPTION = "inbound-emails-sub"
METRICS_TOPIC = "metrics"


def setup_emails_topic():
    """
    Creates the topic and subscription for the inbound emails.
    """
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, EMAILS_SUBSCRIPTION)
    topic_path = publisher.topic_path(PROJECT_ID, EMAILS_TOPIC)

    try:
        topic = publisher.create_topic(request={"name": topic_path})
        print(f"Emails topic: Created topic: {topic.name}")
    except:
        print("Emails topic: Topic already exists")

    try:
        subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})
    except:
        print("Emails topic: Subscription already exists")

    print(f"Emails topic: Subscription path: {subscription_path}")
    print(f"Emails topic: Topic path:        {topic_path}")


def setup_metrics_topic():
    """
    Sets up the metrics topic.
    """
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, METRICS_TOPIC)

    try:
        topic = publisher.create_topic(request={"name": topic_path})
        print(f"Metrics topic: Created topic: {topic.name}")
    except:
        print("Metrics topic: Topic already exists")

    print(f"Metrics topic: Topic path:        {topic_path}")


if __name__ == "__main__":
    setup_emails_topic()
    setup_metrics_topic()
