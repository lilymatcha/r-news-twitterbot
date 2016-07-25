#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy, time, sys, praw
 
# connect to twitter
CONSUMER_KEY = 'fill in here'
CONSUMER_SECRET = 'fill in here'
ACCESS_KEY = 'fill in here'
ACCESS_SECRET = 'fill in here'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
# get the reddit stuff here
r = praw.Reddit('app to post top of r/news')
already_posted = []

def write_tweet(post):
	return post.title + " djflksdjfl " + post.url

def post_relevant_posts(posts):
	for post in posts:
		if post.score > 2000 and post.id not in already_posted:
			api.update_status(write_tweet(post))
			already_posted.append(post.id)

while True:
	submissions = r.get_subreddit('news').get_top(limit=10)
	post_relevant_posts(submissions)
	time.sleep(1800)