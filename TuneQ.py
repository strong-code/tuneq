from flask import Flask, request, redirect, session, get_template_attribute, render_template
import os
import sms, config

app = Flask(__name__)

SERVER_NUMBER = config.SERVER_NUMBER
SID = config.SID
TOKEN = config.TOKEN

@app.route("/", methods=['GET', 'POST'])
def getText():

	from_number = request.values.get('From', None)
	from_contents = request.values.get('Body', None)

	if from_contents is not None:
		return sms.replyToSMS(from_number, from_contents.lower(), len(sms.URLqueue))
	else:
		if len(sms.URLqueue) == 0:
			#This should return a nicely formatted template, but this works for now
			return 'No videos in queue! Text ' + SERVER_NUMBER + ' with \"add [TRACK TITLE]\" to add a song!'
		else:
			return displayPage()

def displayPage():
	video = get_template_attribute('index.html', 'vid')
	url = sms.URLqueue.pop(0)
	return video(url)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)