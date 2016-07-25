# r-news-twitterbot
Twitterbot that posts whatever is popular on r/news right now, but you can fill in with whatever reddit you want.

It is very unrefined, and pretty much doesn't handle any edge cases. (I made it in about 20 minutes as a proof-of-concept to my friend.)

If you actually wanted to run this, you should get a server running (I suggest using DigitalOcean or AWS) and run it there. Keep in mind that it doesn't keep track of what's been posted except locally--so if you restart the script every five minutes, for example, you might post the same thing twice. You could possibly fix this by writing the IDs of the posts you already tweeted about to a text file somewhere, and reading in that text file at the beginning of the script. If you have a better solution in mind, please let me know; I would be curious to hear it.

#### Resources utilized
http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
https://praw.readthedocs.io/en/stable/index.html