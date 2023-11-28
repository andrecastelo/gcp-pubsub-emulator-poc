Based on [Understanding Python Async](https://ruarfff.com/posts/understanding-python-async).

First setup the python environment, then setup the Google Cloud emulators:

```
gcloud beta emulators pubsub start --project=subscription-test
```

Then this makes sure the Pubsub library hits our emulators instead of Google's
servers.

```
$(gcloud beta emulators pubsub env-init)

```

Then install the requirements with

```

pip install -r requirements.txt

```

## Creating the subscription and topic

To create them, run `python setup.py`. It will create the topic and
subscription for the inbound emails, and the topic for the metrics.

For some reason this command does not print it instantly, so you'll probably
need to press `Ctrl+C` at some point. It will then output something like this:

```
^CEmails topic: Topic already exists
^CEmails topic: Subscription already exists
Emails topic: Subscription path: projects/subscription-tests/subscriptions/inbound-emails-sub
Emails topic: Topic path:        projects/subscription-tests/topics/inbound-emails
^CMetrics topic: Topic already exists
Metrics topic: Topic path:        projects/subscription-tests/topics/metrics
```

## Running the events

To run the events, run `python main.py`.
