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
		return sms.replyToSMS(from_number, from_contents.lower(), len(sms.Queue))
	else:
		if len(sms.Queue) == 0:
			first = get_template_attribute('first.html', 'firstLoad')
			return first(SERVER_NUMBER)
		else:
			return displayPage()

def displayPage():
	video = get_template_attribute('index.html', 'vid')
	Titles = sms.Titles[1:]
	sms.Titles.pop(0)
	return video(sms.Queue.pop(0), Titles)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
