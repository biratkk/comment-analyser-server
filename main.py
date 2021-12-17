import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from youtubeAPI import youtube_comments_fetch

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/getCommentAnalysis": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/getCommentAnalysis')
@cross_origin()
def get_comment_analysis():
	# Structure of request
	# {
	# 	videoId:"videoId"
	# }
	response = jsonify(rating=str(youtube_comments_fetch(request.args.get("videoId"))))
	if request.method == "GET":
		return response


app.run(port=5000)
