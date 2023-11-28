Based on [Understanding Python Async](https://ruarfff.com/posts/understanding-python-async).

First setup the python environment, then setup the Google Cloud emulators:

```
gcloud beta emulators pubsub start --project=example-project
```

Then this makes sure the Pubsub library hits our emulators instead of Google's servers.

```
$(gcloud beta emulators pubsub env-init)
```

Then install the requirements with

```
pip install -r requirements.txt
```

## Creating the subscription and topic

To create them, run `python main.py`. It will output subscription and topic paths.
