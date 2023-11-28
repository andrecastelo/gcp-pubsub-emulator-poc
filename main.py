from google.cloud import pubsub_v1


def create_subscription():
    project_id = "example-project"
    topic_id = "emails"
    subscription_id = "emails-subscription"

    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    topic_path = publisher.topic_path(project_id, topic_id)
    try:
        subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})
    except:
        print("Subscription already exists")

    print(f"Subscription path: {subscription_path}")
    print(f"Topic path:        {topic_path}")
