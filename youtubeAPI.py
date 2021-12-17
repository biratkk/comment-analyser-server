from textblob import TextBlob
from dotenv import dotenv_values
import requests


def youtube_comments_fetch(videoID):
	config = dotenv_values(".env")
	api_key = config.get('YOUTUBE_API_KEY')
	# print(api_key)
	params = {
		"part": "snippet",
		"textFormat": "plainText",
		"videoId": videoID,
		"key": api_key,
		# "pageToken": 6,
		"maxResults": 100
	}

	response = requests.get("https://www.googleapis.com/youtube/v3/commentThreads", params=params)
	comments = collate_comments(response.json())
	comment_ratings = [[comment, TextBlob(comment).sentiment.polarity] for comment in comments]
	# print(comment_ratings)
	avg_sentiment_rating = analyse(comment_ratings)
	# print(avg_sentiment_rating)
	return avg_sentiment_rating


def collate_comments(response):
	# print(response)
	return [x["snippet"]["topLevelComment"]["snippet"]["textDisplay"] for x in response["items"]]


def analyse(comment_ratings):
	sum = 0
	for i in comment_ratings:
		sum += i[1]
	avg = sum / len(comment_ratings)

	# normalising the average from -1,1 to 0,100
	avg = 50 + 100 * (avg / 2)
	return avg

# print(youtube_comments_fetch("mSq4w9UemEM"))
