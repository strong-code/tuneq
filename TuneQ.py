from flask import Flask, request, redirect, session, get_template_attribute, render_template
from twilio.rest import TwilioRestClient
import twilio.twiml
import os

SERVER_NUMBER = '14155084527'
SID = 'AC03706901f9c1fe2bda57e15395da6a0d'
TOKEN = '0a1f88c479541c3ff4b1769c5651b964'
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def showVideo():
	from_number = request.values.get('From', None)
	from_contents = request.values.get('Body', None)

	if from_number is not None and from_contents is not None:
		return replyToSMS(from_number, from_contents)
	else:
		video = get_template_attribute('index.html', 'vid')
		url = 'http://www.youtube.com/embed/7W194GQ6fHI'
		return video(url)

def replyToSMS(from_number, from_contents):

	resp = twilio.twiml.Response()
	resp.sms('You texted from ' + from_number + 'with the text ' + from_contents)
	return str(resp)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug = True)