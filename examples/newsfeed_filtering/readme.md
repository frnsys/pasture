## Newsfeed filtering

This is an example application using Pasture. In this application, students can try implementing their own newsfeed filtering algorithms and see their effects.

This example uses tweets collected from a few hashtags. Tweets have been anonymized (usernames have been replaced with random animals, mentions are blacked out, and tweet ids have been removed). Refer to the `scripts/` folder for more info.

A fake social graph was also constructed from the tweets so that social information (relationships) can be used for the filtering algorithms. You can take a peek at this graph by visiting `http://localhost:5001/graph`.

The libraries required for a newsfeed filtering algorithm can be particularly heinous to setup, especially if your students are not experienced in this kind of thing. And students may all have different computers/OSes, each with its own idiosyncracies which may take hours to figure out. Some students have Chromebooks and I have no idea how to set any of this up on those! So this is a great use of Pasture - set the environment up on a machine you control and let everyone share it :)

### Setup

    virtualenv -p python ~/env/pasture_newsfeeds --no-site-packages
    source ~/env/pasture_newsfeeds/bin/activate
    pip install pasture
    pip install -r requirements.txt

### Usage

To run this example:

    python application.py

Then, in your browser, visit `http://localhost:5001`.
You should be redirected to your own coding session.

You can open the newsfeed paired with this session by opening another tab at `http://localhost:5001/feed/<your session id>`,
where `<your session id>` is whatever random animal you were assigned. For example, `SemanticEstablishedSardine`.

To filter your newsfeed, you just need to define a function with the signature `filter(tweets)`. This should return a list of tweet dictionaries. For examples, see [`example_filters.py`](example_filters.py). You can just copy and paste any of those functions into the interpreter and hit "Run" to see your newsfeed updated.

If you get stuck, you can run `print(HELP)` in the interpreter to get some extra info.
