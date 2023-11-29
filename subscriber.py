from google.cloud import pubsub_v1
from icecream import ic

INBOUND_EMAILS_SUB = "projects/subscription-tests/subscriptions/inbound-emails-sub"


def main(subscription_path):
    subscriber = pubsub_v1.SubscriberClient()

    def callback(message):
        ic(message)
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription=subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}")

    with subscriber:
        try:
            streaming_pull_future.result(timeout=10)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.


if __name__ == "__main__":
    main(subscription_path=INBOUND_EMAILS_SUB)
